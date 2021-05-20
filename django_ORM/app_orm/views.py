from django.db import connection
from django.db.models import Q, Subquery, F, Count, Avg, Min, Max, Sum
from django.db.models.functions import Substr, Lower
from django.shortcuts import render
from django.http import HttpResponse
from .models import Student, Department, Seat, Details,OnlyOneObjectcanBeCreated
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets
from django.views.decorators.http import require_http_methods
# Create your views here.

'''Sources : https://books.agiliq.com/projects/django-orm-cookbook/en/latest/join.html
    https://swapps.com/blog/quick-start-with-django-orm/
    https://docs.djangoproject.com/en/3.2/ref/models/querysets/ '''


def create_data(request):
    print("============ To create record using ORM query ====================")
    '''  # don't run it again and again it will keep on creating objects/record '''
    # qs15 = Student.objects.create(name='Chandler', dept_id='6', age='52')
    # print(qs15.name)
    # print(qs15.query)

    # qs16 = Department.objects.create(dep_id=Student.objects.get(id=4), name="D5")
    # because of foreign key the instance of student is passed to select the dep_id from student table
    # print(qs16.name)

    '''We can also save data in model like this'''
    # st = Student()
    # st.name = "Rosita"
    # st.age = 27
    # st.dept_id = 11
    # st.save()

    # print("============ Bulk record creation ====================")
    # list_items = [Student(name='Raju', age=23, dept_id=10),    # list of objects
    #               Student(name='Raju', age=23, dept_id=10),
    #               Student(name='Raju', age=23, dept_id=10)]
    # qs = Student.objects.bulk_create(list_items)
    # print(qs)

    # print("============ Bulk record creation ====================")
    # no_of_students = Student.objects.all().count()  # this will count all objects and Count('name) is used with annotate check below
    # print(no_of_students)
    # obj = Student.objects.first()
    # obj.pk=None # pk is none coz every field other than primary key is saved
    # obj.save()                          # To save the object to database
    # no_of_students = Student.objects.all().count()
    # print(no_of_students)

    print("============ upadate string to date ====================")
    qs2 = OnlyOneObjectcanBeCreated.objects.create(name='Obj1',date='2021-03-04') # if this doesn't work use string to date parsing
    print(qs2)

    return HttpResponse("<h1>created Check console</h1> ")


def update_data(request):
    print("============ To UPDATE record using ORM query ====================")
    qs = Student.objects.first()
    print("Currently the age is :", qs.age)  # on running again it will already be 25

    qs.age = 25  # 1st way
    qs.save()  # save is required to save the changes in DB if record is not saved wit save() method then,
    # qs.refresh_from_db()
    print("Updated age is: ", qs.age)

    # second way of updation
    qs2 = Student.objects.filter(name="Pinkesh").update(age=24)  # it returns number of records updated
    print("number of records updated are :", qs2)

    qs3 = Student.objects.get(id=1)
    print(qs3.age)

    return HttpResponse("<h1>Updated Check console</h1> ")


def field_lookup(request):
    qs = Student.objects.get(name__iexact="piNkeSh")  # case insensitive match
    print(qs)
    qs2 = Student.objects.get(name__contains="eh")  # similar to SELECT ... WHERE name LIKE '%eH%'; case sensitive
    print(qs2)
    qs3 = Student.objects.get(name__icontains="Eh")  # similar to SELECT ... WHERE name LIKE '%eH%'; case insensitive
    print(qs3)
    qs4 = Student.objects.filter(id__in=[1, 8, 9])
    # use in keyword with  list, tuple, or queryset. It’s not a common use case, but strings (being iterables) are accepte
    print(qs4)
    qs5 = Student.objects.filter(id__in=qs4)
    print(qs5)

    return HttpResponse("<h1>Field lookups Check console</h1> ")


def filter_query(request):
    qs = Student.objects.all()
    ''' for printing SQL query of ORM model'''
    print("query for all students is \n", qs.query)
    # print(str(qs.query))

    print("======for getting the dictionary from queryset(Values) =========")

    qs11 = Student.objects.all().values('name','age')  # it will show key value pair of field and values in list of dictionaries
    print(qs11)

    qs12 = Student.objects.filter(name__startswith='n').values('name', 'age')
    print(qs12)

    print("======Values list =========")
    qs1 = Student.objects.values_list('name', 'age')  # it will show only values of field
    print(qs1)

    print("======Value list of single attribute without flat =========")
    qset = Student.objects.values_list('name')  # it will show list of tuples with ,
    print(qset)
    print("======Value list of single attribute with flat=true =========")
    qset1 = Student.objects.values_list('name', flat=True)  # it will show list of content that can be used anywhere(valid for single attribute only)
    print(qset1)

    qs2 = Student.objects.get(id=2)  # get single record/object from query set (row)
    # qs2 = Student.objects.get(name='Pinkesh')
    print("name of the student with id 2 is :", qs2.name)  # get single field from qs (column value)

    ''' OR operation , 2 ways'''
    print("============ OR operation ====================")
    qs3 = Student.objects.filter(name__startswith='P') | Student.objects.filter(name__startswith='N')
    print(qs3)
    print("students whose name starts with P or N are :")
    for obj in qs3:  # using for loop becoz getting multiple records
        print(obj.name)
    qs4 = Student.objects.filter(Q(name__startswith='P') | ~Q(name__istartswith='J')) # start with p but not starts with j
    # startswith is case sensitive and istartswith is case insensitive
    print(qs4)

    ''' == We can also use range, date, year, iso_year, months, day, week, weekday, iso_weekday, isnull, regex etc'''

    ''' AND operation , 3 ways'''
    print("============ AND operation ====================")
    qs5 = Student.objects.filter(name__startswith='P', name__iendswith='h')  # iendswith is case insesnsitive
    print(qs5)
    qs6 = Student.objects.filter(name__startswith='n') & Student.objects.filter(name__endswith='a')
    print(qs6)
    qs7 = Student.objects.filter(Q(name__startswith='P') & Q(name__endswith='a'))
    print(qs7)

    ''' NOT operation , 2 ways'''
    print("============ NOT operation ====================")
    qs8 = Student.objects.exclude(age__lt=30)  # less than
    print(qs8)
    qs9 = Student.objects.filter(~Q(age__gte=24))  # greater than equal to
    print(qs9)

    ''' UNION operation '''
    print("============ UNION operation on querysets ====================")
    print(qs8.union(qs9))

    print("============ UNION operation on Models with same field ====================")
    qs10 = Student.objects.values_list('name').union(Department.objects.values_list('name'))
    print(qs10)  # only union two models if they have same fields, and using values_list you can only filter fields

    print("============ SUB-Query ====================")
    # display names of student whose age is greater than age of pinkesh
    qs13 = Student.objects.filter(name='Pinkesh').values('age')  # will fetch age of st where name = pinkesh
    print(qs13)
    qs14 = Student.objects.filter(age__gt=Subquery(Student.objects.filter(name='Pinkesh').values('age')))
    print(qs14)

    ''' Use F object to compare two fields '''
    print("============ Filter by comparing fields using F object ====================")
    # filter the fields where age = dept_id
    qs17 = Student.objects.filter(age=F("dept_id"))
    print(qs17)
    ''' used with foreign key name in student(dep_id__name) is equal to name in dept F("name")'''
    qss = Department.objects.filter(dep_id__name=F("name"))
    print("===",qss)

    print("============ Filter by comparing fields using annotate, F object and Substr ====================")
    # filter value where first 2 char of first and last name are similar
    qs18 = Details.objects.annotate(fname=Substr("f_name", 1, 2), lname=Substr("l_name", 1, 2)).filter(fname=F("lname"))
    # annotate is use to give alt name
    # Substr is used to take sub string starting from 1 and till 2 char like Substr("pinkesh",1,3) is pin
    print(qs18)

    print("============ Select Student with maximum age ====================")
    qs19 = Student.objects.order_by('age')[2]   # second lowest age
    print(qs19.age)
    qs20 = Student.objects.order_by('age')[Student.objects.all().count()-2] # second highest age
    print(qs20.age)

    print("============ Find student with duplicate name ====================")
    qs21 = Student.objects.values('name').annotate(count=Count('name'))
    print(qs21)

    qs22 = Student.objects.values('name').annotate(count= Count('name')).filter(count__gt=1)
    print(qs22,"\n",qs22[0]['name'])

    print("============ Find student with distinct name ====================")
    qs23 = Student.objects.values('name').annotate(count=Count('name')).filter(count=1)
    print(qs23, "\n", qs23[0]['name'])

    print(i['name'] for i in qs23)
    '''similar to this below'''
    # for i in qs23:
    #     print(i['name'])

    print("============ Select random object efficiently ====================")
    qs24 = Student.objects.all().aggregate(max_id=Max('id')) # return {'max_id': 11}
    print(qs24)
    max = Student.objects.all().aggregate(max_id=Max('id'))['max_id'] # return 11
    # import random
    # ran = random.randint(1,max)
    # qs25 = Student.objects.get(id=ran)
    # print(qs25)

    return HttpResponse("<h1>Check console</h1> ")


def joins(request): # it's a inner join basially
    print("===========JOIN is ====================")
    # only work with related fields i.e foreign key or OneToOneField etc
    qs = Department.objects.select_related("dep_id")
    print(qs)
    qs2 = Seat.objects.select_related("student")
    print(qs2.query)

    qs3 = Seat.objects.filter(student__name='Pinkesh')  # student is name of key in seat, name is the key in student table where name =pinkesh
    print(qs3)
    print(qs3.quer)

    return HttpResponse("<h1>Joins done Check console</h1>")


def group_functions(request):
    avg = Student.objects.all().aggregate(Avg('age'))
    print(avg, type(avg))
    min = Student.objects.all().aggregate(Min('age'))
    print(min)
    max = Student.objects.all().aggregate(Max('age'))
    print(max)
    sum = Student.objects.all().aggregate(Sum('age'))
    print(sum)

    return HttpResponse("<h1>Group functions done Check console</h1>")


def delete(request):
    print("==============Deletion===================")
    qs = OnlyOneObjectcanBeCreated.objects.count()
    print(f'total number of objects are {qs}')
    qs1 = OnlyOneObjectcanBeCreated.objects.all().delete()
    print(qs1)

    print("hi====",connection.cursor())

    return HttpResponse("<h1>Deleted table data Check console</h1>")


def ordering(request):
    print("\n==============Ascending order (case sensitive)===================")
    qs = Student.objects.all().order_by('name')   # frst  all upper case then all lowercase ordering case sensetive
    print(qs)
    print("\n==============Ascending order (case Insensitive) ===================")
    qs = Student.objects.all().order_by(Lower('name')).values_list('name') # check 1st upper case the lowe case for both alphabetically
    print(qs)
    print("\n==============descending order===================")
    qs1 = Student.objects.all().order_by('-name')
    print(qs1)
    print("\n==============Order by multiple columns===================")
    qs2 = Student.objects.all().order_by('name','-age')  # will order first by name in asc and age in desc
    print(qs2)
    print("\n==============Foreign key order===================")
    qs3 = Department.objects.all().order_by('dep_id__name')  # name of fireign key and name of field of the re;lated table acc toi which sorting is done
    print(qs3)
    print("\n==============Orderinga cc to annotated field===================")
    qs4 = Student.objects.values_list('name').annotate(count=Count('name')) #
    print(qs4)

    return HttpResponse("<h1>Ordering done data Check console</h1>")