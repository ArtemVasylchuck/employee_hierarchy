from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    hire_date = models.DateField()
    email = models.EmailField()
    manager = models.ForeignKey('self', on_delete=models.CASCADE, related_name='subordinates', null=True, blank=True)

    def __str__(self):
        return self.name

    def get_subordinates(self):
        return self.subordinates.all()

