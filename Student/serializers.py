from rest_framework import serializers
from main.models import Student, Subject


class SubjectSerializers(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'
