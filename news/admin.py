from django.contrib import admin
from .models import Person, Hobby, Cartoon, Play

# Register your models here.
@admin.register(Person)
class Person(admin.ModelAdmin):
    list_display=['name', 'address', 'age']

admin.site.register(Hobby)

@admin.register(Cartoon)
class Cartoon(admin.ModelAdmin):
    list_display=['name', 'dob', 'f_name', 'm_name', 'birth_place', 'p_address', 'telephone', 'mobile', 'email',  'gender', 'martial_status', 'nationality', 'religion']

@admin.register(Play)
class Play(admin.ModelAdmin):
    list_display=['first_name', 'email', 'password', 'contact', 'profile_picture', 'citizenship', 'age', 'gender', 'qualification', 'occupation', 'about_you']