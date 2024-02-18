from django.db import models
import threading
import uuid

from datetime import datetime
from django.conf import settings
if settings.SYSTEM == 'pi':
    import controller.pifunctions as functions
else:
    import controller.functions as functions
# Create your models here.


class Function(models.Model):
    name = models.CharField(max_length=100, unique=True)
    args = models.JSONField(null=True)  # Dictionary of the args and kwargs


class ScheduledCommand(models.Model):
    function = models.ForeignKey(Function, on_delete=models.CASCADE)
    args = models.JSONField(null=models.CASCADE)
    asyncro = models.BooleanField(default=False)
    job_id = models.CharField(max_length=40, default=uuid.uuid4())
    interval_number = models.IntegerField(default=1)
    interval = models.CharField(max_length=20)
    at = models.CharField(max_length=5, null=True)
    run_once = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    def run(self):
        cmd = Command()
        cmd.function = self.function
        cmd.args = self.args
        cmd.asyncro = self.asyncro
        cmd.schedule = self
        cmd.run()


class Command(models.Model):

    function = models.ForeignKey(Function, on_delete=models.CASCADE)
    schedule = models.ForeignKey(ScheduledCommand, on_delete=models.CASCADE, null=True)
    args = models.JSONField(null=True)  # Dictionary of the values of args
    executed = models.BooleanField(default=False)
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True)
    asyncro = models.BooleanField(default=False)

    def finished(self):
        self.executed = True
        self.end = settings.TZ.localize(datetime.now())
        self.save()

    def run_threaded(self, job, args):
        thread = threading.Thread(target=job, args=args, kwargs={})
        thread.start()
        # print(thread.result)

    def run(self, **kwargs):
        func = getattr(functions, self.function.name)
        args = []
        args.extend(self.args)
        args.append(self.finished)
        self.start = settings.TZ.localize(datetime.now())
        self.save()
        if self.asyncro:
            self.run_threaded(func, args)
        else:
            func(*args)
