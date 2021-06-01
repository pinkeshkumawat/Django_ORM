from django.contrib import admin
from .models import Student,Department,Seat,Details,OnlyOneObjectcanBeCreated,SelfRefForeignKey
# Register your models here.
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Seat)
admin.site.register(Details)
admin.site.register(OnlyOneObjectcanBeCreated)
admin.site.register(SelfRefForeignKey)
