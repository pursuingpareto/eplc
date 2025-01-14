from django.test import TestCase, Client
from api.models import Event
from datetime import datetime
from django.contrib.auth.models import User

class APITestCase(TestCase):
	client = Client()
	new_event_payload = {
		'title': 'new event',
		'description': 'some stuff happens',
		'start': '2025-02-05T12:00:00Z',
		'end': '2025-02-05T13:00:00Z'
	}

	def setUp(self):
		# should appear last chronologically
		Event.objects.create(
			title="1", 
			description="example description 1",
			start=datetime.fromisoformat('2025-02-04T19:00:00Z'),
			end=datetime.fromisoformat('2025-02-04T20:00:00Z')
			)

		# should appear first chronologically
		Event.objects.create(
			title="2", 
			description="example description 2",
			start=datetime.fromisoformat('2025-02-04T17:00:00Z'),
			end=datetime.fromisoformat('2025-02-04T20:00:00Z')
			)

		Event.objects.create(
			title="3", 
			description="example description 3",
			start=datetime.fromisoformat('2025-02-04T18:00:00Z'),
			end=datetime.fromisoformat('2025-02-04T20:00:00Z')
			)

	def test_event_list_returns_valid_json(self):
		response = self.client.get("/api/events/")
		data = response.json()
		self.assertEqual(len(data), 3)
	
	def test_event_list_sorts_by_start_date(self):
		response = self.client.get("/api/events/")
		data = response.json()
		self.assertEqual(data[0]['title'], '2')
		self.assertEqual(data[1]['title'], '3')
		self.assertEqual(data[2]['title'], '1')

	def test_single_event_can_be_retrieved_by_primary_key(self):
		response = self.client.get("/api/events/1/")
		event = response.json()
		self.assertEqual(event['id'], 1)
		self.assertEqual(event['description'], 'example description 1')

	def test_event_cannot_be_created_when_not_logged_in(self):
		response = self.client.post("/api/events/", self.new_event_payload)
		self.assertEqual(response.status_code, 403)
		self.assertEqual(response.json()['detail'], "Authentication credentials were not provided.")

	def test_event_can_be_created_when_logged_in(self):
		user = User.objects.create(username="admin")
		user.set_password('Testing123!')
		user.save()
		logged_in = Client()
		logged_in.login(username='admin', password='Testing123!')
		response = logged_in.post("/api/events/", self.new_event_payload)
		self.assertEqual(response.status_code, 201)
		self.assertEqual(response.json()['title'], 'new event')


