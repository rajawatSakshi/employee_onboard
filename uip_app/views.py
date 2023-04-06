from django.shortcuts import render
from rest_framework.generics import ListAPIView,CreateAPIView,DestroyAPIView,UpdateAPIView
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import get_user_model,authenticate
from rest_framework import views, permissions
# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializors import ObtainTokenSerializer,OrganisationSerializer,DepartmentSerializer,RoleSerializer
from .serializors import QuestionsSerializer,AnswersSerializer, UserSerializer, ObtainLoginSerializer
from .authentication import JWTAuthentication
from .models import Users, Organisation, Department,Role,Questions, Answers
import jwt
from django.conf import settings
from django.http import JsonResponse
from rest_framework.views import APIView
from datetime import datetime

User = get_user_model()

class ObtainTokenView(views.APIView):

    
    permission_classes = [permissions.AllowAny]
    serializer_class = ObtainTokenSerializer
    
    def post(self, request, *args, **kwargs):
        
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        emp_id = serializer.validated_data.get('employee_id')

        # import pdb;pdb.set_trace();
        user = User.objects.filter(employee_id=emp_id).first()


        if user is None:
            serializer.save()
        
        jwt_token = JWTAuthentication.create_jwt(emp_id)
        return Response({'token': jwt_token})  
    

class ObtainLoginView(views.APIView):

    permission_classes = [permissions.AllowAny]
    serializer_class = ObtainLoginSerializer
    
    def post(self, request, *args, **kwargs):
        print("hr")

        employee_id = request.data.get('employee_id')
        password = request.data.get('password')
        user = User.objects.filter(employee_id=employee_id, password=password).first()

        if user is None:
            return Response("Invalid username and password")  
        
        jwt_token = JWTAuthentication.create_jwt(employee_id)
        return Response({'token': jwt_token})  



# @permission_classes((permissions.AllowAny,))
# class LoginView(APIView):

    
#     def post(self, request):
#         # import pdb; pdb.set_trace();
#         employee_id = request.data.get('employee_id')
#         password = request.data.get('password')
#         print(employee_id)
#         print(password)
#         # import pdb; pdb.set_trace();
#         # print(authenticate(request, employee_id=employee_id, password=password))
#         # user = authenticate(username=data["username"], password=data["password"])


#         user = authenticate( employee_id=employee_id, password=password)
#         print(user)
        
#         if user is not None:
#             # Generate a JWT token with a payload containing the user ID and expiration time
#             print("hello sakshi rajawat")
            
#             token_payload = {
#                 'user_id': user.id,
#                 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
#             }
#             token = jwt.encode(token_payload, settings.SECRET_KEY, algorithm='HS256')
#             return JsonResponse({'token': token}, status=200)
        
#         else:
#             return JsonResponse({'error': 'Invalid credentials'}, status=400)


    


# oraganisation crud
@permission_classes((permissions.IsAuthenticated, ))  
class ListOrganisationAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer

@permission_classes((permissions.IsAuthenticated, )) 
class CreateOrganisationAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer

@permission_classes((permissions.IsAuthenticated, )) 
class UpdateOrganisationAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer

@permission_classes((permissions.IsAuthenticated, )) 
class DeleteOrganisationAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Todo from the database"""
    queryset = Organisation.objects.all()
    serializer_class = OrganisationSerializer


# department crud
@permission_classes((permissions.IsAuthenticated, )) 
class ListDepartmentAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

@permission_classes((permissions.IsAuthenticated, )) 
class CreateDepartmentAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

@permission_classes((permissions.IsAuthenticated, )) 
class UpdateDepartmentAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

@permission_classes((permissions.IsAuthenticated, )) 
class DeleteDepartmentAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Todo from the database"""
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer



# role crud
@permission_classes((permissions.IsAuthenticated, )) 
class ListRoleAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

@permission_classes((permissions.IsAuthenticated, )) 
class CreateRoleAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

@permission_classes((permissions.IsAuthenticated, )) 
class UpdateRoleAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

@permission_classes((permissions.IsAuthenticated, )) 
class DeleteRoleAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Todo from the database"""
    queryset = Role.objects.all()
    serializer_class = RoleSerializer



# questions crud
@permission_classes((permissions.IsAuthenticated, )) 
class ListQuestionsAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer

@permission_classes((permissions.IsAuthenticated, )) 
class CreateQuestionsAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer

@permission_classes((permissions.IsAuthenticated, )) 
class UpdateQuestionsAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer

@permission_classes((permissions.IsAuthenticated, )) 
class DeleteQuestionsAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Todo from the database"""
    queryset = Questions.objects.all()
    serializer_class = QuestionsSerializer    


# Answers crud
@permission_classes((permissions.IsAuthenticated, )) 
class ListAnswersAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer


@permission_classes((permissions.IsAuthenticated, )) 
class CreateAnswerAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer


@permission_classes((permissions.IsAuthenticated, )) 
class UpdateAnswersAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer

@permission_classes((permissions.IsAuthenticated, )) 
class DeleteAnswersAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Todo from the database"""
    queryset = Answers.objects.all()
    serializer_class = AnswersSerializer
    


# User crud
@permission_classes((permissions.IsAuthenticated, )) 
class ListUserAPIView(ListAPIView):
    """This endpoint list all of the available todos from the database"""
    queryset = Users.objects.all()
    serializer_class = UserSerializer

@permission_classes((permissions.IsAuthenticated, )) 
class CreateUserAPIView(CreateAPIView):
    """This endpoint allows for creation of a todo"""
    queryset = Users.objects.all()
    serializer_class = UserSerializer

@permission_classes((permissions.IsAuthenticated, )) 
class UpdateUserAPIView(UpdateAPIView):
    """This endpoint allows for updating a specific todo by passing in the id of the todo to update"""
    queryset = Users.objects.all()
    serializer_class = UserSerializer

@permission_classes((permissions.IsAuthenticated, )) 
class DeleteUserAPIView(DestroyAPIView):
    """This endpoint allows for deletion of a specific Todo from the database"""
    queryset = Users.objects.all()
    serializer_class = UserSerializer



@permission_classes((permissions.IsAuthenticated, ))    
class AccessHomePage(views.APIView):
    authentication_classes = [JWTAuthentication]

    def get(self, request):
        token = request.COOKIES.get("jwt")
        return Response("Welcome to employee registrations page")
