from django.urls import path,include
from calculate.views import *

urlpatterns = [
    path('',index,name='home'),
    path('calculation',calculation)

]