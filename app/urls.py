from django.urls import path
from .import views

app_name = "app"

urlpatterns = [
    path('', views.list_invoice,name="list_invoices"),
    path('create/', views.create,name="create"),
    path('update/<int:pk>/', views.update_invoice, name='update_invoice'),
    path('upload_csv/', views.upload_csv, name='upload_csv'),
]
