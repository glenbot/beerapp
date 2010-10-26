from django.db import models

TYPE_CHOICES = (('draft', 'Draft'), ('bottle', 'Bottle'), )


class Beer(models.Model):
    name = models.CharField(max_length=150, blank=True)
    type = models.CharField(max_length=25, choices=TYPE_CHOICES)
    style = models.CharField(max_length=75, blank=True)
    description = models.TextField()
    create_dt = models.DateField(auto_now_add=True)
    update_dt = models.DateField(auto_now=True)

    def __unicode__(self):
        return self.name
