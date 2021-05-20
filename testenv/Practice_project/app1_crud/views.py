from django.shortcuts import render
from django.http import HttpResponse
from app1_crud.models import Student, Department
from app1_crud.serializers import StudentSerializer, DepartmentSerializer
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer


# Create your views here.

def student_view(request):
    print(request)
    if request.method == 'GET':
        # data = request.body
        # stream = io.BytesIO(data)
        # python_data = JSONParser().parse(stream)
        # print("=========================")
        # print(request)
        # print(request.body)
        # print(type(request.body))
        # print("=========================")
        # print(stream, " : is stream and type is :", type(stream))
        # print("=========================")
        # print(python_data, " is python_data and type is : ", type(python_data))
        # print("=========================")
        # if id is not None:

        qs = Student.objects.all()
        serializer = StudentSerializer(qs, many=True)
        json_data = JSONRenderer().render(serializer.data)
        qs1 = Department.objects.all()
        serializer1 = DepartmentSerializer(qs1, many=True)
        json_data1 = JSONRenderer().render(serializer1.data)
        print("=========================")
        print(type(json_data))

    return HttpResponse(json_data, content_type='application/json')
