from django.shortcuts import render, redirect
from .forms import SanPhamForm

# Create your views here.
def them_san_pham(request):
    form = SanPhamForm()
    if request.method == 'POST':
        form = SanPhamForm(request.POST, request.FILES)   #Xu li file anh
        if form.is_valid():
            form.save()
            return redirect('danh sach san pham')
        else:
            form = SanPhamForm()

    return render(request, "trang_dat_hang/them_san_pham.html", {'form': form})


