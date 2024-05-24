from django.shortcuts import get_object_or_404, render, redirect
from trang_dat_hang.models import SanPham

# Create your views here.
def product_list(request):
    products = SanPham.objects.filter(trang_thai='cho_duyet')

    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        action = request.POST.get('action')
        product = get_object_or_404(SanPham, pk=product_id)

        if action == 'approve':
            product.trang_thai = 'dong_y'
        elif action == 'reject':
            product.trang_thai = 'tu_choi'
        elif action == 'increase_quantity':
            product.so_luong += 1
        elif action == 'decrease_quantity':
            if product.so_luong > 0:
                product.so_luong -= 1

        product.save()
        return redirect('custom_admin:product_list')

    return render(request, 'customadmin/list.html', {'products': products})

def approved_list(request):
    products = SanPham.objects.filter(trang_thai='dong_y')

    return render(request, r'customadmin\approved_list.html', {'products': products})
