from .forms import RegistrationForm, LoginForm
from cart.cart import Cart, CartAuth

from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth import views as auth_views
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse


def register_user(request):
    
    if request.method == 'POST':
        registerForm = RegistrationForm(request.POST)
        if registerForm.is_valid():
            user = registerForm.save(commit=False)
            user.email = registerForm.cleaned_data['email']
            user.set_password(registerForm.cleaned_data['password'])
            user.save()
            return redirect('user:register_success')
            
            
    else:
        registerForm = RegistrationForm()
    return render(request, 'user/register.html', {'form': registerForm})

def register_success(request):
    return render(request,'user/register_success.html')


class Login(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'user/login.html'
    success_url = 'user:load_cart'
    
    
    
#Loads items in cart from database,if the user was previously loged in and add something in cart    
class LoadCart(View):
    def get(self, request):
        cart = Cart(request)
        cart.cart_load_from_db()
        return HttpResponseRedirect(reverse('core:index'))
   
       
       
   
   
   
   
        
        
        

            
            
            
            
           

    
