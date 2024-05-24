from django.contrib import admin
from django.utils.html import format_html
from django.urls import reverse
from .models import SanPham

@admin.register(SanPham)
class SanPhamAdmin(admin.ModelAdmin):
    list_display = ('ten_san_pham', 'gia_ban', 'so_luong', 'ten_shop', 'trang_thai', 'custom_actions')
    search_fields = ('ten_san_pham', 'ten_shop__ten_shop')  
    actions = ['dong_y', 'tu_choi']

    # Lọc sản phẩm chờ phê duyệt
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.path == '/admin/trang_dat_hang/sanpham/':  # Chỉ lọc trên trang danh sách sản phẩm
            return qs.filter(trang_thai='cho_duyet')
        return qs

    # Truyền biến is_pending_approval vào context
    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['is_pending_approval'] = request.path == '/admin/trang_dat_hang/sanpham/'
        return super().changelist_view(request, extra_context=extra_context)

    # Actions tùy chỉnh
    def dong_y(self, request, queryset):
        queryset.update(trang_thai='dong_y')
    dong_y.short_description = "Đồng ý sản phẩm"

    def tu_choi(self, request, queryset):
        queryset.update(trang_thai='tu_choi')
    tu_choi.short_description = "Từ chối sản phẩm"

    def custom_actions(self, obj):
        return format_html(
            '<a class="button" href="{}">Tăng số lượng</a>&nbsp;'
            '<a class="button" href="{}">Giảm số lượng</a>',
            reverse('admin:trang_dat_hang_sanpham_change', args=[obj.pk]) + '?action=tang_so_luong',
            reverse('admin:trang_dat_hang_sanpham_change', args=[obj.pk]) + '?action=giam_so_luong',
        )
    
    
    # Xử lý actions trong view
    def change_view(self, request, object_id, form_url='', extra_context=None):
        if request.method == 'GET':
            action = request.GET.get('action')
            if action == 'tang_so_luong':
                san_pham = SanPham.objects.get(pk=object_id)
                san_pham.so_luong += 1
                san_pham.save()
            elif action == 'giam_so_luong':
                san_pham = SanPham.objects.get(pk=object_id)
                if san_pham.so_luong > 0:
                    san_pham.so_luong -= 1
                    san_pham.save()
        return super().change_view(request, object_id, form_url, extra_context)