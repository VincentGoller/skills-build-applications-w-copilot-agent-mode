from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='dc', description='DC superheroes')

        # Create users
        users = [
            User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel.name),
            User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel.name),
            User.objects.create(name='Wonder Woman', email='wonderwoman@dc.com', team=dc.name),
            User.objects.create(name='Batman', email='batman@dc.com', team=dc.name),
        ]

        # Create activities
        Activity.objects.create(user=users[0], activity_type='Running', duration=30, date='2024-04-01')
        Activity.objects.create(user=users[1], activity_type='Cycling', duration=45, date='2024-04-02')
        Activity.objects.create(user=users[2], activity_type='Swimming', duration=60, date='2024-04-03')
        Activity.objects.create(user=users[3], activity_type='Yoga', duration=40, date='2024-04-04')

        # Create workouts
        Workout.objects.create(name='Hero HIIT', description='High intensity workout for heroes', suggested_for='marvel')
        Workout.objects.create(name='Power Yoga', description='Yoga for strength and flexibility', suggested_for='dc')

        # Create leaderboard
        Leaderboard.objects.create(user=users[0], points=100)
        Leaderboard.objects.create(user=users[1], points=90)
        Leaderboard.objects.create(user=users[2], points=110)
        Leaderboard.objects.create(user=users[3], points=95)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
