# Generated by Django 4.0.1 on 2022-02-19 01:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hasil_Telespocheck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hasil', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Inputer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('penginput', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Kecamatan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namakecamatan', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Kelurahan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namakelurahan', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Kota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('namakota', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Status_Telespocheck',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Telespochecker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('penelpon', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Database',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_dpt', models.CharField(max_length=100)),
                ('rt', models.IntegerField(null=True)),
                ('nomor_kk', models.IntegerField(null=True)),
                ('nik', models.IntegerField(null=True)),
                ('alamat', models.CharField(blank=True, max_length=100)),
                ('tanggal_lahir', models.DateField(default='Tanggal Lahir')),
                ('nomor_hp', models.IntegerField(null=True)),
                ('nomor_rekening', models.IntegerField(null=True)),
                ('bank', models.CharField(blank=True, max_length=100)),
                ('nama_pemilik_rekening', models.CharField(blank=True, max_length=100)),
                ('keterangan', models.CharField(blank=True, max_length=100)),
                ('keterangan_telespocheck', models.CharField(default='Ket. Telespocheck', max_length=100)),
                ('tanggal_telespocheck', models.DateField(default='Tgl Telpon')),
                ('tanggal_input_data', models.DateField(default='Tgl Input')),
                ('tanggal_honor', models.DateField(default='Tgl Pembayaran')),
                ('nominal_honor', models.IntegerField(default='Rp. ')),
                ('keterangan_honor', models.CharField(default='Ket. Honor', max_length=100)),
                ('hasil_telespocheck', models.ForeignKey(default='Proggress', on_delete=django.db.models.deletion.CASCADE, to='harum.hasil_telespocheck')),
                ('inputer', models.ForeignKey(default='Harum Center', on_delete=django.db.models.deletion.CASCADE, to='harum.inputer')),
                ('kecamatan', models.ForeignKey(default='Pilih Kecamatan', on_delete=django.db.models.deletion.CASCADE, to='harum.kecamatan')),
                ('kelurahan', models.ForeignKey(default='Pilih Kelurahan', on_delete=django.db.models.deletion.CASCADE, to='harum.kelurahan')),
                ('kota', models.ForeignKey(default='Pilih Kota', on_delete=django.db.models.deletion.CASCADE, to='harum.kota')),
                ('status_telespocheck_id', models.ForeignKey(default='Status Telespocheck', on_delete=django.db.models.deletion.CASCADE, to='harum.status_telespocheck')),
                ('telespochecker', models.ForeignKey(default='Penelpon', on_delete=django.db.models.deletion.CASCADE, to='harum.telespochecker')),
            ],
        ),
    ]