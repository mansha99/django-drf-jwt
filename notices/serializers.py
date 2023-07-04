from rest_framework import serializers
from  .models import CustomUser
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import Notice

class RegisterSerializer(serializers.ModelSerializer):
    mobile = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    
    class Meta:
        model = CustomUser
        fields = ('password', 
                  'mobile', 'full_name')
        extra_kwargs = {
            'full_name': {'required': True}
        }

    def validate(self, attrs):
        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create(
            mobile=validated_data['mobile'],
            full_name=validated_data['full_name']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

class NoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notice
        fields = ('__all__')