from django.urls import path
from .views import index, other_page, BBLoginView,profile_login, BBLogoutView

app_name = 'main'
urlpatterns = [
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
    path('account/login', BBLoginView.as_view(), name='login'),
    path('account/profile', profile_login, name='profile'),
    path('account/logout', BBLogoutView.as_view(), name='logout')

]