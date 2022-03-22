from django.urls import path
from WAS_Practical import views

app_name = "WAS_Practical"

url_patterns = [
    path('/courses', views.courses, name=courses)
]
