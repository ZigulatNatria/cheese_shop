from django.contrib.auth.models import User
from django.http import request
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from orders.models import OrderItem


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'protect/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_aut'] = self.request.user.groups.exists()
        return context

    # def orders(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['order_user'] = OrderItem.objects.filter(first_name='Oleg')
    #     return context