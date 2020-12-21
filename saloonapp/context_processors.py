from .models import *


def allhaveit(request):
    if request.session.has_key('user_id'):
        cartcount = Cart.objects.filter(user_id=LoginInfo.objects.get(id=request.session['user_id'])).count()
        return {'cartcount': cartcount}
    else:
        return {'cartcount':''}