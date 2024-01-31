from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status
from .serializers import *
from .models import *
from rest_framework.permissions import IsAuthenticated


class AddInvoice(APIView):
    
    def post(self, request):
        # permission_classes = [IsAuthenticated]
        serialized_invoice = InvoiceSerializer(data=request.data)
        if serialized_invoice.is_valid():
            serialized_invoice.save()
            return Response(serialized_invoice.data, status=status.HTTP_201_CREATED)
        return Response(serialized_invoice.errors, status=status.HTTP_400_BAD_REQUEST)



class InvoiceList(APIView):
    # permission_classes = [IsAuthenticated]
    def get(self, request):
        invoices = Invoice.objects.all()
        serialized = InvoiceSerializer(invoices, many=True).data
        return Response(serialized, status=status.HTTP_200_OK)



class InvoiceById(APIView):

    def get(self, request, id):
        invoice = Invoice.objects.get(invoice_id=id)
        serialized = InvoiceSerializer(invoice).data
        return Response(serialized, status=status.HTTP_200_OK)



class AddItems(APIView):
    def post(self, request, id):
        
        # seeked chatGPT help, thanks to chatGPT
        try:
            invoice = Invoice.objects.get(invoice_id=id)
        except Invoice.DoesNotExist:
            return Response("Invoice not found", status=status.HTTP_404_NOT_FOUND)

        serialized_item = ItemSerializer(data=request.data)
        if serialized_item.is_valid():
            item_instance = serialized_item.save()  # Save the item to the database

            invoice.items.add(item_instance)  # Add the item to the invoice's items
            invoice.save()  # Save the updated invoice

            # Assuming 'items' is a list field in your InvoiceSerializer
            serialized_invoice = InvoiceSerializer(invoice).data
            return Response({'Item added': serialized_item.data}, status=status.HTTP_201_CREATED)



class SignupAPI(APIView):
    def post(self, request):
        serialized = UserSerializer(data=request.data)
        if serialized.is_valid():
            user = serialized.save()
            token = RefreshToken.for_user(user)
            return Response({
                "access": str(token.access_token),
                "refresh": str(token),
            }, status=status.HTTP_201_CREATED)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPI(APIView):
    def post(self, request):
        serialized = LoginSerializer(data=request.data)
        if serialized.is_valid():
            user = serialized.validated_data
            token = RefreshToken.for_user(user)
            return Response({
                "access": str(token.access_token),
                "refresh": str(token),
            }, status=status.HTTP_200_OK)
        return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)



class UsersList(APIView):
    def get(self, request):
        users = User.objects.all()
        serialized = UserSerializer(users, many=True).data
        return Response(serialized, status=status.HTTP_200_OK)