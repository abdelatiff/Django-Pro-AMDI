import os
from datetime import datetime

from django.core.mail import send_mail
from django.http import request, HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required,permission_required
from .forms import UserRegistration, UserEditForm, GraphicForm, ContactForm
from .models import GraphiCards
from django.core.mail import send_mail, BadHeaderError
from cart.cart import Cart
import json
# Create your views here.

@login_required
def dashboard(request):
    # Getting all the stuff from database
    query_results = GraphiCards.objects.all()
    # Creating a dictionary to pass as an argument
    context = {'query_results': query_results}
    return render(request, 'authapp/dashboard.html', context=context)




@permission_required('authapp.add_item', raise_exception=True)
@login_required
def model_form_upload(request):
    if request.method == 'POST':
        form = GraphicForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = GraphicForm()
    return render(request, 'authapp/model_form_upload.html', {
        'form': form
    })


@permission_required('authapp.update_item', raise_exception=True)
@login_required
def updateitem(request, pk):
    graphiCards = GraphiCards.objects.get(id=pk)
    form = GraphicForm(instance=graphiCards)

    if request.method == 'POST':
        form = GraphicForm(request.POST, request.FILES, instance=graphiCards)
        if form.is_valid():
            form.save()
            next_ = request.POST.get('next', '/')
            return HttpResponseRedirect(next_)

    context = {'orders': form}
    print(form)
    return render(request, 'authapp/update_item.html', context)


@permission_required('authapp.delete_item', raise_exception=True)
@login_required
def delete_item(request, pk):
    order = GraphiCards.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/dashboard/')
    context = {'item': order}
    return render(request, 'authapp/delete_item.html', context)


def register(request):
    if request.method == 'POST':
        form = UserRegistration(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(
                form.cleaned_data.get('password')
            )
            new_user.save()
            return render(request, 'authapp/register_done.html')
    else:
        form = UserRegistration()

    context = {
        "form": form
    }

    return render(request, 'authapp/register.html', context=context)


@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user,
                                 data=request.POST)
        if user_form.is_valid():
            user_form.save()
    else:
        user_form = UserEditForm(instance=request.user)
    context = {
        'form': user_form,
    }
    return render(request, 'authapp/model_form_upload.html', context=context)



def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['abdelatifchairids@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
    return render(request, "authapp/contact.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')


@login_required
def cart_add(request, id):
    cart = Cart(request)
    product = GraphiCards.objects.get(id=id)
    product.Quantity = product.Quantity - 1
    product.save()
    cart.add(product=product)
    return redirect('/dashboard/')


@login_required
def item_clear(request, id):
    cart = Cart(request)
    product = GraphiCards.objects.get(id=id)
    cart.remove(product)
    product.Quantity = product.Quantity +1
    product.save()
    return render(request, 'authapp/cart.html')


@login_required
def item_increment(request, id):
    cart = Cart(request)
    product = GraphiCards.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required
def item_decrement(request, id):
    cart = Cart(request)
    product = GraphiCards.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("/")


@login_required
def cart_clear(request):
    cart = Cart(request)
    print("---------herree-------------")
    print(cart.cart)
    cart.clear()
    return render(request, 'authapp/cart.html')


@login_required
def cart_detail(request):
    return render(request, 'authapp/cart.html')


