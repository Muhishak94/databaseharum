from django.forms import ModelForm
from django import forms
from mahulu.models import Mahulu


class FormMahulu(ModelForm):
    class Meta:
        model = Mahulu
        fields = '__all__'
        pilihankota = (
            ('MAHAKAM ULU', 'MAHAKAM ULU'),
        )
        pilihankecamatan = (
            ('', ''),
            ('LAHAM', 'LAHAM'),
            ('LONG APARI', 'LONG APARI'),
            ('LONG BAGUN', 'LONG BAGUN'),
            ('LONG HUBUNG', 'LONG HUBUNG'),
            ('LONG PAHANGAI', 'LONG PAHANGAI'),
        )
        pilihankelurahan = (
            ('', ''),
            ('DANUM PAROY', 'DANUM PAROY'),
            ('LAHAM', 'LAHAM'),
            ('LONG GELAWANG', 'LONG GELAWANG'),
            ('MUARA RATAH', 'MUARA RATAH'),
            ('NYARIBUNGAN', 'NYARIBUNGAN'),
            ('LONG APARI', 'LONG APARI'),
            ('LONG KERIOQ', 'LONG KERIOQ'),
            ('LONG PENANEH I', 'LONG PENANEH I'),
            ('LONG PENANEH II', 'LONG PENANEH II'),
            ('LONG PENANEH III', 'LONG PENANEH III'),
            ('NAHA BUAN', 'NAHA BUAN'),
            ('NAHA SILAT', 'NAHA SILAT'),
            ('NAHA TIFAB', 'NAHA TIFAB'),
            ("TIONG BU'U", "TIONG BU'U"),
            ('TIONG OHANG', 'TIONG OHANG'),
            ('BATOQ KELO', 'BATOQ KELO'),
            ('BATU MAJANG', 'BATU MAJANG'),
            ('LONG BAGUN ILIR', 'LONG BAGUN ILIR'),
            ('LONG BAGUN ULU', 'LONG BAGUN ULU'),
            ('LONG HURAI', 'LONG HURAI'),
            ('LONG MELAHAM', 'LONG MELAHAM'),
            ('LONG MERAH', 'LONG MERAH'),
            ('MEMAHAK BESAR', 'MEMAHAK BESAR'),
            ('MEMAHAK ULU', 'MEMAHAK ULU'),
            ('RUKUN DAMAI', 'RUKUN DAMAI'),
            ('UJOH BILANG', 'UJOH BILANG'),
            ('DATAH BILANG BARU', 'DATAH BILANG BARU'),
            ('DATAH BILANG ILIR', 'DATAH BILANG ILIR'),
            ('DATAH BILANG ULU', 'DATAH BILANG ULU'),
            ('LONG HUBUNG', 'LONG HUBUNG'),
            ('LONG HUBUNG ULU', 'LONG HUBUNG ULU'),
            ('LUTAN', 'LUTAN'),
            ('MATALIBAQ', 'MATALIBAQ'),
            ('MEMAHAK TEBOQ', 'MEMAHAK TEBOQ'),
            ('SIRAU', 'SIRAU'),
            ('TRI PARIQ MAKMUR', 'TRI PARIQ MAKMUR'),
            ('WANA PARIQ', 'WANA PARIQ'),
            ('DATAH NAHA', 'DATAH NAHA'),
            ('DELANG KEROHONG', 'DELANG KEROHONG'),
            ('LIRUNG UBING', 'LIRUNG UBING'),
            ('LIU MULANG', 'LIU MULANG'),
            ('LONG ISUN', 'LONG ISUN'),
            ('LONG LUNUK', 'LONG LUNUK'),
            ('LONG LUNUK BARU', 'LONG LUNUK BARU'),
            ('LONG PAHANGAI I', 'LONG PAHANGAI I'),
            ('LONG PAHANGAI II', 'LONG PAHANGAI II'),
            ('LONG PAKAQ', 'LONG PAKAQ'),
            ('LONG PAKAQ BARU', 'LONG PAKAQ BARU'),
            ('LONG TUYOQ', 'LONG TUYOQ'),
            ('NAHA ARU', 'NAHA ARU'),
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
