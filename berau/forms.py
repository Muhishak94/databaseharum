from django.forms import ModelForm
from django import forms
from berau.models import Berau


class FormBerau(ModelForm):
    class Meta:
        model = Berau
        fields = '__all__'
        pilihankota = (
            ('BERAU', 'BERAU'),
        )
        pilihankecamatan = (
            ('', ''),
            ('BATU PUTIH', 'BATU PUTIH'),
            ('BIATAN', 'BIATAN'),
            ('BIDUK-BIDUK', 'BIDUK-BIDUK'),
            ('GUNUNG TABUR', 'GUNUNG TABUR'),
            ('KELAY', 'KELAY'),
            ('MARATUA', 'MARATUA'),
            ('PULAU DERAWAN', 'PULAU DERAWAN'),
            ('SAMBALIUNG', 'SAMBALIUNG'),
            ('SEGAH', 'SEGAH'),
            ('TABALAR', 'TABALAR'),
            ('TALISAYAN', 'TALISAYAN'),
            ('TANJUNG REDEB', 'TANJUNG REDEB'),
            ('TELUK BAYUR', 'TELUK BAYUR'),
        )
        pilihankelurahan = (
            ('', ''),
            ('AMPEN MEDANG', 'AMPEN MEDANG'),
            ('BALIKUKUP', 'BALIKUKUP'),
            ('BATU PUTIH', 'BATU PUTIH'),
            ('KAYU INDAH', 'KAYU INDAH'),
            ('LOBANG KELATAK', 'LOBANG KELATAK'),
            ('SUMBER AGUNG', 'SUMBER AGUNG'),
            ('TEMBUDAN', 'TEMBUDAN'),
            ('BIATAN BAPINANG', 'BIATAN BAPINANG'),
            ('BIATAN BARU', 'BIATAN BARU'),
            ('BIATAN ILIR', 'BIATAN ILIR'),
            ('BIATAN LEMPAKE', 'BIATAN LEMPAKE'),
            ('BIATAN ULU', 'BIATAN ULU'),
            ('BUKIT MAKMUR JAYA', 'BUKIT MAKMUR JAYA'),
            ('KARANGAN', 'KARANGAN'),
            ('BIDUK-BIDUK', 'BIDUK-BIDUK'),
            ('GIRING-GIRING', 'GIRING-GIRING'),
            ('PANTAI HARAPAN', 'PANTAI HARAPAN'),
            ('TANJUNG PREPAT', 'TANJUNG PREPAT'),
            ('TELUK SULAIMAN', 'TELUK SULAIMAN'),
            ('TELUK SUMBANG', 'TELUK SUMBANG'),
            ('BATU-BATU', 'BATU-BATU'),
            ('BIRANG', 'BIRANG'),
            ('GUNUNG TABUR', 'GUNUNG TABUR'),
            ('MALUANG', 'MALUANG'),
            ('MELATI JAYA', 'MELATI JAYA'),
            ('MERANCANG ILIR', 'MERANCANG ILIR'),
            ('MERANCANG ULU', 'MERANCANG ULU'),
            ('PULAU BESING', 'PULAU BESING'),
            ('SAMBAKUNGAN', 'SAMBAKUNGAN'),
            ('SAMBURAKAT', 'SAMBURAKAT'),
            ('TASUK', 'TASUK'),
            ('LESAN DAYAK', 'LESAN DAYAK'),
            ('LONG BELIU', 'LONG BELIU'),
            ('LONG DUHUNG', 'LONG DUHUNG'),
            ('LONG KELUH', 'LONG KELUH'),
            ('LONG LAMCIN', 'LONG LAMCIN'),
            ('LONG PELAY', 'LONG PELAY'),
            ('LONG SULUI', 'LONG SULUI'),
            ('MAPULU', 'MAPULU'),
            ('MERABU', 'MERABU'),
            ('MERAPUN', 'MERAPUN'),
            ('MERASA', 'MERASA'),
            ('MUARA LESAN', 'MUARA LESAN'),
            ('PANAAN', 'PANAAN'),
            ('SIDO BANGEN', 'SIDO BANGEN'),
            ('MARATUA BOHESILLAN', 'MARATUA BOHESILLAN'),
            ('MARATUA PAYUNG-PAYUNG', 'MARATUA PAYUNG-PAYUNG'),
            ('MARATUA TELUK ALULU', 'MARATUA TELUK ALULU'),
            ('MARATUA TELUK HARAPAN', 'MARATUA TELUK HARAPAN'),
            ('KASAI', 'KASAI'),
            ('PEGAT BETUMBUK', 'PEGAT BETUMBUK'),
            ('PULAU DERAWAN', 'PULAU DERAWAN'),
            ('TELUK SEMANTING', 'TELUK SEMANTING'),
            ('BENA BARU', 'BENA BARU'),
            ('GURIMBANG', 'GURIMBANG'),
            ('INARAN', 'INARAN'),
            ('LONG LANUK', 'LONG LANUK'),
            ('PEGAT BUKUR', 'PEGAT BUKUR'),
            ('PESAYAN/MENGKAJANG', 'PESAYAN/MENGKAJANG'),
            ('PILANJAU', 'PILANJAU'),
            ('RANTAU PANJANG', 'RANTAU PANJANG'),
            ('SAMBALIUNG', 'SAMBALIUNG'),
            ('SEI BEBANIR BANGUN', 'SEI BEBANIR BANGUN'),
            ('SUARAN', 'SUARAN'),
            ('SUKAN TENGAH', 'SUKAN TENGAH'),
            ('TANJUNG PERANGAT', 'TANJUNG PERANGAT'),
            ('TUMBIK DAYAT', 'TUMBIK DAYAT'),
            ('BATU RAJANG', 'BATU RAJANG'),
            ('BUKIT MAKMUR', 'BUKIT MAKMUR'),
            ('HARAPAN JAYA', 'HARAPAN JAYA'),
            ('LONG AYAN', 'LONG AYAN'),
            ('LONG AYAP', 'LONG AYAP'),
            ('LONG LA AI', 'LONG LA AI'),
            ('PANDAN SARI', 'PANDAN SARI'),
            ('PUNAH SEGAH', 'PUNAH SEGAH'),
            ('PUNAN MAHAKAM', 'PUNAN MAHAKAM'),
            ('PUNAN MALINAU', 'PUNAN MALINAU'),
            ('SIDUUNG INDAH', 'SIDUUNG INDAH'),
            ('TEPIAN BUAH', 'TEPIAN BUAH'),
            ('BAMBANGAN/TUBAAN', 'BAMBANGAN/TUBAAN'),
            ('BUYUNG BUYUNG', 'BUYUNG BUYUNG'),
            ('HARAPAN MAJU', 'HARAPAN MAJU'),
            ('SEMURU', 'SEMURU'),
            ('TABALAR MUARA', 'TABALAR MUARA'),
            ('TABALAR ULU', 'TABALAR ULU'),
            ('BUMU JAYA', 'BUMU JAYA'),
            ('CAMPUR SARI', 'CAMPUR SARI'),
            ('CAPUAK', 'CAPUAK'),
            ('DUMARING', 'DUMARING'),
            ('EKA SAPTA', 'EKA SAPTA'),
            ('PURNASARI JAYA', 'PURNASARI JAYA'),
            ('SUKA MURYA', 'SUKA MURYA'),
            ('SUMBER MULYA', 'SUMBER MULYA'),
            ('TALISAYAN', 'TALISAYAN'),
            ('TUNGGAL BUMI', 'TUNGGAL BUMI'),
            ('GAYAM', 'GAYAM'),
            ('KARANG AMBUN', 'KARANG AMBUN'),
            ('SUNGAI BEDUNGUN', 'SUNGAI BEDUNGUN'),
            ('TENJUNG REDEB', 'TENJUNG REDEB'),
            ('LABANAN JAYA', 'LABANAN JAYA'),
            ('LABANAN MAKARTI', 'LABANAN MAKARTI'),
            ('LABANAN MAKMUR', 'LABANAN MAKMUR'),
            ('RINDING', 'RINDING'),
            ('TELUK BAYUR', 'TELUK BAYUR'),
            ('TUMBIT MELAYU', 'TUMBIT MELAYU'),

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
