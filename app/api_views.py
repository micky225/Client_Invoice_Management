from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.views import APIView
from .models import Invoice
from .serializers import InvoiceSerializer
from .tasks import process_csv_file

class InvoiceListView(generics.ListAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer


class InvoiceUploadView(APIView):
    parser_classes = [MultiPartParser, FormParser]

    def post(self, request, *args, **kwargs):
        if 'file' not in request.FILES:
            return Response({"error": "No file provided"}, status=status.HTTP_400_BAD_REQUEST)
        
        csv_file = request.FILES['file']
        process_csv_file.delay(csv_file.read().decode('utf-8'))
        return Response(status=status.HTTP_202_ACCEPTED)