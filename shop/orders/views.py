from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, UpdateView, TemplateView

from .models import OrderItem, Order
from .forms import OrderCreateForm, OrderUpdateForm
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


class OrderList(PermissionRequiredMixin, ListView):
    permission_required = (
        'orders.order_item.view_order_item',
    )
    model = OrderItem
    context_object_name = 'orders'
    template_name = 'orders/order_list.html'
    queryset = OrderItem.objects.all()


# class OrderList(TemplateView):
#     template_name = 'orders/order_list.html'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         set_categories = {order: order.objects.all() for order in OrderItem.objects.filter()}
#         context['all_items_by_orders'] = set_categories
#         return context


class OrderUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = (
        'orders.order_item.change_order',
    )
    template_name = 'orders/update.html'
    form_class = OrderUpdateForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Order.objects.get(pk=id)

