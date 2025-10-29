from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status

@api_view(['GET'])
def get_students(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_student(request):
    serializer = StudentSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'PATCH'])
def update_student(request, pk):
    try:
        student= Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return Response({"error":"Student not found"},status=status.HTTP_404_NOT_FOUND)
    
    #Partial update support
    if request.method == 'PATCH':
        serializer = StudentSerializer(student, data=request.data, partial=True)
    else:
        serializer = StudentSerializer(student, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def delete_student(request, pk):
    try:
        student= Student.objects.get(id=pk)
    except Student.DoesNotExist:
        return Response({"error":"Student not found"},status=status.HTTP_404_NOT_FOUND)

    student.delete()
    return Response({"message":"Student deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
