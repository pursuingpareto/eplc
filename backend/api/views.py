# from django.shortcuts import render

# from django.http import HttpResponse, JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
from api.models import Event
from api.serializers import EventSerializer
from rest_framework import generics
from rest_framework import permissions

class EventList(generics.ListCreateAPIView):
	queryset = Event.objects.all()
	serializer_class = EventSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset = Event.objects.all()
	serializer_class = EventSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# @csrf_exempt
# def event_list(request):
#     """
#     List all events, or create a new event.
#     """
#     if request.method == 'GET':
#         events = Event.objects.all()
#         serializer = EventSerializer(events, many=True)
#         return JsonResponse(serializer.data, safe=False)

#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = EventSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def event_detail(request, pk):
#     """
#     Retrieve, update or delete an event.
#     """
#     try:
#         event = Event.objects.get(pk=pk)
#     except Event.DoesNotExist:
#         return HttpResponse(status=404)

#     if request.method == 'GET':
#         serializer = EventSerializer(event)
#         return JsonResponse(serializer.data)

#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = EventSerializer(event, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         event.delete()
#         return HttpResponse(status=204)
