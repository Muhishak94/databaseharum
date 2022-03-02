# Generated by Django 4.0.1 on 2022-02-28 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ppu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_dpt', models.CharField(blank=True, max_length=100, null=True)),
                ('nik', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('nomor_kk', models.CharField(blank=True, max_length=100, null=True)),
                ('alamat', models.CharField(blank=True, max_length=100, null=True)),
                ('kota', models.CharField(blank=True, max_length=40, null=True)),
                ('kecamatan', models.CharField(blank=True, max_length=40, null=True)),
                ('kelurahan', models.CharField(blank=True, max_length=40, null=True)),
                ('rt', models.IntegerField(blank=True, null=True)),
                ('tanggal_lahir', models.DateField(blank=True, null=True)),
                ('nomor_hp', models.CharField(blank=True, max_length=40, null=True)),
                ('nomor_rekening', models.CharField(blank=True, max_length=40, null=True)),
                ('bank', models.CharField(blank=True, max_length=100, null=True)),
                ('nama_pemilik_rekening', models.CharField(blank=True, max_length=100, null=True)),
                ('keterangan', models.CharField(blank=True, max_length=100, null=True)),
                ('status_telespocheck', models.CharField(blank=True, max_length=40, null=True)),
                ('hasil_telespocheck', models.CharField(blank=True, max_length=40, null=True)),
                ('keterangan_telespocheck', models.CharField(blank=True, max_length=100, null=True)),
                ('telespochecker', models.CharField(blank=True, max_length=40, null=True)),
                ('tanggal_telespocheck', models.DateField(blank=True, null=True)),
                ('inputer', models.CharField(blank=True, max_length=40, null=True)),
                ('tanggal_input_data', models.DateField(blank=True, null=True)),
                ('tanggal_honor', models.DateField(blank=True, null=True)),
                ('nominal_honor', models.IntegerField(blank=True, null=True)),
                ('keterangan_honor', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]
