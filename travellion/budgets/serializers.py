from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import *
from accounts.models import User
from accounts.serializers import UserSerializer
from datetime import datetime


class GroupSerializer(ModelSerializer):
    
    duration = serializers.SerializerMethodField()
    dday = serializers.SerializerMethodField()
    leader = serializers.ReadOnlyField(source = 'leader.nickname')
    member = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Group
        fields = ['groupId', 'leader', 'member', 'title', 'nation', 'location', 'start_date', 'end_date', 'duration', 'budget', 'dday']

    def get_duration(self, obj):
        start_date = obj.start_date
        end_date = obj.end_date
        if start_date and end_date:
            return (end_date - start_date).days
        return None

    def get_dday(self, obj):
        start_date = obj.start_date
        if start_date:
            today = datetime.now().date()
            days_difference = (start_date - today).days
            if days_difference > 0:
                return f"D-{days_difference}일" # D-며칠
            elif days_difference < 0:
                return f"D+{-days_difference}일" # D+며칠
            else:
                return "D-Day"  # 오늘이 start_date랑 같음
        return None
    

class PlanSerializer(ModelSerializer):
    class Meta:
        model = Plan
        fields = ['planId', 'title', 'date', 'day_of_week', 'individual_cost', 'total_cost', '', '', '', '', '', '', ]