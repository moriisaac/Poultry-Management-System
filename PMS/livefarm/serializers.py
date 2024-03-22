

from rest_framework import serializers
from .models import Farm, PoultryHouse, Chicken

class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = '__all__'


class PoultryHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = PoultryHouse
        fields = '__all__'

class ChickenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chicken
        fields = '__all__'
