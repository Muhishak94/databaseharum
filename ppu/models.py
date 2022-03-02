from django.db import models

# Create your models here.


class Ppu(models.Model):
    nama_dpt = models.CharField(max_length=100, null=True, blank=True)
    nik = models.CharField(max_length=20, unique=True, null=True, blank=True)
    nomor_kk = models.CharField(max_length=100, null=True, blank=True)
    alamat = models.CharField(max_length=100, null=True, blank=True)
    kota = models.CharField(max_length=40, null=True, blank=True)
    kecamatan = models.CharField(max_length=40, null=True, blank=True)
    kelurahan = models.CharField(max_length=40, null=True, blank=True)
    rt = models.IntegerField(null=True, blank=True)
    tanggal_lahir = models.DateField(null=True, blank=True)
    nomor_hp = models.CharField(max_length=40, null=True, blank=True)
    nomor_rekening = models.CharField(max_length=40, null=True, blank=True)
    bank = models.CharField(max_length=100, null=True, blank=True)
    nama_pemilik_rekening = models.CharField(
        max_length=100, null=True, blank=True)
    keterangan = models.CharField(max_length=100, null=True, blank=True)
    status_telespocheck = models.CharField(
        max_length=40, null=True, blank=True)
    hasil_telespocheck = models.CharField(max_length=40, null=True, blank=True)
    keterangan_telespocheck = models.CharField(
        max_length=100, null=True, blank=True)
    telespochecker = models.CharField(max_length=40, null=True, blank=True)
    tanggal_telespocheck = models.DateField(null=True, blank=True)
    inputer = models.CharField(max_length=40, null=True, blank=True)
    tanggal_input_data = models.DateField(null=True, blank=True)
    tanggal_honor = models.DateField(null=True, blank=True)
    nominal_honor = models.IntegerField(null=True, blank=True)
    keterangan_honor = models.CharField(
        max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nama_dpt
