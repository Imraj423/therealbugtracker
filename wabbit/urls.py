from django.urls import path
from . import views
# from django.views.generic import RedirectView

urlpatterns = [
    path('', views.loginPage, name="login"),
    path('home/', views.home, name='home'),
    path('detail/<int:id>/', views.detail, name='detail'),
    path('createTicket/', views.ticket_add),
    path('logout/', views.logoutUser, name="logout"),
    path('editTicket/<int:id>/', views.edit_tick),
    path('sortt/', views.sortedt, name="sort_status"),
    path('sortx/', views.sortedx, name="sort_time"),
    path('user/<int:id>/', views.user_detail_view),
    ]
