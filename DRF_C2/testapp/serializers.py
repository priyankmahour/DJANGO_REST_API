from rest_framework import serializers

class NameSerializer(serializers.Serializer):
    # partner application will send only one field   ie.. name
    name    =serializers.CharField(max_length=10)
