from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response

@api_view(['GET'])
def student_list(request):
    Students = Student.objects.all()
    serializer = StudentSerializer(Students, many=True)
    return Response(serializer.data)
