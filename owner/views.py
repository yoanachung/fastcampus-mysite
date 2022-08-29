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

@csrf_exempt
def accept(request):
    if request.method == 'POST':
        order = Order.objects.get(pk=int(request.POST['order_id']))
        order.estimated_time = int(request.POST['estimated_time'])
        order.save()
        shop = order.shop
        return render(request, 'owner/success.html', {'shop': shop})
    else:
        return HttpResponse(status=405)