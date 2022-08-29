from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from order.models import Shop, Menu, Order, OrderFood

@csrf_exempt
def orders(request, shop):
    if request.method == 'GET':
        order = Order.objects.filter(shop=shop)
        return render(request, 'owner/order_list.html', {'order_list': order})
    else:
        return HttpResponse(status=405)
