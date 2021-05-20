from app1_crud.models import Student, Department
from rest_framework import serializers


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

        # exclude = ['dep_name']


class StudentSerializer(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=3)
    # dept_id = serializers.IntegerField()
    # age = serializers.IntegerField()      for serializers.Serializer

    stu = DepartmentSerializer(many=True, read_only=True)

    class Meta:
        model = Student
        fields = ['id', 'name', 'dept_id', 'age', 'stu']
