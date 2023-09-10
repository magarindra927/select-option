from django.urls import path, include
from.import views

urlpatterns=[
    path('',views.index),
    path('show',views.show),
    path('send',views.send),
    path('delete', views.delete),
    path('edit', views.edit),
    path('record', views.record),

    path('person', views.person, name='person'),
    path('hobby', views.hobby, name='hobby'),
    path('forms', views.forms, name='forms'),
    path('cv', views.cv, name='cv'),
    path('cv_show', views.cv_show, name='cv_show')
]