# api/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExerciseStatisticsView, ExerciseViewSet, GoalProgressReportView, GoalViewSet, WorkoutReportView, WorkoutViewSet

router = DefaultRouter()
router.register(r'exercises', ExerciseViewSet)
router.register(r'goals', GoalViewSet)
router.register(r'workouts', WorkoutViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('goals/progress/', GoalProgressReportView.as_view(), name='goal_progress_report'),
    path('exercises/statistics/', ExerciseStatisticsView.as_view(), name='exercise_statistics'),
    path('workouts/report/', WorkoutReportView.as_view(), name='workout_report'),
]+ router.urls
