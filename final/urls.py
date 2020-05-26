"""session URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from web import views
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('signup/',views.createuser,name='createuser'),
    path('home/',views.home,name='home'),
    path('logoutuser/',views.logoutuser,name='logoutuser'),
    path('abt/',views.abt,name='abt'),
    path('cart/',views.cart,name='cart'),
    path('cse/',views.cse,name='cse'),
    path('ece/',views.ece,name='ece'),
    path('eee/',views.eee,name='eee'),
    path('mech/',views.mech,name='mech'),
    path('civil/',views.civil,name='civil'),
    path('conformation/',views.conformation,name='conformation'),
    path('mycart/',views.mycart,name='mycart'),
    path('<int:my_id>/',views.returned,name="return"),
    path('<int:my_id>/',views.delete,name="delete"),
    path('returned/',views.past,name="past"),



]
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
