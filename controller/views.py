import json
import datetime
import pytz
from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .models import Task
from .serializers import *
from .tasks import start_run
from django.utils import timezone


# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):

        task_data = serializer.validated_data
        #options = json.loads(task_data.get('options', '{}'))
        options = {}

        options['meas_duration'] = task_data.get('duration', 3600)
        options['username'] = self.request.user.username
        options['rate_settings'] = {}
        options['pulse_settings'] = {}
        options['velocity_settings'] = {}
        options['decay_settings'] = {}

        for k in self.request.POST:
            v = self.request.POST.get(k)
            if k[:2] == 'do':
                options[k] = True if v == 'true' else False
            if k[:8] == 'velocity' and v != 'NaN' and v:
                options['velocity_settings'][k[9:]] = int(float(v))     # TODO: not so elegant - think about adding fields to serializer
            if k[:4] == 'rate' and v != 'NaN' and v:
                options['rate_settings'][k[5:]] = int(float(v))
            if k[:5] == 'decay' and v != 'NaN' and v:
                options['decay_settings'][k[6:]] = int(float(v))

        res = start_run.apply_async(args=[options],
                                    eta=task_data.get('time').astimezone(datetime.timezone.utc))

        serializer.save(id=res.id, user=self.request.user, options=json.dumps(options))

    def get_queryset(self):
        return super().get_queryset().filter(time__gte=timezone.now()).order_by('time')


