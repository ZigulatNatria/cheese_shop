from django.shortcuts import render, redirect #get_object_or_404
from django.views.generic import DetailView, ListView
from .models import Product, Category, Comment
from django.views.generic.edit import CreateView
from .forms import ProductForm, ContactForm   #, UserCommentForm, GuestCommentForm
from cart.forms import CartAddProductForm
from django.urls import reverse_lazy
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib import messages

# Create your views here.
class ProductListlView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products.html'
    queryset = Product.objects.all()


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'product.html'
    queryset = Product.objects.all()

    def product_add_cart(self):
        cart_product_form = CartAddProductForm()
        return cart_product_form

    # def comment(self, request, category_pk, pk):
    #     product = Product.objects.get(pk=pk)
    #     comments = Comment.objects.filter(Product=pk, is_active=True)
    #     initial = {'product': product.pk}
    #     form_class = GuestCommentForm
    #     form = form_class(initial=initial)
    #     if request.method == 'POST':
    #         c_form = form_class(request.POST)
    #         if c_form.is_valid():
    #             c_form.save()



class CategoryListlView(ListView):
    model = Category
    context_object_name = 'categorys'
    template_name = 'base.html'
    queryset = Category.objects.all()


def by_category(request, category_id):
    products = Product.objects.filter(productCategory=category_id)
    productCategory = Category.objects.all()
    current_category = Category.objects.get(pk=category_id)
    context = {'products': products, 'productCategory': productCategory, 'current_category': current_category}
    return render (request, 'by_category.html', context)


class ProductAddView(CreateView):
    model = Product
    template_name = 'create.html'
    form_class = ProductForm
    success_url = reverse_lazy('categorys')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = "Заказ сыра!!!"
            body = {
                'name': form.cleaned_data['name'],
                'telephone': form.cleaned_data['telephone'],
                'message': form.cleaned_data['message'],
            }
            message = "\n".join(body.values()) #при переписывании на цифры в формах вылетает ошибка типов
            try:
                send_mail(subject, message,
                          'vachrameev.oleg@yandex.ru',
                          ['zigulatnatria@yandex.ru'])
            except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
            return redirect("/cheese/")
        else:
            messages.error(request, 'НЕПРАВИЛЬНО ВВЕДЁН КОД С КАРТИНКИ') #сообщение если капча не верна

    form = ContactForm()
    return render(request, "contact.html", {'form': form})
