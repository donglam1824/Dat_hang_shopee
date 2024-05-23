from django.db import models

# Create your models here.
class SanPham(models.Model):
    anh = models.ImageField(upload_to='images/')
    ten_san_pham = models.CharField(max_length=100)
    gia_ban = models.DecimalField(max_digits=10, decimal_places=2)
    so_luong = models.PositiveIntegerField()
    ten_shop = models.CharField(max_length= 50)

    def __str__(self):
        return self.ten_san_pham