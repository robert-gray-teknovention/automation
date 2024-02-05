from django.db import models
import threading
import controller.functions as functions
from datetime import datetime
from django.conf import settings
# Create your models here.


class Function(models.Model):
    name = models.CharField(max_length=100, unique=True)
    args = models.JSONField(null=True)  # Dictionary of the args and kwargs


class Command(models.Model):

    function = models.ForeignKey(Function, on_delete=models.CASCADE)
    args = models.JSONField(null=True)  # Dictionary of the values of args
    executed = models.BooleanField(default=False)
    start = models.DateTimeField(null=True)
    end = models.DateTimeField(null=True)

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
        if kwargs['asyncro']:
            self.run_threaded(func, args)
        else:
            func(*args)
