from django.forms import ModelForm
from django import forms
from balikpapan.models import Balikpapan


class FormBalikpapan(ModelForm):
    class Meta:
        model = Balikpapan
        fields = '__all__'
        pilihankota = (
            ('BALIKPAPAN', 'BALIKPAPAN'),
        )
        pilihankecamatan = (
            ('', ''),
            ('BALIKPAPAN BARAT', 'BALIKPAPAN BARAT'),
            ('BALIKPAPAN KOTA', 'BALIKPAPAN KOTA'),
            ('BALIKPAPAN SELATAN', 'BALIKPAPAN SELATAN'),
            ('BALIKPAPAN TENGAH', 'BALIKPAPAN TENGAH'),
            ('BALIKPAPAN TIMUR', 'BALIKPAPAN TIMUR'),
            ('BALIKPAPAN UTARA', 'BALIKPAPAN UTARA'),

        )
        pilihankelurahan = (
            ('', ''),
            ('BARU ILIR', 'BARU ILIR'),
            ('BARU TENGAH', 'BARU TENGAH'),
            ('BARU ULU', 'BARU ULU'),
            ('KARIANGAU', 'KARIANGAU'),
            ('MARGA SARI', 'MARGA SARI'),
            ('MARGO MULYO', 'MARGO MULYO'),
            ('DAMAI', 'DAMAI'),
            ('KLANDASAN ILIR', 'KLANDASAN ILIR'),
            ('KLANDASAN ULU', 'KLANDASAN ULU'),
            ('PRAPATAN', 'PRAPATAN'),
            ('TELAGA SARI', 'TELAGA SARI'),
            ('DAMAI BAHAGIA', 'DAMAI BAHAGIA'),
            ('DAMAI BARU', 'DAMAI BARU'),
            ('GUNUNG BAHAGIA', 'GUNUNG BAHAGIA'),
            ('SEPINGGAN', 'SEPINGGAN'),
            ('SEPINGGAN BARU', 'SEPINGGAN BARU'),
            ('SEPINGGAN RAYA', 'SEPINGGAN RAYA'),
            ('SUNGAI NANGKA', 'SUNGAI NANGKA'),
            ('GUNUNG SARI ILIR', 'GUNUNG SARI ILIR'),
            ('GUNUNG SARI ULU', 'GUNUNG SARI ULU'),
            ('KARANG JATI', 'KARANG JATI'),
            ('KARANG REJO', 'KARANG REJO'),
            ('MEKAR SARI', 'MEKAR SARI'),
            ('SUMBER REJO', 'SUMBER REJO'),
            ('LAMARU', 'LAMARU'),
            ('MANGGAR', 'MANGGAR'),
            ('MANGGAR BARU', 'MANGGAR BARU'),
            ('TERITIP', 'TERITIP'),
            ('BATU AMPAR', 'BATU AMPAR'),
            ('GRAHA INDAH', 'GRAHA INDAH'),
            ('GUNUNG SAMARINDA', 'GUNUNG SAMARINDA'),
            ('GUNUNGSAMARINDA BARU', 'GUNUNGSAMARINDA BARU'),
            ('KARANG JOANG', 'KARANG JOANG'),
            ('MUARARAPAK', 'MUARARAPAK'),

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
