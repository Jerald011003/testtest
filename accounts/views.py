from django.shortcuts import render, redirect
from accounts.forms import EmployeeForm
from accounts.models import Employee

from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth

from django.http import HttpResponse

from .models import *
from .forms import OrderForm, CreateUserForm
from django.forms import inlineformset_factory
from .filters import OrderFilter, CustomerFilter

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms import *
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'auth/register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'auth/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

# Create your views here.
def addnew(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('record/')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request,'index.html',{'form':form})
def index(request):
    employees = Employee.objects.all()
    return render(request,"show.html",{'employees':employees})
def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request,'edit.html', {'employee':employee})
def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance = employee)
    if form.is_valid():
        form.save()
        return redirect("/record")
    return render(request, 'edit.html', {'employee': employee})
def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/record")

#All Source Code
@login_required(login_url='login')
def dashboard2(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    mycusFilter = CustomerFilter(request.GET, queryset=customers)
    customers = mycusFilter.qs

    total_customers = customers.count()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {'orders': orders, 'customers': customers,
               'total_orders': total_orders, 'delivered': delivered,
               'pending': pending, 'mycusFilter': mycusFilter}

    return render(request, 'dashboard2.html', context)

@login_required(login_url='login')
def products2(request):
    products2 = ProductForCustomer.objects.all()

    return render(request, 'products2.html', {'products2' :products2})

@login_required(login_url='login')
def allcustomer(request):
    customer2 = Customer.objects.all()

    return render(request, 'allcustomer.html', {'customer2' :customer2})

@login_required(login_url='login')
def customer2(request, pk_test):
    customer = Customer.objects.get(id=pk_test)

    orders = customer.order_set.all()
    order_count = orders.count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context = {'customer': customer, 'orders': orders, 'order_count': order_count,
               'myFilter': myFilter}

    return render(request, 'customer2.html', context)

def createCustomer(request):
        form = CustomerForm
        if request.method == "POST":
            form = CustomerForm(request.POST)
            if form.is_valid():
                try:
                    form.save()
                    return redirect('/')
                except:
                    pass
        else:
            form = CustomerForm()
        context = {
            'form': form
        }
        return render(request, 'createcustomer.html', context)

@login_required(login_url='login')
def createOrder(request, pk):
        OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=3 )
        customer = Customer.objects.get(id=pk)
        formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
        #form = OrderForm(initial={'customer':customer})
        if request.method == 'POST':
                #print('Printing POST:', request.POST)
                #form = OrderForm(request.POST)
                formset = OrderFormSet(request.POST, instance=customer)
                if formset.is_valid():
                    formset.save()
                    return redirect('/')

        context = {'form':formset}
        return render(request, 'order_form.html', context)

@login_required(login_url='login')
def updateOrder(request, pk):

        order = Order.objects.get(id=pk)
        form = OrderForm(instance=order)

        if request.method == 'POST':
                form = OrderForm(request.POST, instance=order)
                if form.is_valid():
                    form.save()
                    return redirect('/')

        context = {'form':form}
        return render(request, 'order_form.html', context)

@login_required(login_url='login')
def deleteOrder(request, pk):
        order = Order.objects.get(id=pk)
        if request.method == "POST":
            order.delete()
            return redirect('/')

        context = {'item':order}
        return render(request, 'delete.html', context)

@login_required(login_url='login')
def invoices(request):
    customer2 = Customer.objects.all()


    return render(request, 'invoices.html', {'customer2' :customer2})

def orderForm(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'create_order.html', context)