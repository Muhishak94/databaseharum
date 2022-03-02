from django.db import models

# Create your models here.


class TabelBuah(models.Model):
    nama = models.CharField(max_length=50)
    keterangan = models.TextField()

    def __str__(self):
        return self.nama
