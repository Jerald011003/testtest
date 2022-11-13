from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView
from accounts import views
from .view import contact_page

from accounts.views import register_page

from django.contrib.auth import views as auth_views

#importing static infos
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", include("django.contrib.auth.urls")),
    # path('contact/', contact_page),
    path('admin/', admin.site.urls),

    #RecordList
    path('record/', views.index, name="recordlist"),
    # path('record/', views.index),
    # path('addnew',views.addnew),
    # path('edit/<int:id>', views.edit),
    # path('update/<int:id>', views.update),
    # path('delete/<int:id>', views.destroy),

   #Login
    path('register/', views.register_page, name="register"),
    path('login/', views.loginPage2, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    #Search
    # path('search/', include("search.urls", namespace='search')),

    #All Source Code
    path('dashboard/', views.dashboard2, name="dashboard"),
    path('customer/<str:pk_test>/', views.customer2, name="customer"),
    path('products/', views.products2, name="products"),

    path('create_order/<str:pk>/', views.createOrder, name="create_order"),
    path('update_order/<str:pk>/', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>/', views.deleteOrder, name="delete_order"),
    path('', views.dashboard2, name="home"),

    path('allcustomer/', views.allcustomer, name="allcustomer"),
    path('invoices/', views.invoices, name="invoices"),
    path('createcustomer/', views.createCustomer, name="createcustomer"),
    path('order_form', views.orderForm, name="orderform")
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
