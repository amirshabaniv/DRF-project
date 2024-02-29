from datetime import datetime, timedelta
import random
from django.conf import settings
from rest_framework import serializers

from .models import UserModel, UserProfile



class UserSerializer(serializers.ModelSerializer):

    password1 = serializers.CharField(
        write_only=True,
        min_length=settings.MIN_PASSWORD_LENGTH,
        error_messages={
            "min_length": "Password must be longer than {} characters".format(
                settings.MIN_PASSWORD_LENGTH
            )
        },
    )
    password2 = serializers.CharField(
        write_only=True,
        min_length=settings.MIN_PASSWORD_LENGTH,
        error_messages={
            "min_length": "Password must be longer than {} characters".format(
                settings.MIN_PASSWORD_LENGTH
            )
        },
    )

    class Meta:
        model = UserModel
        fields = (
            "id",
            "phone_number",
            "email",
            "password1",
            "password2"
        )
        read_only_fields = ("id",)

    def validate(self, data):

        if data["password1"] != data["password2"]:
            raise serializers.ValidationError("Passwords do not match")
        return data
    

    def create(self, validated_data):
        
        otp = random.randint(1000, 9999)
        otp_expiry = datetime.now() + timedelta(minutes = 10)

        user = UserModel(
            phone_number=validated_data["phone_number"],
            email=validated_data["email"],
            otp=otp,
            otp_expiry=otp_expiry,
            max_otp_try=settings.MAX_OTP_TRY
        )
        user.set_password(validated_data["password1"])
        user.save()
        # Send OTP with sms.ir or kavenegar or ....
        return user


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ['id', 'first_name', 'last_name', 'address']

    