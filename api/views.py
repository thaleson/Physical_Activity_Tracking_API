from rest_framework import viewsets
from .models import Exercise, Goal, Workout
from .serializers import ExerciseSerializer, GoalSerializer, WorkoutSerializer
from rest_framework.response import Response
from datetime import datetime
from rest_framework import status
from django.db.models import Count, Avg, Sum

from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


class ExerciseViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows exercises to be viewed or edited.
    """
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class GoalViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows goals to be viewed or edited.
    """
    queryset = Goal.objects.all()
    serializer_class = GoalSerializer


class WorkoutViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows workouts to be viewed or edited.
    """
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer


class GoalProgressReportView(APIView):
    """
    API endpoint that provides a report of the user's progress towards their goals.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        Returns a report of progress for each goal of the authenticated user.

        Args:
            request: The HTTP request object.

        Returns:
            Response: A JSON response with the progress report.
        """
        user = request.user
        goals = Goal.objects.filter(user=user)
        report = []
        for goal in goals:
            progress = goal.achieved
            target = goal.target
            percentage = (progress / target) * 100 if target else 0
            report.append({
                'name': goal.name,
                'target': target,
                'achieved': progress,
                'percentage': round(percentage, 2),
            })
        return Response(report)


class ExerciseStatisticsView(APIView):
    """
    API endpoint that provides statistics about the user's exercises within a specified date range.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        Returns statistics about the user's exercises within the given date range.

        Args:
            request: The HTTP request object. Requires 'start_date' and 'end_date' query parameters.

        Returns:
            Response: A JSON response with the total duration and number of exercises.
        """
        user = request.user
        start_date = request.query_params.get('start_date')
        end_date = request.query_params.get('end_date')

        if not start_date or not end_date:
            return Response({"error": "start_date and end_date are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            start_date = datetime.strptime(start_date, '%Y-%m-%d')
            end_date = datetime.strptime(end_date, '%Y-%m-%d')
        except ValueError:
            return Response({"error": "Invalid date format. Use YYYY-MM-DD."}, status=status.HTTP_400_BAD_REQUEST)

        workouts = Workout.objects.filter(user=user, date__range=[start_date, end_date])
        total_duration = workouts.aggregate(total_duration=Sum('duration'))['total_duration']
        total_exercises = workouts.count()

        return Response({
            'total_duration': str(total_duration),
            'total_exercises': total_exercises
        })


class WorkoutReportView(APIView):
    """
    API endpoint that provides a report of the user's workouts.
    """

    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        """
        Returns a report on the user's workouts including total number, average duration, and most common exercise.

        Args:
            request: The HTTP request object.

        Returns:
            Response: A JSON response with the workout report.
        """
        user = request.user
        workouts = Workout.objects.filter(user=user)
        report = {
            'total_workouts': workouts.count(),
            'average_duration': workouts.aggregate(average_duration=Avg('duration'))['average_duration'],
            'most_common_exercise': workouts.values('exercise__name').annotate(count=Count('exercise')).order_by('-count').first()
        }
        return Response(report)

