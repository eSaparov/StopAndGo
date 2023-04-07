from rest_framework import serializers
from .models import *
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        token['username'] = user.username
        return token


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'name', 'surname', 'email',
                  'date_created', 'is_active', 'is_staff']


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    username = serializers.CharField(required=True, validators=[
                                     UniqueValidator(queryset=User.objects.all())])

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'password2',
                  'email', 'name', 'surname', 'is_staff')
        extra_kwargs = {
            'name': {'required': True},
            'surname': {'required': True}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            name=validated_data['first_name'],
            surname=validated_data['last_name'],
            is_active=True,
            is_staff=validated_data['is_active'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'fullname',]


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['index', 'description', 'project', 'responsible']


class Quality_issueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quality_issue
        fields = ['name', 'description',]


class Safety_issueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Safety_issue
        fields = ['name', 'description',]


class Report_SafetySerializer(serializers.ModelSerializer):
    class Meta:
        model = Report_Safety
        fields = ['photo', 'name', 'author', 'responsible',
                  'room', 'created', 'updated', 'is_active', 'status']


class Report_QualitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Report_Quality
        fields = ['photo', 'name', 'author', 'responsible',
                  'room', 'created', 'updated', 'is_active', 'status']
