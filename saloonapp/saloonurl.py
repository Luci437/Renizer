from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'login/index$', views.index, name='indexs'),
    path('login/', views.login, name='login'),
    path('login/checklogin/', views.checklogin, name='checklogin'),
    path('login/checkusername/', views.usernameCheck, name='usernamecheck'),
    path('login/signup/', views.signup, name='signup'),
    path('showstyle/', views.showStyle, name='showstyle'),
    path('showstyle/search/', views.search, name='search'),
    path('showstyle/menstyle/', views.maleGender, name='menstyle'),
    path('showstyle/femalestyle/', views.femaleGender, name='femalestyle'),
    path('checkbookingdate/', views.checkBookingDate, name='checkbooking'),
    path('login/checkbookingdate/', views.checkBookingDate, name='checkbooking'),
    path('booking/', views.booking, name='booking'),
    path('showstyle/searchstyle/', views.searchstyle, name='searchstyle'),
    path('product/', views.showproduct, name='product'),
    path('product/sortcategory/', views.sortCategory, name='sortcategory'),
    path('product/bycategory/', views.byCategory, name='bycategory'),
    path('product/searchproduct/', views.searchItems, name='search_item'),
    path('logout/', views.logout, name='logout'),
    path('product/tocart/', views.addtocart, name='tocart'),
    path('carts/', views.cartshow, name='carts'),
    path('carts/removecart/', views.removecart, name='removecart'),
    path('carts/paybill/', views.paybill, name='paybill'),
    path('admindash/', views.admindash, name='admindash'),
    path('updateproduct/', views.updateproduct, name='updateproduct'),
    path('<int:bookid>/updatebooking/', views.updateorders, name='updatebooking'),
    path('<int:appo_id>/attendappo/', views.attendbooking, name='attendbooking'),
    path('addproduct/', views.addproduct, name='addproduct')
]
