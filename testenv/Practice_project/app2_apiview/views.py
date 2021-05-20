from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Student,Department
from .serializers import StudentSerializer,DepartmentSerializer
from rest_framework.response import Response

# Create your views here.


@api_view(['GET','POST'])
def student_api(request):
    if request.method == 'GET':
        print(request)
        print(request.data)
        id = request.data.get('id')
        print(id)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        stu = Student.objects.all()
        str(stu.query)
        print(stu.query)
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        data = request.data
        print(data)
        serializer = StudentSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Posted'})
    return Response({'msg': 'Not Posted'})
