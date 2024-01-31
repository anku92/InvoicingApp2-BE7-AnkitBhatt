from django.urls import path
from .views import *

urlpatterns = [
    path('invoices/add/', AddInvoice.as_view(), name='new-invoice'),
    path('invoices/', InvoiceList.as_view(), name='all-invoices'),
    path('invoices/<int:id>/items/', AddItems.as_view(), name='add-item'),
    path('invoices/<int:id>/', InvoiceById.as_view(), name='invoice-by-id'),
    path('user/signup/', SignupAPI.as_view(), name='user-signup'),
    path('user/login/', LoginAPI.as_view(), name='user-login'),
    path('users/', UsersList.as_view(), name='users-list'),
]
