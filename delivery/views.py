from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from order.models import Shop, Menu, Order, OrderFood

@csrf_exempt
def orders(request):
    if request.method == 'GET':
        order = Order.objects.all()
        return render(request, 'delivery/order_list.html', {'order_list': order})
        
    elif request.method == 'POST':
        order = Order.objects.get(pk=int(request.POST['order_id']))
        order.deliver_finish = 1
        order.save()
        return render(request, 'delivery/success.html')
    else:
        return HttpResponse(status=405)