from django.urls import path
from .import views

app_name = "api"

urlpatterns = [
    path('invoices/', views.InvoiceListView.as_view(), name='api_invoice_list_create'),
    path('api_upload_csv/', views.InvoiceUploadView.as_view(), name='api_invoice_upload_csv'),
]
