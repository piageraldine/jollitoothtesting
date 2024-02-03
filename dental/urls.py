from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.sign_in, name="login"),
    path('register/', views.sign_up, name="register"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('set-appointment/', views.set_appointment, name="set-appointment"),
    path('logout/', views.sign_out, name="logout"),
    path('service/', include([
       path('index/', views.service_list, name="service_index"),
       path('create/', views.service_create, name="service_create"),
       path('show/<int:serviceID>', views.service_show, name="service_show"),
       path('delete/<int:serviceID>', views.service_destroy, name="service_delete")
    ])),
    path('appointments', include([
        path('', views.appointment_index, name="appointment_index"),
        path('show/<int:appointmentID>', views.appointment_show, name="appointment_show"),
        path('edit/<int:appointmentID>', views.appointment_edit, name="appointment_edit"),
        path('delete/<int:appointmentID>', views.appointment_delete, name="appointment_delete")
    ]))
]
