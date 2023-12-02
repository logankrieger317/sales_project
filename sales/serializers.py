from rest_framework import serializers
from .models import User, Profile




class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    user = serializers.HyperlinkedRelatedField(
        view_name="user_detail", read_only=True
    )
    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), source="user"
    )
    
    class Meta:
        model = Profile
        fields = ["user", "age", "position", "availability","profile", "user_id"]
        
class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = serializers.HyperlinkedRelatedField(
        view_name="user_detail", many=True, read_only=True
    )
    profile_id = serializers.PrimaryKeyRelatedField(
        queryset=Profile.objects.all(), source="profile"
    )

    class Meta:
        model = User
        fields = ["name", "position", "profile", "profile_id"]