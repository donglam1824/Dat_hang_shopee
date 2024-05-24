from django.shortcuts import render, redirect

from trang_dat_hang.models import SanPham
from .forms import SanPhamForm

# Create your views here.
def home(request):
    return redirect('them_san_pham')

def them_san_pham(request):
    form = SanPhamForm()
    if request.method == 'POST':
        form = SanPhamForm(request.POST, request.FILES)   #Xu li file anh
        if form.is_valid():
            form.save()
            return redirect('them_san_pham')
        else:
            form = SanPhamForm()

    return render(request, "trang_dat_hang/them_san_pham.html", {'form': form})


