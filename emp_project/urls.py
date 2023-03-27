from emp_app import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('',views.index),
    path('admin/', admin.site.urls),
    path('home',views.home,name="home"),
    path('office',views.office,name="office"),
    path('employee',views.employee,name="employee"),
    path('offices',views.getAllOffices,name="offices"),
    path('employees',views.getAllEmployee,name="employees"),
    path('pages/office',views.office_page,name="pages/employees"),
    path('pages/employee',views.employee_page,name="pages/employees"),
]
