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
def dashboard(request):                                                         # Dashboard view
    query_results = GraphiCards.objects.all()                                   # Getting all the information from database
    context = {'query_results': query_results}                                  # Creating a dictionary to pass as an argument
    return render(request, 'authapp/dashboard.html', context=context)           # render the home page url




@permission_required('authapp.add_item', raise_exception=True)                  # Permission docerator 'admin' for uploading new product
@login_required                                                                 # Login requirment to upload new product
def model_form_upload(request):                                                 # Adding product view
    if request.method == 'POST':                                                # Check if a request method is Post
        form = GraphicForm(request.POST, request.FILES)                         # Parse the Post request to the product form as well as the files uploaded
        if form.is_valid():                                                     # check if the form is valid
            form.save()                                                         # save the information in the form
    else:
        form = GraphicForm()
    return render(request, 'authapp/model_form_upload.html', {                  # render the upload html page to upload your product
        'form': form
    })


@permission_required('authapp.update_item', raise_exception=True)                # Permission docerator 'admin' for modyfing a product
@login_required                                                                  # Login requirment to update a product
def updateitem(request, pk):                                                     # Product modyfing view
    graphiCards = GraphiCards.objects.get(id=pk)                                 # Get all the information from the product model with primary key
    form = GraphicForm(instance=graphiCards)                                     # Get the form of the product

    if request.method == 'POST':                                                 # Check if the post condition
        form = GraphicForm(request.POST, request.FILES, instance=graphiCards)    # Parse a post request, files to product form with product's instance
        if form.is_valid():                                                      # check if the form is valid
            form.save()                                                          # save the form
            next_ = request.POST.get('next', '/')
            return HttpResponseRedirect(next_)

    context = {'orders': form}                                                   # Creating a dictionary to pass as an argument
    print(form)
    return render(request, 'authapp/update_item.html', context)


@permission_required('authapp.delete_item', raise_exception=True)                 # Permission docerator 'admin' for deleting a product
@login_required                                                                   # Login requirment to delete a product
def delete_item(request, pk):                                                     # delete product from home page view
    order = GraphiCards.objects.get(id=pk)                                        # Get all the information from the product model with primary key
    if request.method == "POST":                                                  # Check if request method is post
        order.delete()                                                            # delete the product
        return redirect('/dashboard/')                                            # return to home page
    context = {'item': order}                                                     # Creating a dictionary to pass as an argument
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
def cart_clear(request):                                                        # clear cart view
    cart = Cart(request)                                                        # Parse request to the cart model
    print("---------herree-------------")
    print(cart.cart)
    cart.clear()                                                                 # remove products from the cart
    return render(request, 'authapp/cart.html')                                  # render the cart details


@login_required
def cart_detail(request):                                                         # cart detail's view
    return render(request, 'authapp/cart.html')                                   # Render the cart details


