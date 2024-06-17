from django.urls import path
from .import views
from .import api_views

app_name = "app"

urlpatterns = [
    path('', views.list_invoice,name="list_invoices"),
    path('create/', views.create,name="create"),
    path('update/<int:pk>/', views.update_invoice, name='update_invoice'),
    path('upload_csv/', views.upload_csv, name='upload_csv'),
    path('api/invoices/', api_views.InvoiceListView.as_view(), name='api_invoice_list_create'),
    path('api/invoices/upload_csv/', api_views.InvoiceUploadView.as_view(), name='api_invoice_upload_csv'),
]
