from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'priority', 'status', 'created_at', 'updated_at', 'completed_at']

    def validate_due_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Due date must be in the future.")
        return value

    def validate(self, attrs):
        if attrs.get('status') == 'Completed' and not attrs.get('completed_at'):
            attrs['completed_at'] = timezone.now()
        return attrs