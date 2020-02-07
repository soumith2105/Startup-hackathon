from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.serializers import ValidationError
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password as default_validate_password
from django.db.models import Q
from profiles.models import UserProfile

User = get_user_model()


class StartupUserCreateSerializer(serializers.ModelSerializer):
    confirm_email = serializers.EmailField(label='Confirm email')

    class Meta:
        model = User
        fields = [
            'full_name',
            'username',
            'email_id',
            'confirm_email',
            'mobile_number',
            'genre',
            'password',
        ]

        extra_kwargs = {"password": {"write_only": True}}

    def validate_confirm_email(self, value):
        data = self.get_initial()
        email = data.get("email_id")
        email2 = value
        if email2 != email:
            raise ValidationError("Email id's don't match")
        return value

    def create(self, validated_data):
        full_name = validated_data['full_name']
        username = validated_data['username']
        email_id = validated_data['email_id']
        mobile_number = validated_data['mobile_number']
        genre = validated_data['genre']
        password = validated_data['password']
        user_obj = User(
            full_name=full_name,
            username=username,
            email_id=email_id,
            mobile_number=mobile_number,
            genre=genre,
        )
        user_obj.is_mentor = False
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


class MentorUserCreateSerializer(serializers.ModelSerializer):
    confirm_email = serializers.EmailField(label='Confirm email')

    class Meta:
        model = User
        fields = [
            'full_name',
            'username',
            'email_id',
            'confirm_email',
            'mobile_number',
            'genre',
            'password',
        ]

        extra_kwargs = {"password": {"write_only": True}}

    def validate_confirm_email(self, value):
        data = self.get_initial()
        email = data.get("email_id")
        email2 = value
        if email2 != email:
            raise ValidationError("Email id's don't match")
        return value

    def create(self, validated_data):
        full_name = validated_data['full_name']
        username = validated_data['username']
        email_id = validated_data['email_id']
        mobile_number = validated_data['mobile_number']
        genre = validated_data['genre']
        password = validated_data['password']
        user_obj = User(
            full_name=full_name,
            username=username,
            email_id=email_id,
            mobile_number=mobile_number,
            genre=genre,
        )
        user_obj.is_mentor = True
        user_obj.set_password(password)
        user_obj.save()
        return validated_data


class UserModificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'full_name',
            'username',
            'email_id',
            'mobile_number',
            'genre',
        ]


class UserLoginSerializer(serializers.ModelSerializer):
    id_field = serializers.CharField(label='Username or Email or Mobile number')
    password = serializers.CharField(label='Password')

    class Meta:
        model = User
        fields = [
            'id_field',
            'password',
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, data):
        id_field = data.get("id_field").casefold()
        password = data.get("password").casefold()

        if id_field and password:
            user_obj = UserProfile.objects.filter(
                                Q(username__iexact=id_field) |
                                Q(email_id__iexact=id_field) |
                                Q(mobile_number=id_field)
                            ).distinct()
            if user_obj.exists() and user_obj.count() == 1:
                user_object = user_obj.first()
                user = authenticate(username=user_object.username, password=password)
                if user:
                    data["user"] = user
                else:
                    raise ValidationError("Username or password is incorrect")
        else:
            raise ValidationError("Both fields must be provided")
        return data

    def validate_id_field(self, value):
        if value:
            user_obj = UserProfile.objects.filter(
                                Q(username__iexact=value) |
                                Q(email_id__iexact=value) |
                                Q(mobile_number=value)
                            ).distinct()
            if user_obj.exists() and user_obj.count() == 1:
                return value
            else:
                raise ValidationError("Username or Email or Mobile Number does not exist")


class UserPasswordChangeSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True, max_length=30)
    password = serializers.CharField(required=True, max_length=30)
    confirm_password = serializers.CharField(required=True, max_length=30)

    class Meta:
        model = User
        fields = [
            'old_password',
            'password',
            'confirm_password',
        ]

    def validate_password(self, value):
        default_validate_password(value)
        return value

    def validate_confirm_password(self, value):
        data = self.get_initial()
        password = data.get("password")
        confirm_password = value
        if confirm_password != password:
            raise ValidationError("Passwords don't match")
        return value


class UserDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'username',
            'full_name',
            'email_id',
            'mobile_number',
            'genre',
        ]


class MentorsListSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = [
            'full_name',
            'genre',
        ]
