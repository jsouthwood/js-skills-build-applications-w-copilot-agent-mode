from django.test import TestCase
from .models import User, Team, Activity, Leaderboard, Workout

class ModelTests(TestCase):
    def test_create_team(self):
        team = Team.objects.create(name='Test Team')
        self.assertEqual(team.name, 'Test Team')

    def test_create_user(self):
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpass')
        self.assertEqual(user.email, 'test@example.com')

    def test_create_activity(self):
        user = User.objects.create_user(username='testuser2', email='test2@example.com', password='testpass')
        activity = Activity.objects.create(user=user, activity_type='Run', duration=30, team='Test Team')
        self.assertEqual(activity.activity_type, 'Run')

    def test_create_leaderboard(self):
        leaderboard = Leaderboard.objects.create(team='Test Team', points=100)
        self.assertEqual(leaderboard.points, 100)

    def test_create_workout(self):
        workout = Workout.objects.create(name='Test Workout', description='Desc', suggested_for='Test Team')
        self.assertEqual(workout.name, 'Test Workout')
