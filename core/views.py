from rest_framework import viewsets
from .serializers import DisciplineSerializer, StudySessionSerializer
from django.db.models import Sum
from django.utils.timezone import now
from datetime import timedelta
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Discipline, StudySession
from .serializers import DisciplineSerializer
from .utils import format_duration


class DisciplineViewSet(viewsets.ModelViewSet):
    queryset = Discipline.objects.all()
    serializer_class = DisciplineSerializer

    @action(detail=True, methods=['get'])
    def stats(self, request, pk=None):
        discipline = self.get_object()
        sessions = StudySession.objects.filter(discipline=discipline)

        # total geral
        total_time = sessions.aggregate(
            total=Sum('total_time')
        )['total']

        # meses
        monthly = {}
        for month in range(1, 13):
            month_sum = sessions.filter(
                start__month=month
            ).aggregate(total=Sum('total_time'))['total']

            monthly[month] = format_duration(month_sum)

        # semana atual (segunda → domingo)
        today = now().date()
        start_week = today - timedelta(days=today.weekday())
        end_week = start_week + timedelta(days=6)

        week_sum = sessions.filter(
            start__date__range=(start_week, end_week)
        ).aggregate(total=Sum('total_time'))['total']

        return Response({
            "total_time": format_duration(total_time),
            "january": monthly[1],
            "february": monthly[2],
            "march": monthly[3],
            "april": monthly[4],
            "may": monthly[5],
            "june": monthly[6],
            "july": monthly[7],
            "august": monthly[8],
            "september": monthly[9],
            "october": monthly[10],
            "november": monthly[11],
            "december": monthly[12],
            "current_week": format_duration(week_sum)
        })


class StudySessionViewSet(viewsets.ModelViewSet):
    queryset = StudySession.objects.all()
    serializer_class = StudySessionSerializer
