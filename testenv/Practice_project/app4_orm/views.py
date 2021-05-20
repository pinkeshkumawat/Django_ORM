from django.db.models import Q, Subquery
from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Department, Seat


# Create your views here.


def filter_query(request):
    qs = Student.objects.all()
    ''' for printing SQL query of ORM model'''
    print("query for all students is \n",qs.query)
    #print(str(qs.query))

    print("======for getting the dictionary from queryset =========")

    qs12 = Student.objects.all().values('name', 'age')
    print(qs12)

    qs2 = Student.objects.get(id=2)  # get single record/object from query set (row)
    print("name of the student with id 2 is :", qs2.name)                  # get single field from qs (column value)

    ''' OR operation , 2 ways'''
    print("============ OR operation ====================")
    qs3 = Student.objects.filter(name__startswith='P') | Student.objects.filter(name__startswith='N')
    print(qs3)
    print("students whose name starts with P or N are :")
    for obj in qs3:   # using for loop becoz getting multiple records
        print(obj.name)
    qs4 = Student.objects.filter(Q(name__startswith='P') | Q(name__startswith='J'))
    print(qs4)

    ''' AND operation , 3 ways'''
    print("============ AND operation ====================")
    qs5 = Student.objects.filter(name__startswith='P', name__endswith='h')
    print(qs5)
    qs6 = Student.objects.filter(name__startswith='n') & Student.objects.filter(name__endswith='a')
    print(qs6)
    qs7 = Student.objects.filter(Q(name__startswith='P') & Q(name__endswith='a'))
    print(qs7)

    ''' NOT operation , 2 ways'''
    print("============ NOT operation ====================")
    qs8 = Student.objects.exclude(age__lt=30)  # less than
    print(qs8)
    qs9 = Student.objects.filter(~Q(age__gte=24)) # greater than equal to
    print(qs9)

    ''' UNION operation '''
    print("============ UNION operation on querysets ====================")
    print(qs8.union(qs9))

    print("============ UNION operation on Models with same field ====================")
    qs10 = Student.objects.values_list('name').union(Department.objects.values_list('name'))
    print(qs10) # only union two models if they have same fields, and using values_list you can only filter fields

    qs11 = Student.objects.filter(name__startswith='n').values('name', 'age')
    print(qs11)

    print("============ SUB-Query ====================")
    # display names of student whose age is greater than age of pinkesh
    qs13 = Student.objects.filter(name='Pinkesh').values('age') # will fetch age of st where name = pinkesh
    print(qs13)
    qs14 = Student.objects.filter(age__gt=Subquery(Student.objects.filter(name='Pinkesh').values('age')))
    print(qs14)

    return HttpResponse("<h1>Check console</h1> ")
