from django.forms import ModelForm
from django import forms
from bontang.models import Bontang


class FormBontang(ModelForm):
    class Meta:
        model = Bontang
        fields = '__all__'
        pilihankota = (
            ('BONTANG', 'BONTANG'),
        )
        pilihankecamatan = (
            ('', ''),
            ('BONTANG BARAT', 'BONTANG BARAT'),
            ('BONTANG SELATAN', 'BONTANG SELATAN'),
            ('BONTANG UTARA', 'BONTANG UTARA'),
        )
        pilihankelurahan = (
            ('', ''),
            ('BELIMBING', 'BELIMBING'),
            ('GUNUNG TELIHAN', 'GUNUNG TELIHAN'),
            ('KANAAN', 'KANAAN'),
            ('BERBAS PANTAI', 'BERBAS PANTAI'),
            ('BERBAS TENGAH', 'BERBAS TENGAH'),
            ('BONTANG LESTARI', 'BONTANG LESTARI'),
            ('SATIMPO', 'SATIMPO'),
            ('TANJUNG LAUT', 'TANJUNG LAUT'),
            ('TANJUNG LAUT INDAH', 'TANJUNG LAUT INDAH'),
            ('API-API', 'API-API'),
            ('BONTANG BARU', 'BONTANG BARU'),
            ('BONTANG KUALA', 'BONTANG KUALA'),
            ('GUNTUNG', 'GUNTUNG'),
            ('GUNUNG ELAI', 'GUNUNG ELAI'),
            ('LOK TUAN', 'LOK TUAN'),
        )
        widgets = {
            # 'judul': forms.TextInput({'class': 'form-control'}),
            # 'penulis': forms.TextInput({'class': 'form-control'}),
            # 'penerbit': forms.TextInput({'class': 'form-control'}),
            # 'jumlah': forms.NumberInput({'class': 'form-control'}),
            # 'kelompok_id': forms.Select({'class': 'form-control'}),
            'nama_dpt': forms.TextInput({'class': 'form-control'}),
            'kota': forms.Select({'class': 'form-control'}, choices=pilihankota),
            'kecamatan': forms.Select({'class': 'form-control'}, choices=pilihankecamatan),
            'kelurahan': forms.Select({'class': 'form-control'}, choices=pilihankelurahan),
            'alamat': forms.TextInput({'class': 'form-control'}),
            'nik': forms.NumberInput({'class': 'form-control'}),
            'nomor_hp': forms.NumberInput({'class': 'form-control'}),
            'nomor_rekening': forms.NumberInput({'class': 'form-control'}),
            'nomor_kk': forms.NumberInput({'class': 'form-control'}),
            'tanggal_lahir': forms.DateInput({'class': 'form-control', 'type': 'date'}),
            'tanggal_input_data': forms.DateInput({'class': 'form-control', 'type': 'date'}),
            'tanggal_honor': forms.DateInput({'class': 'form-control', 'type': 'date'}),
            'tanggal_telespocheck': forms.DateInput({'class': 'form-control', 'type': 'date'}),
            'rt': forms.NumberInput({'class': 'form-control'}),
            'nominal_honor': forms.NumberInput({'class': 'form-control'}),
            'bank': forms.TextInput({'class': 'form-control'}),
            'status_telespocheck': forms.Select({'class': 'form-control'}),
            'keterangan_telespocheck': forms.TextInput({'class': 'form-control'}),
            'telespochecker': forms.Select({'class': 'form-control'}),
            'hasil_telespocheck': forms.Select({'class': 'form-control'}),
            'keterangan': forms.TextInput({'class': 'form-control'}),
            'nama_pemilik_rekening': forms.TextInput({'class': 'form-control'}),
            'inputer': forms.Select({'class': 'form-control'}),
            'keterangan_honor': forms.TextInput({'class': 'form-control'}),
        }
