from django.db import models

# Create your models here.
class MatHang(models.Model):
    ten_san_pham = models.CharField(max_length=100)
    gia_ban = models.DecimalField(max_digits=10)
    so_luong = models.IntegerField()
    ten_shop = models.CharField(max_length= 50)

    def __str__(self):
        return self.ten_san_pham