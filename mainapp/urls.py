from django.urls import path
from .import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('register/',views.registerUser,name='register'),
    path('login/', views.loginUser, name='login_user'),
    path('logout/', views.logoutUser, name='logout_user'),
    # path('user-profile/', views.user_profile, name='user_profile'),grouptable
    # path('group-table/',views.grouptable,name='grouptable'),

    path('m-table/',views.mentortable,name='mentor'),
    path('m-create/',views.createMentor,name='mentor-create'),
    path('m-update/<str:pk>',views.updateMentor,name='mentor-update'),
    path('m-delete/<str:pk>',views.deleteMentor,name='mentor-delete'),

    path('s-table/',views.student_table,name='student_table'),
    path('s-create/',views.CreateStudent,name='student_create'),
    path('s-update/<str:pk>',views.updateStudent,name='student_update'),
    path('s-delete/<str:pk>',views.deleteStudent,name='student_delete'),
    
    path('test/',views.testpage,name='test'),

    path('error-404/',views.error_404,name='error_404'),
    path('error-500/',views.error_500,name='error_500'),
]
