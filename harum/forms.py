from django.forms import ModelForm
from harum.models import Database
from django import forms


class FormDatabase(ModelForm):
    class Meta:
        model = Database
        fields = '__all__'

        widgets = {
            'nama_dpt': forms.TextInput({'class': 'form-control'}),
            'kota': forms.Select({'class': 'form-control'}),
            'kecamatan': forms.Select({'class': 'form-control'}),
            'kelurahan': forms.Select({'class': 'form-control'}),
            'alamat': forms.TextInput({'class': 'form-control'}),
            'nik': forms.NumberInput({'class': 'form-control'}),
            'nomor_hp': forms.NumberInput({'class': 'form-control'}),
            'nomor_rekening': forms.NumberInput({'class': 'form-control'}),
            'nomor_kk': forms.NumberInput({'class': 'form-control'}),
            'tanggal_lahir': forms.DateInput({'class': 'form-control'}),
            'tanggal_input_data': forms.DateInput({'class': 'form-control'}),
            'tanggal_honor': forms.DateInput({'class': 'form-control'}),
            'tanggal_telespocheck': forms.DateInput({'class': 'form-control'}),
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
