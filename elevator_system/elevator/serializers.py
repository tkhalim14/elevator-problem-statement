
from rest_framework import serializers
from .models import Elevator, FloorRequest


class ElevatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Elevator
        fields = ["id", "name", "current_floor", "moving_up", "is_working", "is_running"]


class FloorRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FloorRequest
        fields = ["id", "floor_number", "elevator"]
