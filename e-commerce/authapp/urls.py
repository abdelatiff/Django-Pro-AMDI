from django.urls import path
from .views import edit, dashboard, register, model_form_upload, updateitem, delete_item, contactView, successView, \
    cart_add, item_clear, cart_clear, cart_detail
from django.urls import reverse_lazy
from django.contrib.auth.views import (LoginView, LogoutView, PasswordResetDoneView, PasswordResetView,
                                       PasswordResetCompleteView, PasswordResetConfirmView,
                                       PasswordChangeView, PasswordChangeDoneView,
                                       PasswordResetDoneView)
from django.conf import settings
from django.conf.urls.static import static

app_name = 'authapp'

urlpatterns = [
    path('register/', register, name='register'),
    path('edit/', edit, name='edit'),
    path('dashboard/', dashboard, name='dashboard'),
    path('contact/', contactView, name='contact'),
    path('success/', successView, name='success'),
    path('model_form_upload/', model_form_upload, name='model_form_upload'),
    path('update_item/<str:pk>/', updateitem, name="update_item"),
    path('delete_item/<str:pk>/', delete_item, name="delete_item"),
    path('', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='authapp/logged_out.html'), name='logout'),
    path('cart/add/<int:id>/', cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', item_clear, name='item_clear'),
    path('cart/cart_clear/', cart_clear, name='cart_clear'),
    path('cart/cart-detail/', cart_detail, name='cart_detail'),

]
