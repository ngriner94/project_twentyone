from rest_framework.serializers import ModelSerializer
from users.models import user

class UserSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = user

