from django.test import TestCase
from api.models import Event
from datetime import datetime, timedelta

class EventTestCase(TestCase):
    def setUp(self):
        Event.objects.create(
        	title="example event", 
        	description="example description",
        	start=datetime.fromisoformat('2025-02-04T18:00:00Z'),
        	end=datetime.fromisoformat('2025-02-04T20:00:00Z')
        	)

    def test_events_are_created(self):
        """Events are created"""
        events = Event.objects.all()
        self.assertEqual(len(events), 1)