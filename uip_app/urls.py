from django.urls import path
# from rest_framework.urlpatterns import format_suffix_patterns
from uip_app import views

urlpatterns = [
    path('register/', views.ObtainTokenView.as_view(), name="register"),
    path('home/', views.AccessHomePage.as_view(), name="home"),
    # path('login/', views.LoginView.as_view(), name="login"),
    path('login/', views.ObtainLoginView.as_view(), name="login"),

    #organisation API
    path("organisation",views.ListOrganisationAPIView.as_view(),name="organisation_list"),
    path("organisation_create/", views.CreateOrganisationAPIView.as_view(),name="organisation_create"),
    path("organisation_update/<int:pk>/",views.UpdateOrganisationAPIView.as_view(),name="organisation_update"),
    path("organisation_delete/<int:pk>/",views.DeleteOrganisationAPIView.as_view(),name="organisation_delete"), 

    #department API
    path("department",views.ListDepartmentAPIView.as_view(),name="dep_list"),
    path("department_create/", views.CreateDepartmentAPIView.as_view(),name="dep_create"),
    path("department_update/<int:pk>/",views.UpdateDepartmentAPIView.as_view(),name="dep_update"),
    path("department_delete/<int:pk>/",views.DeleteDepartmentAPIView.as_view(),name="dep_delete"), 

    #role API
    path("role",views.ListRoleAPIView.as_view(),name="role_list"),
    path("role_create/", views.CreateRoleAPIView.as_view(),name="role_create"),
    path("role_update/<int:pk>/",views.UpdateRoleAPIView.as_view(),name="role_update"),
    path("role_delete/<int:pk>/",views.DeleteRoleAPIView.as_view(),name="role_delete"),

    #Questions API
    path("questions",views.ListQuestionsAPIView.as_view(),name="role_list"),
    path("question_create/", views.CreateQuestionsAPIView.as_view(),name="question_create"),
    path("question_update/<int:pk>/",views.UpdateQuestionsAPIView.as_view(),name="question_update"),
    path("question_delete/<int:pk>/",views.DeleteQuestionsAPIView.as_view(),name="question_delete"),

    #Answers API
    path("answers",views.ListAnswersAPIView.as_view(),name="answers_list"),
    path("answers_create/", views.CreateAnswerAPIView.as_view(),name="answers_create"),
    path("answers_update/<int:pk>/",views.UpdateAnswersAPIView.as_view(),name="answers_update"),
    path("answers_delete/<int:pk>/",views.DeleteAnswersAPIView.as_view(),name="answers_delete"),


    #User API
    path("users",views.ListUserAPIView.as_view(),name="users_list"),
    path("user_create/", views.CreateUserAPIView.as_view(),name="user_create"),
    path("user_update/<int:pk>/",views.UpdateUserAPIView.as_view(),name="user_update"),
    path("user_delete/<int:pk>/",views.DeleteUserAPIView.as_view(),name="user_delete"),


    #Notifications API
    path("Notifications",views.ListNotificationsAPIView.as_view(),name="notifications_list"),
    path("Notifications_create/", views.CreateNotificationAPIView.as_view(),name="Notifications_create"),
    path("Notifications_update/<int:pk>/",views.UpdateNotificationAPIView.as_view(),name="Notifications_update"),
    path("Notifications_delete/<int:pk>/",views.DeleteNotificationAPIView.as_view(),name="Notifications_delete"),
]