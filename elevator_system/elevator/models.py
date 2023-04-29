from django.db import models

# Create your models here.

class Elevator(models.Model):
    name = models.CharField(max_length=255)
    current_floor = models.IntegerField()
    destination_floor = models.IntegerField()
    is_moving_up = models.BooleanField(default=False)
    is_moving_down = models.BooleanField(default=False)
    is_door_open = models.BooleanField(default=False)
    is_running = models.BooleanField(default=True)
    is_operational = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class FloorRequest(models.Model):
    elevator = models.ForeignKey(Elevator, on_delete=models.CASCADE, related_name='floor_requests')
    floor = models.IntegerField()
    is_up = models.BooleanField()

    def __str__(self):
        return f'{self.floor} ({self.elevator})'