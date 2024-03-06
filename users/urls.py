from django.contrib import admin
from django.urls import path
from users import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('registercustomer/',views.customers,name='registercustomer'),
    path('sendotp/',views.send_otp,name='sendotp'),
    path('login/',views.login,name='login'),
    path('forgot/',views.forgot_pass,name='forgot'),
    path('addcart/',views.addcart,name='addcart'),
    path('cart/',views.showcart,name='cart'),
    path('delcart/',views.delcart,name='delcart'),
    path('savelater/',views.addsavelater,name='savelater'),
    path('savelatershow/',views.showsavelater,name='savelatershow'),
    path('delsave/',views.delsavelater,name='delsave'),
    
]