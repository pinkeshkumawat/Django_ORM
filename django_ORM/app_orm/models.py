from django.db import models, connection


# Create your models here.

'''
TO CONVERT ANY EXISTING DATABASE TO MODELS FILE RUN COMMAND:
Before running this you will have to configure your database in the settings.py file
"Python manage.py inspectdb to chk db 
"python manage.py inspectdb > file_name.py" To store in file_name.py

'''


class Student(models.Model):
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # it will make id as '3cd2b4b0c36f43488a93b3bb72029f46' instead of 1
    name = models.CharField(max_length=30, null=False, blank=False)
    dept_id = models.IntegerField()
    age = models.IntegerField()

    def __str__(self):  # it will show the name of every object/record in admin panel, instead of Student.object(0)
        return self.name

    # class Meta:
    #     abstract = True  # it can be inherited
    #     db_table = 'student'  # name changed in DB table
    #     ordering = ['-name', 'age']
    #     # constaints = models.constraints(age__gt=0, age__lte=100)
    #     get_latest_by = ''   # by default date, it shows latest by time


class Department(models.Model):
    dep_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = "department"
        verbose_name_plural = "Depts"   # name of table on admin panel

    def __str__(self):  # name of object on admin panel
        return self.name


class Seat(models.Model):
    student = models.OneToOneField(Student,on_delete=models.CASCADE)
    seat_name = models.CharField(max_length=20)

    def __str__(self):
        return self.seat_name

    @classmethod
    def truncate(cls): # to delete whole table at once bu calling Seat.truncate() method
        with connection.cursor() as cursor:
            cursor.execute('TRUNCATE TABLE "{0}" CASCADE'.format(cls._meta.db_table))


class Details(models.Model):
    f_name = models.CharField(max_length=30, null=False, blank=False)
    l_name = models.CharField(max_length=30, null=False, blank=False)

    def __str__(self):
        return self.f_name


class OnlyOneObjectcanBeCreated(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateField(null=True)

    '''this will only let this model create 1 object after that it will throw an Integirty error
        and it will keep on deleting the previous objects and kept on storing the single object'''
    def save(self, *args, **kwargs):

        if self.__class__.objects.count():
            self.pk = self.__class__.objects.first().pk
        super().save(*args, **kwargs)


class SelfRefForeignKey(models.Model):
    name = models.ForeignKey('self', on_delete=models.CASCADE, default=None)
    number = models.IntegerField
    greet = models.CharField(max_length=20,default= None)

    def __str__(self):
        return self.name
