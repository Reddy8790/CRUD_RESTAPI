from rest_framework import serializers
from.models import *


class bookserializer(serializer.modelserializer):
    class Meta:
        model=booksmodel
        fields'_all_'