# from django.http import JsonResponse
# from django.http import JsonResponse
# from django.shortcuts import render
# from .models import Category, Course
# Create your views here.
# def index(request):
#     categories = Category.objects.all()
#     data = categories.values()
#     return JsonResponse(list(data), safe=False)


from rest_framework import viewsets, status
from rest_framework.decorators import action
from django.http import HttpResponse

from .models import Course
from .serializers import CourseSerializaer
from rest_framework.response import Response


class CoursesViewSet(viewsets.ViewSet):
    # @action()
    def list(self, request):
        courses = Course.objects.all()
        serializers = CourseSerializaer(courses, many=True)
        return Response(serializers.data)
    def create(self, request):
        serializer = CourseSerializaer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    def retrieve(self, request, pk=None):#/courses/<str:id>
        course = Course.objects.get(pk=pk)
        serializer = CourseSerializaer(course)
        return Response(serializer.data)

    def update(self, request, pk=None):#/courses/<str:id>
        course = Course.objects.get(id=pk)
        
        serializer = CourseSerializaer(instance=course, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status = status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):#/courses/<str:id>
        course = Course.objects.get(id=pk)
        course.delete()
        return Response("delete success")

