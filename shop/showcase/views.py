from django import forms
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
from django.db.models import Q


class ProductListlView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products.html'
    queryset = Product.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_product_form = CartAddProductForm()
        context['my_form'] = cart_product_form
        # context['is_aut'] = self.request.user.groups.exists()
        return context

    def product_add_cart(self):   #Форма добавления продукта в корзину
        cart_product_form = CartAddProductForm()
        return cart_product_form


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'product.html'
    queryset = Product.objects.all()

    def product_add_cart(self):   #Форма добавления продукта в корзину
        current_product = self.get_object()
        product_id = current_product.id
        # cart_product_form = CartAddProductForm()

        class CartAddProductForm(forms.Form):

            product = Product.objects.get(id=product_id)
            list_amount = product.amount + 1
            PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, list_amount)]

            quantity = forms.TypedChoiceField(label='Колличество', choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
            override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
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
    context_object_name = 'categories'
    template_name = 'categories.html'
    queryset = Category.objects.all()


def by_category(request, category_id):
    products = Product.objects.filter(productCategory=category_id)
    productCategory = Category.objects.all()
    current_category = Category.objects.get(pk=category_id)
    context = {'products': products, 'productCategory': productCategory, 'current_category': current_category}
    # return render (request, 'by_category.html', context)
    return render (request, 'products.html', context)


class ProductAddView(CreateView):
    model = Product
    template_name = 'create.html'
    form_class = ProductForm
    success_url = reverse_lazy('products')


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


def search(request):
    search_query = request.GET.get('search', '') # передаётся имя ввода (строка поиска)

# если значение search_query существует (в строку поиска введён текст) ищем в нужных полях введённый текст
    if search_query:
        # Q(позволяет илспользовать "И", "ИЛИ")
        products = Product.objects.filter(Q(name__icontains=search_query) | Q(name__icontains=search_query.capitalize())
                                   | Q(name__icontains=search_query.casefold()))
    else:
        products = Product.objects.all()
    context = {'products': products}
    return render(request, 'search.html', context)