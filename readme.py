"""CourseSys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, re_path, include
from student import views

urlpatterns = [
    # 学生信息增删改查
    path('', views.student, name='student'),  # 默认index
    path('student/', views.student, name='student'),
    path('add/', views.stu_add, name='add'),
    re_path('delete/(\d+)/', views.delete, name='delete'),
    re_path('edit/(\d+)/', views.edit, name='edit'),
    # 课程信息增删改查
    path('course/', views.course, name='course'),
    path('course_add/', views.course_add, name='course_add'),
    re_path('course_edit/(\d+)', views.course_edit, name='course_edit'),
    re_path('course_delete/(\d+)', views.course_delete, name='course_delete'),
    # 批量添加学生信息
    path('stu_excel/', views.stu_excel, name='stu_excel'),
    # 搜索
    path('search/', views.search, name='search'),
    # 登录和退出
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout')
]
