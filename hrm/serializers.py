from rest_framework import serializers
from hrm.models import Users

class UserSerializer(serializers.ModelSerializer):
    employee_id = serializers.CharField(required=False)  #all this are provided to just edit any particular field not to madate edit all the fields 
    name = serializers.CharField(required=False)
    ranking = serializers.FloatField(required=False)

    class Meta:
        model = Users
        fields = '__all__' 