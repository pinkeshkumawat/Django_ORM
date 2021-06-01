# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

'''
TO CONVERT ANY EXISTING DATABASE TO MODELS FILE RUN COMMAND:
Before running this you will have to configure your database in the settings.py file
"python manage.py inspectdb > file_name.py" 

'''
class App1CrudDepartment(models.Model):
    dep_name = models.CharField(max_length=20)
    dep_id = models.ForeignKey('App1CrudStudent', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app1_crud_department'


class App1CrudStudent(models.Model):
    name = models.CharField(max_length=30)
    dept_id = models.IntegerField()
    age = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'app1_crud_student'


class App2ApiviewDepartment(models.Model):
    dep_name = models.CharField(max_length=20)
    dep_id = models.ForeignKey('App2ApiviewStudent', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app2_apiview_department'


class App2ApiviewStudent(models.Model):
    name = models.CharField(max_length=30)
    dept_id = models.IntegerField()
    age = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'app2_apiview_student'


class App3OnetoonePage(models.Model):
    user = models.OneToOneField('AuthUser', models.DO_NOTHING, primary_key=True)
    page_name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'app3_onetoone_page'


class App4OrmDepartment(models.Model):
    dep_id = models.ForeignKey('App4OrmStudent', models.DO_NOTHING)
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'app4_orm_department'


class App4OrmSeat(models.Model):
    seat_named = models.CharField(max_length=20)
    student = models.OneToOneField('App4OrmStudent', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app4_orm_seat'


class App4OrmStudent(models.Model):
    name = models.CharField(max_length=30)
    dept_id = models.IntegerField()
    age = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'app4_orm_student'


class AppOrmDepartment(models.Model):
    name = models.CharField(max_length=20)
    dep_id = models.ForeignKey('AppOrmStudent', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app_orm_department'


class AppOrmDetails(models.Model):
    f_name = models.CharField(max_length=30)
    l_name = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'app_orm_details'


class AppOrmOnlyoneobjectcanbecreated(models.Model):
    name = models.CharField(max_length=30)
    date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'app_orm_onlyoneobjectcanbecreated'


class AppOrmSeat(models.Model):
    student = models.OneToOneField('AppOrmStudent', models.DO_NOTHING)
    seat_name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'app_orm_seat'


class AppOrmSelfrefforeignkey(models.Model):
    greet = models.CharField(max_length=20)
    name = models.ForeignKey('self', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app_orm_selfrefforeignkey'


class AppOrmStudent(models.Model):
    name = models.CharField(max_length=30)
    dept_id = models.IntegerField()
    age = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'app_orm_student'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_flag = models.PositiveSmallIntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

