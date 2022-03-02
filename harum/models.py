from email.policy import default
from django.db import models

# Create your models here.


class Kota(models.Model):
    namakota = models.CharField(max_length=40)

    def __str__(self):
        return self.namakota


class Kecamatan(models.Model):
    namakecamatan = models.CharField(max_length=40)

    def __str__(self):
        return self.namakecamatan


class Kelurahan(models.Model):
    namakelurahan = models.CharField(max_length=40)

    def __str__(self):
        return self.namakelurahan


class Status_Telespocheck(models.Model):
    status = models.CharField(max_length=20)

    def __str__(self):
        return self.status


class Hasil_Telespocheck(models.Model):
    hasil = models.CharField(max_length=40)

    def __str__(self):
        return self.hasil


class Telespochecker(models.Model):
    penelpon = models.CharField(max_length=40)

    def __str__(self):
        return self.penelpon


class Inputer(models.Model):
    penginput = models.CharField(max_length=40)

    def __str__(self):
        return self.penginput


class Database(models.Model):
    nama_dpt = models.CharField(max_length=100)
    nik = models.IntegerField(null=True, blank=True)
    nomor_kk = models.IntegerField(null=True, blank=True)
    alamat = models.CharField(max_length=100, null=True, blank=True)
    kota = models.ForeignKey(
        Kota, on_delete=models.CASCADE, null=True, blank=True)
    kecamatan = models.ForeignKey(
        Kecamatan, on_delete=models.CASCADE, null=True, blank=True)
    kelurahan = models.ForeignKey(
        Kelurahan, on_delete=models.CASCADE, null=True, blank=True)
    rt = models.IntegerField(null=True, blank=True)
    tanggal_lahir = models.DateField(null=True, blank=True)
    nomor_hp = models.IntegerField(null=True, blank=True)
    nomor_rekening = models.IntegerField(null=True, blank=True)
    bank = models.CharField(max_length=100, null=True, blank=True)
    nama_pemilik_rekening = models.CharField(
        max_length=100, null=True, blank=True)
    keterangan = models.CharField(max_length=100, null=True, blank=True)
    status_telespocheck = models.ForeignKey(
        Status_Telespocheck, on_delete=models.CASCADE, null=True, blank=True)
    hasil_telespocheck = models.ForeignKey(
        Hasil_Telespocheck, on_delete=models.CASCADE, null=True, blank=True)
    keterangan_telespocheck = models.CharField(
        max_length=100, null=True, blank=True)
    telespochecker = models.ForeignKey(
        Telespochecker, on_delete=models.CASCADE, null=True, blank=True)
    tanggal_telespocheck = models.DateField(null=True, blank=True)
    inputer = models.ForeignKey(
        Inputer, on_delete=models.CASCADE, null=True, blank=True)
    tanggal_input_data = models.DateField(null=True, blank=True)
    tanggal_honor = models.DateField(null=True, blank=True)
    nominal_honor = models.IntegerField(null=True, blank=True)
    keterangan_honor = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.nama_dpt
