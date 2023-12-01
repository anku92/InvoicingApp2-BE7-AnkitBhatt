from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserSerializer, InvoiceSerializer, ItemSerializer
from .data import invoices_data, users_data
from rest_framework.response import Response
import json
import jwt


# GET - VIEW ALL INVOICES
class InvoiceList(APIView):
    def get(self, request):
        serialized = InvoiceSerializer(invoices_data, many=True).data
        return Response(serialized, status=200)


# POST - CREATE NEW INVOICE
class AddInvoice(APIView):
    def post(self, request):
        bodyData = json.loads(request.body)
        bodyData["invoice_id"] = len(invoices_data) + 1
        serialized = InvoiceSerializer(data=bodyData)

        if serialized.is_valid():
            invoices_data.append(serialized.data)
            return Response({"invoice added": str(serialized.data)}, status=201)
        return Response({"message": "bad request"}, status=400)


# GET - VIEW A SPECIFIC INVOICE
class SingleInvoice(APIView):
    def get(self, request, invoice_id):
        for invoice in invoices_data:
            if invoice["invoice_id"] == invoice_id:
                serialized = InvoiceSerializer(invoice).data
                return Response(serialized, status=200)
        return Response({"message": "Invoice doesn't exist"}, status=404)



# ADD ITEM API:
class AddItem(APIView):
    def post(self, request, invoice_id):
        for invoice in invoices_data:
            if invoice["invoice_id"] == invoice_id:
                bodyData = request.data
                serialized = ItemSerializer(data = bodyData)
                if serialized.is_valid():
                    invoice["items"].append(serialized.data)
                    return Response({"Items Added": str(serialized.data)}, status=201)
                return Response(serialized.errors, status=400)
        return Response("Invoice not found", status=404)




# GET - VIEW ALL USERS
class UsersView(APIView):
    def get(self, request):
        serialized = UserSerializer(users_data, many=True).data
        return Response(serialized, status=200)


# POST - SIGNUP
class UserSignup(APIView):
    def post(self, request):
        bodyData = request.data
        for data in users_data:
            if data["username"] == bodyData["username"]:
                return Response({"Message": "username already exists"}, status=409)
            elif data["email"] == bodyData["email"]:
                return Response({"Message": "Email already exists"}, status=409)

        bodyData["user_id"] = len(users_data) + 1
        serialized = UserSerializer(data=bodyData)

        if serialized.is_valid():
            users_data.append(serialized.data)
            return Response({"User Added": str(serialized.data)}, status=201)
        return Response(serialized.errors, status=400)

        
# POST - LOGIN
class UserLogin(APIView):
    def post(self, request):
        bodyData = request.data
        for user in users_data:
            if (
                user["username"] == bodyData["username"]
                and user["password"] == bodyData["password"]
            ):
                token = jwt.encode(
                    {"user_id": user["user_id"], "username": user["username"]},
                    "secret",
                    algorithm="HS256",
                )
                return Response({"token": token}, status=200)
        return Response({"Error": "Login Failed"}, status=401)
