# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
# from .models import Student
# from .serializers import StudentSerializer

# from rest_framework import generics, mixins
# from .models import Student
# from .serializers import StudentSerializer

from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer

# #CRUD oprb using GenericAPIView and Mixins
# class StudentListCreateAPI(
#     generics.GenericAPIView,
#     mixins.ListModelMixin,
#     mixins.CreateModelMixin
# ):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     # Read all data
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     # Create data
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
    
# class StudentRetrieveUpdateDeleteAPI(
#     generics.GenericAPIView,
#     mixins.RetrieveModelMixin,
#     mixins.UpdateModelMixin,
#     mixins.DestroyModelMixin
# ):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     #Get single data
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
#     # Update data
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
    
#     # Delete data
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)
    

# #CRUD oprb using APIView
# class StudentAPI(APIView):
#     # Read ALL or single data
#     def get(self, request, pk=None):
#         if pk:
#             try:
#                 student = Student.objects.get(id = pk)
#                 serializer = StudentSerializer(student)
#                 return Response(serializer.data, status=status.HTTP_200_OK)
#             except Student.DoesNotExist:
#                 return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
#         else:
#             # Read all data
#             students = Student.objects.all()
#             serializer = StudentSerializer(students, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
        
# # Create data(POST)
#     def post(self, request):
#         serializer = StudentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     # Update data(PUT)
#     def put(self, request, pk):
#         try:
#             student = Student.objects.get(id=pk)
#         except Student.DoesNotExist:
#             return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)
        
#         serializer = StudentSerializer(student, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     # Delete data(DELETE)
#     def delete(self, request, pk):
#         try:
#             student = Student.objects.get(id=pk)
#             student.delete()
#             return Response(status=status.HTTP_204_NO_CONTENT)
#         except Student.DoesNotExist:
#             return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)

# Full CRUD using ViewSets
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer