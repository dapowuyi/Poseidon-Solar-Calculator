from rest_framework import serializers
from .models import Appliances, Subscription


# We serializer our Appliance model and validates the fields and they are converted to JSON
class AppliancesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appliances
        fields = ('id', 'appliance', 'watt_per_hour', 'quantity_of_appliance', 
                'hours_used_per_day', 'date')
        lookup_field = 'id'


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ('your_email',)