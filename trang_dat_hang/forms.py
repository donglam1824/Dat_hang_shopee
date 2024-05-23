
from django import forms
from .models import SanPham

class SanPhamForm(forms.ModelForm):
    class Meta:
        model = SanPham
        fields = ['anh', 'ten_san_pham', 'gia_ban', 'so_luong', 'ten_shop']
        labels = {
            'anh': 'Ảnh sản phẩm',
            'ten_san_pham': 'Tên sản phẩm',
            'gia_ban': 'Giá bán',
            'so_luong': 'Số lượng',
            'ten_shop': 'Tên shop',
        }
