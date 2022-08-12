from django.urls import path
from . import views


urlpatterns = [
    path('', views.OrderCreateListView.as_view(), name='orders'),
    path('<int:order_id>/', views.PostRetriewveUpdateDeleteOrder.as_view()),
    path('update-status/<int:order_id>/', views.UpdateOrderStatus.as_view()),
    path('user-orders/', views.UserOdersView.as_view())
]
