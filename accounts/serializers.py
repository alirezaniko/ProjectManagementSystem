from rest_framework import serializers
from django.contrib.auth import get_user_model
from django_otp.plugins.otp_totp.models import TOTPDevice

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'role')

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            role=validated_data['role']
        )
        return user


class OTPSerializer(serializers.Serializer):
    otp_code = serializers.CharField()

    def validate_otp_code(self, value):
        user = self.context['request'].user
        if not user.otp_device.verify_token(value):
            raise serializers.ValidationError("Invalid OTP code.")
        return value
