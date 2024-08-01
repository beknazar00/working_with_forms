from django.contrib import admin
from django.shortcuts import get_object_or_404

from online_shop.models import Product, Category

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)


#######

def add_order(request, en_slug):
    product = get_object_or_404(Product, slug=en_slug)

    print(request.POST.get('quantity'))

    if product.quantity >= int(request.POST.get('quantity')):
        product.quantity -= int(request.POST.get('quantity'))
        product.save()
        changed_slug = product.slug
        if request.method == 'POST':
            form = OrderForm(request.POST)
            if form.is_valid():
                order = form.save(commit=False)
                order.product = product
                order.save()
                messages.success(request, 'Order successfully created🎉')
                return redirect('details', changed_slug)
    else:
        form = OrderForm(request.GET)
        messages.success(request, "Pls, Order less product❗️")

    context = {'form': form,
               'product': product}

    return render(request, 'shopping/detail.html', context)
