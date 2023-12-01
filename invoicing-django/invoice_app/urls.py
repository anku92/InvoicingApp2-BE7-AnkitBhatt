from django.urls import path
from .views import (
    UserSignup,
    UsersView,
    UserLogin,
    InvoiceList,
    SingleInvoice,
    AddInvoice,
    AddItem,
)


urlpatterns = [
    path("users/", UsersView.as_view(), name="all-users"),
    path("user/signup/", UserSignup.as_view(), name="register"),
    path("user/login/", UserLogin.as_view(), name="login"),
    path("invoices/", InvoiceList.as_view(), name="invoice-list"),
    path("invoices/<int:invoice_id>/", SingleInvoice.as_view(), name="single-invoice"),
    path("invoices/add/", AddInvoice.as_view(), name="add-invoice"),
    path("invoices/<int:invoice_id>/items/", AddItem.as_view(), name="edit-invoice"),
]
