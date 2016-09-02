from django.db import models
from django.core.urlresolvers import reverse


class Emp(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=70, null=True, blank=True, unique=True)
    sex = models.CharField(max_length=10)

    def get_absolute_url(self):
        return reverse("employee:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.firstName + ' ' + self.lastName
