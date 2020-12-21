from django.core import serializers
from django.http import JsonResponse, HttpResponseRedirect, request
from django.shortcuts import render
from django.template import RequestContext
from django.urls import reverse

from .models import *
# Create your views here.


def index(request):
    return render(request, 'index.html')


def login(request):
    return render(request, 'joinlogin.html')


def checklogin(request):
    data = {}
    is_user_exists = False
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if LoginInfo.objects.filter(username=username, password=password).exists():
            is_user_exists = True
            data = {'response': is_user_exists}
            logobj = LoginInfo.objects.get(username=username, password=password)
            request.session['user_id'] = logobj.id
            return JsonResponse(data)
        else:
            data = {'response': is_user_exists}

        return JsonResponse(data)
    return login(request)


def usernameCheck(request):
    data = {}
    is_user_exists = False
    if request.method == 'POST':
        username = request.POST.get('username')

        if LoginInfo.objects.filter(username=username).exists():
            is_user_exists = True
            data = {'response':is_user_exists}

            return JsonResponse(data)
        else:
            data = {'response':is_user_exists}
            return JsonResponse(data)

    return HttpResponseRedirect(reverse('login'))


def signup(request):
    if request.method == 'POST':
        name = request.POST.get('fname')
        username = request.POST.get('username')
        password = request.POST.get('password')

        obj = LoginInfo()
        obj.fname = name
        obj.username = username
        obj.password = password
        obj.save()

        data = {'done':'Welcome to Renizer Family,Login to Continue.'}

        return JsonResponse(data)
    return HttpResponseRedirect(reverse('index'))


def showStyle(request):
    styleobj = HairStyles.objects.all()
    return render(request, 'hairstyle.html',{'styles':styleobj})


def search(request):
    data = {}
    if request.method == 'POST':
        search = request.POST.get('search')

        if LoginInfo.objects.filter(fname__contains=search).exists():
            obj = serializers.serialize('json',list(LoginInfo.objects.all()), fields=('fname','username'))
            data = {'result':obj}
            return JsonResponse(data, status=200)
        else:
            data = {'result':'empty'}
            return JsonResponse(data, status=400)


    return render(request, 'hairstyle.html')


def maleGender(request):
    obj = HairStyles.objects.filter(gender='male')
    data = {
        'styles': list(obj.values_list()),
        'totalitems': obj.count()
    }
    return JsonResponse(data)


def femaleGender(request):
    obj = HairStyles.objects.filter(gender='female')
    data = {
        'styles': list(obj.values_list()),
        'totalitems': obj.count()
    }
    return JsonResponse(data)


def checkBookingDate(request):
    if request.method == 'POST':
        is_availabled = False
        dk = request.POST.get('bkdate')
        obj = Booking.objects.filter(booking_date__exact=dk).count()
        if obj <= 10:
            is_availabled = True
            data = {
                'is_available': is_availabled
            }
        else:
            is_availabled = False
            data = {
                'is_available': is_availabled
            }

        return JsonResponse(data)
    return index(request)


def booking(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile = request.POST.get('mobile')
        booking_date = request.POST.get('booking_date')

        bookcount = Booking.objects.filter(booking_date=booking_date).count()
        if bookcount <= 10:
            obj = Booking()
            obj.booker_name = name
            obj.mobile = mobile
            obj.booking_date = booking_date
            obj.booked_date = datetime.now()
            obj.save()

            data = {
                'response': 'Thank you for the booking, we are waiting'
            }
        else:
            data = {
                'response': 'Sorry to say, we are full on '+booking_date
            }

        return JsonResponse(data)


def searchstyle(request):
    if request.method == 'POST':
        stylename = request.POST.get('stylename')

        if HairStyles.objects.filter(style_name__contains=stylename).exists():
            obj = HairStyles.objects.filter(style_name__contains=stylename)
            data = {
                'styles': list(obj.values_list()),
                'totalitems': obj.count()
            }
        else:
            data = {
                'styles': 'none'
            }

        return JsonResponse(data)


def showproduct(request):
    obj = Product.objects.filter(product_stock__gt=0)
    catobj = ProductCategory.objects.all()
    return render(request, 'products.html',{'products': obj,'cats': catobj})


def sortCategory(request):
    if request.method == 'POST':

        sortby = request.POST.get('sortby')
        category = request.POST.get('category')

        print(category)

        if category == 'all':
            obj = Product.objects.filter(product_stock__gt=0).order_by(sortby)
            data = {
                'products': list(obj.values_list()),
                'total_items': obj.count(),
                'category': list(ProductCategory.objects.all().values_list())
            }
        else:
            catobj = ProductCategory.objects.get(category_name=category)
            obj = Product.objects.filter(category=catobj,product_stock__gt=0).order_by(sortby)
            data = {
                'products': list(obj.values_list()),
                'total_items': obj.count(),
                'category': list(ProductCategory.objects.all().values_list())
            }

    return JsonResponse(data)

def byCategory(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        sortby = request.POST.get('sortby')

        if category == 'all':
            obj = Product.objects.filter(product_stock__gt=0).order_by(sortby)
            data = {
                'products': list(obj.values_list()),
                'total_items': obj.count(),
                'category': list(ProductCategory.objects.all().values_list())
            }
        else:
            catobj = ProductCategory.objects.get(category_name=category)
            obj = Product.objects.filter(category=catobj, product_stock__gt=0).order_by(sortby)
            data = {
                'products': list(obj.values_list()),
                'total_items': obj.count(),
                'category': list(ProductCategory.objects.all().values_list())
            }

    return JsonResponse(data)


def searchItems(request):
    if request.method == 'POST':
        search = request.POST.get('search')

        if Product.objects.filter(product_name__contains=search,product_stock__gt=0).exists():
            obj = Product.objects.filter(product_name__contains=search,product_stock__gt=0)
            data = {
                'products': list(obj.values_list()),
                'total_items': obj.count(),
                'category': list(ProductCategory.objects.all().values_list())
            }
        else:
            data = {
                'products': 'none',
                'total_items': '',
                'category': list(ProductCategory.objects.all().values_list())
            }

        return JsonResponse(data)


def logout(request):
    if request.session.has_key('user_id'):
        del request.session['user_id']
    return HttpResponseRedirect(reverse('index'))


def addtocart(request):
    if request.method == 'POST':
        prd_id = request.POST.get('prd_id')

        logobj = LoginInfo.objects.get(id=request.session['user_id'])
        prdobj = Product.objects.get(id=prd_id,product_stock__gt=0)

        if Cart.objects.filter(user_id=logobj, product_id=prdobj).exists():
            data = {
                'response': True,
                'cartcount': Cart.objects.filter(user_id=LoginInfo.objects.get(id=request.session['user_id'])).count()
            }
        else:
            obj = Cart()
            obj.product_id = prdobj
            obj.user_id = logobj
            obj.is_in_cart = True
            obj.save()

            data = {
                'response': False,
                'cartcount': Cart.objects.filter(user_id=LoginInfo.objects.get(id=request.session['user_id'])).count()
            }

        return JsonResponse(data)


def cartshow(request):
    if request.session.has_key('user_id'):
        cartobj = Cart.objects.filter(user_id=LoginInfo.objects.get(id=request.session['user_id']),is_in_cart=True)
        totalamount = 0

        for cart in cartobj:
            totalamount += cart.product_id.product_price

        if totalamount == 0:
            return HttpResponseRedirect(reverse('product'))

        return render(request, 'cart.html', {'carts': cartobj,'totalpay': totalamount})
    return HttpResponseRedirect(reverse('index'))


def removecart(request):
    if request.method == 'POST':
        prdid = request.POST.get('prdid')

        obj = Cart.objects.get(user_id=LoginInfo.objects.get(id=request.session['user_id']),product_id=Product.objects.get(id=prdid))
        obj.delete()

        cartobj = Cart.objects.filter(user_id=LoginInfo.objects.get(id=request.session['user_id']))
        prdobj = Product.objects.all()

        totalamount = 0

        for cart in cartobj:
            totalamount += cart.product_id.product_price

        data = {
            'carts': list(cartobj.values_list()),
            'product': list(prdobj.values_list()),
            'totalpay': totalamount
        }

        return JsonResponse(data)


def paybill(request):
    if request.method == 'POST':
        address = request.POST.get('address')
        state = request.POST.get('state')
        city = request.POST.get('city')
        pincode = request.POST.get('pincode')
        phone = request.POST.get('phone')
        cardnumber = request.POST.get('cardnumber')
        cardname = request.POST.get('cardname')
        cvv = request.POST.get('cvv')
        cardexp = request.POST.get('cardexp')
        finalpay = request.POST.get('totalpay')

        logobj = LoginInfo.objects.get(id=request.session['user_id'])

        billingobj = Billing()
        billingobj.user_id = logobj
        billingobj.totalpay = finalpay
        billingobj.save()

        billaddobj = BillingAddress()
        billaddobj.billingid = billingobj
        billaddobj.address = address
        billaddobj.state = state
        billaddobj.city = city
        billaddobj.pincode = pincode
        billaddobj.phone = phone
        billaddobj.save()

        cardobj = BillingCard()
        cardobj.billingid = billingobj
        cardobj.cardname = cardname
        cardobj.cardnumber = cardnumber
        cardobj.cardexp = cardexp
        cardobj.cardcvv = cvv
        cardobj.save()

        itemobj = Cart.objects.filter(user_id=logobj)
        for it in itemobj:
            billobj = BillingItem()
            billobj.billingid = billingobj
            billobj.itemid = it.product_id
            billobj.save()

            itobj = Product.objects.get(id=it.product_id_id)
            itobj.product_stock -= 1
            itobj.save()

        itemobj.delete()

        data = {
            'response':True
        }

        return JsonResponse(data)


def admindash(request):
    userobj = LoginInfo.objects.all()
    prodobj = Product.objects.all()
    billingobj = Billing.objects.filter(is_active=True)
    billitemobj = BillingItem.objects.all()
    billaddobj = BillingAddress.objects.all()
    appobj = Booking.objects.filter(booked_date__gte=datetime.now(), is_active=True)
    catobj = ProductCategory.objects.all()

    totalamount = 0

    for book in billingobj:
        totalamount += book.totalpay

    return render(request, 'admindash.html',{'users':userobj,'appos':appobj ,'products': prodobj , 'turnover': totalamount,'booking': billingobj,'bookitem': billitemobj,'bookaddress': billaddobj,'cats':catobj})


def updateproduct(request):
    if request.method == 'POST':
        price = request.POST.get('price')
        qty = request.POST.get('qty')
        prdid = request.POST.get('prdid')

        prdobj = Product.objects.get(id=prdid)
        prdobj.product_price = price
        prdobj.product_stock = qty
        prdobj.save()

        return HttpResponseRedirect(reverse('admindash'))


def updateorders(request,bookid):
    bookobj = Billing.objects.get(id=bookid)
    bookobj.is_active = False
    bookobj.save()

    return HttpResponseRedirect(reverse('admindash'))


def attendbooking(request,appo_id):
    appobj = Booking.objects.get(id=appo_id)
    appobj.is_active = False
    appobj.save()

    return HttpResponseRedirect(reverse('admindash'))


def addproduct(request):
    if request.method == 'POST':
        pname = request.POST.get('product-name')
        price = request.POST.get('price')
        qty = request.POST.get('qty')
        pimg = request.FILES['image']
        gender = request.POST.get('gender')
        category = request.POST.get('category')

        catobj = ProductCategory.objects.get(category_name=category)

        prdobj = Product()
        prdobj.product_name = pname
        prdobj.product_price = price
        prdobj.product_stock = qty
        prdobj.product_img = pimg
        prdobj.product_gender = gender
        prdobj.category = catobj
        prdobj.save()

        return HttpResponseRedirect(reverse('admindash'))