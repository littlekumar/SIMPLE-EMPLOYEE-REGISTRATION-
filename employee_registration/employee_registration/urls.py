"""employee_registration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from app import views
from employee_registration import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.showindex, name='home'),
    path('', views.showindex, name='manager'),
    # path('', views.showindex, name='employee'),
    # path('myadmin/', views.ShowAdmin.as_view(template_name="Admin_registration.html"), name='myadmin'),
    path('employee_registration/', views.employee_Registration.as_view(template_name="employee_myprofile_head.html"), name='employee'),
    path('manager_login/', views.Manager_Login_page.as_view(template_name="Manager_Login.html"), name='manager_login'),
    # path('employee_login_page/', views.employee_Login.as_view(template_name="Employee_Login.html"), name='employee_login_page'),
     path('manager_validation/', views.manager_validation, name='manager_validation'),
    path('store_user/', views.store_user, name='store_user'),
    # path('user_login/', views.employee_login, name='employee_login'),
    path('employee_data_selection/',views.employee_data_selection,name="employee_data_selection"),
    # path('qualification/',views.qualificatiom,name="qualification"),
    path('employee_edu/', views.employee_edu, name='employee_edu'),
    path('personalinformation/',views.personalinformation,name="personalinformation"),
    path('work_experience/',views.Work_experience.as_view(template_name="employee_work_experience.html"),name="work_experience"),
    path('personal_information/',views.Personal_information.as_view(template_name="employee_myprofile_head.html"),name="personal_information"),
    path('button_validation/',views.button_validation,name="button_validation"),
    path('idno/',views.idno,name="idno"),
    path('search/',views.search,name="search"),
    path('seemore/',views.seemore,name="seemore")
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)