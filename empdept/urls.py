from django.urls import path
from . import views

urlpatterns=[
    path('createdept',views.create_dept,name='createdept'),
    path('createemp',views.create_emp,name='createemp'),
    path('emp',views.list_emp,name='emp'),
    path('updateemp/<int:id>',views.update_emp,name='updateemp'),
    path('deleteemp/<int:id>',views.delete_emp,name='deleteemp'),
    path('details/<int:id>',views.detail,name='detail'),
    path('dept',views.list_dept,name='dept'),
    path('updatedept/<int:id>',views.update_dept,name='updatedept'),
    path('detaildept/<int:id>',views.detail_dept,name='detail_dept')

]