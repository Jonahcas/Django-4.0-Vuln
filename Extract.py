from django.db import models
from datetime import datetime
from django.db.models.functions import Extract
class Experiment(models.Model):
    start_datetime = models.DateTimeField()
    start_date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_datetime = models.DateTimeField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)

def main():
    start = datetime(2015, 6, 15)
    end = datetime(2015, 7, 2)
    Experiment.objects.create(
    start_datetime=start, start_date=start.date(),
    end_datetime=end, end_date=end.date())
    # Add the experiment start year as a field in the QuerySet.
    experiment = Experiment.objects.annotate(
    start_year=Extract('start_datetime', 'year')).get()
    experiment.start_year
    # How many experiments completed in the same year in which they started?
    Experiment.objects.filter(
    start_datetime__year=Extract('end_datetime', 'year')).count()