from django.urls import re_path
from . import views

urlpatterns = [
    re_path('pricing/', views.pricing_table, name='pricing_table'),
    re_path('rate/<int:plan_id>/', views.rate_subscription, name='rate_subscription'),
]
