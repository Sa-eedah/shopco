from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .forms import LoginForm
from .views import CustomLogoutView

app_name = 'shopco'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(
        template_name='shopco/login.html',
        authentication_form=LoginForm
    ), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('reviews/', views.customer_reviews, name='customer_reviews'),
]
