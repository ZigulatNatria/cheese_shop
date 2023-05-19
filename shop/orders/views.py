from django.shortcuts import render
from django.views.generic import ListView

from .models import OrderItem
from .forms import OrderCreateForm
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(order=order,
                                         product=item['product'],
                                         price=item['price'],
                                         quantity=item['quantity']
                                         )
            # очистить корзину
            cart.clear()
            return render(request,
                          'orders/created.html',
                          {'order': order}
                          )
    else:
        form = OrderCreateForm()
    return render(request,
                  'orders/create.html',
                  {'cart': cart, 'form': form}
                  )


class OrderList(ListView):
    model = OrderItem
    context_object_name = 'orders'
    template_name = 'orders/order_list.html'
    queryset = OrderItem.objects.all()

