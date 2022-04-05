from django.urls import path
from .views import edit, dashboard, register, model_form_upload, updateitem, delete_item, contactView, successView, \
    cart_add, item_clear, item_increment, item_decrement, cart_clear, cart_detail
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
    path('password_change/', PasswordChangeView.as_view(
        template_name='authapp/password_change_form.html'), name='password_change'),
    path('password_change/dond/', PasswordChangeDoneView.as_view(template_name='authapp/password_change_done.html'),
         name='password_change_done'),
    path('password_reset/', PasswordResetView.as_view(
        template_name='authapp/password_reset_form.html',
        email_template_name='authapp/password_reset_email.html',
        success_url=reverse_lazy('authapp:password_reset_done')), name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(
        template_name='authapp/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='authapp/password_reset_confirm.html',
        success_url=reverse_lazy('authapp:login')), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(
        template_name='authapp/password_reset_complete.html'), name='password_reset_complete'),

    path('cart/add/<int:id>/', cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         item_decrement, name='item_decrement'),
    path('cart/cart_clear/', cart_clear, name='cart_clear'),
    path('cart/cart-detail/', cart_detail, name='cart_detail'),

]
