from django.shortcuts import render
from WAS_Practical.models import Course


def courses(request):
    allCourses = Course.objects.all()
    context_dict = {}
    context_dict['courseList'] = allCourses
    return render(request, 'courses.html', context=context_dict)
