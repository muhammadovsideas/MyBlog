from rest_framework import serializers
from .models import *
from django.contrib.auth.password_validation import validate_password
from main.serializers import *


class UserSerializer(serializers.ModelSerializer):
    skills = SkillSerializer1(many=True, read_only=True)
    softskills = SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name','avatar','phone_number','bio','job','resume','location','github','linkedin','website','skills','softskills')

    def get_softskills(self, obj):
        active_softskills = obj.softskills.filter(is_active=True)
        return SoftSkillSerializer(active_softskills, many=True).data


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    class Meta:
        model = User
        fields = ('id', 'username', 'password','first_name', 'last_name')

    def create(self,validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.is_active = True
        user.set_password(password)
        user.save()
        return user


