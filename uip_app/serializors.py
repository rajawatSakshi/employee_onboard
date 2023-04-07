# apps/management/api/serializers.py

from rest_framework import serializers
from .models import Users,Organisation,Department, Questions, Role,Answers,Notifications
from django.contrib.auth import authenticate
from rest_framework import serializers



class ObtainTokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"  
        # fields = (
        #     "employee_id",
        #     "password",
        #     "email",
        #     "username"
        # )

class ObtainLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = (
            "employee_id",
            "password"
        )        

# class UserLoginSerializer(serializers.Serializer):
#     employee_id = serializers.CharField()
#     password = serializers.CharField()

#     def validate(self, data):
#         employee_id = data.get('employee_id')
#         password = data.get('password')

#         user = authenticate(employee_id=employee_id, password=password)

#         if not user:
#             raise serializers.ValidationError('Invalid login credentials')

#         data['user'] = Users

#         return data

class OrganisationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organisation
        fields = "__all__"    
        
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"   

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"   

class QuestionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = "__all__"  

class AnswersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answers
        fields = "__all__"  

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = (
            "employee_id",
            "password",
            "email",
            "username",
        )   

class NotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"            