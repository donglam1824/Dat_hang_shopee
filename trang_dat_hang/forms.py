
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
        widgets = {
            'ten_san_pham': forms.TextInput(attrs={'class': 'form-control'}),
            'gia_ban': forms.NumberInput(attrs={'class': 'form-control'}),
            'so_luong': forms.NumberInput(attrs={'class': 'form-control'}),
            'ten_shop': forms.TextInput(attrs={'class': 'form-control'}),
        }
