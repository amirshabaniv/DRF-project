from rest_framework import serializers
from .models import BoardAssembly


class BoardAssemblySerialzier(serializers.ModelSerializer):

    class Meta:
        model = BoardAssembly
        fields = ['id', 'name', 'phone_number',
                  'email', 'file', 'description']