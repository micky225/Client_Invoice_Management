from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Invoice
from .forms import InvoiceForm
from .tasks import process_csv_file

def list_invoice(request):
    invoices = Invoice.objects.all()
    paginator = Paginator(invoices, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'index.html', {"page_obj": page_obj})


def create(request):
    form = InvoiceForm()

    if request.method == "POST":
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('app:list_invoices')
    form = InvoiceForm()
    return render(request, 'create-update-invoice.html', {"form":form})


def update_invoice(request, pk):
    invoice = get_object_or_404(Invoice, pk=pk)
    if request.method == 'POST':
        form = InvoiceForm(request.POST, instance=invoice)
        if form.is_valid():
            form.save()
            return redirect('app:list_invoices')
    else:
        form = InvoiceForm(instance=invoice)
    return render(request, 'create-update-invoice.html', {'form': form})    


def upload_csv(request):
    if request.method == 'POST':
        csv_file = request.FILES['file']
        process_csv_file.delay(csv_file.read().decode('utf-8'))
        return redirect('app:list_invoices')    
    return render(request, 'upload_csv.html')