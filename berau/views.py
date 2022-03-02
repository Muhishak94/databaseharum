from django.shortcuts import render, redirect, HttpResponse
from berau.models import Berau
from berau.forms import FormBerau
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from berau.resource import BerauResource


@login_required(login_url=settings.LOGIN_URL)
def index(request):
    return render(request, 'berau/index.html')


@login_required(login_url=settings.LOGIN_URL)
def export_xls(request):
    berau = BerauResource()
    dataset = berau.export()
    response = HttpResponse(
        dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Data DPT.xls"'
    return response


@login_required(login_url=settings.LOGIN_URL)
def hapus_berau(request, id_berau):
    berau = Berau.objects.filter(id=id_berau)
    berau.delete()

    messages.success(request, "Data Berhasil dihapus")
    return redirect('berau')


@login_required(login_url=settings.LOGIN_URL)
def ubah_berau(request, id_berau):
    berau = Berau.objects.get(id=id_berau)
    template = 'berau/ubah-berau.html'
    if request.POST:
        form = FormBerau(request.POST, request.FILES, instance=berau)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Data Telah Berhasil diperbaharui")
            return redirect('berau')
        else:
            form = FormBerau(instance=berau)
            messages.success(
                request, "Terdapat kesalahan pada saat penginputan, Pastikan format Tanggal benar ! ")
            error = "Terdapat kesalahan pada saat penginputan, Pastikan format Tanggal benar !"
            konteks = {
                'form': form,
                'berau': berau,
                'error': error,
            }
            return render(request, template, konteks)
    else:
        form = FormBerau(instance=berau)
        konteks = {
            'form': form,
            'berau': berau,
        }
        return render(request, template, konteks)


@login_required
def berau(request):
    berauu = Berau.objects.all()
    konteks = {
        'berauu': berauu,
    }
    return render(request, 'berau/berau.html', konteks)


@login_required(login_url=settings.LOGIN_URL)
def tambah_berau(request):
    if request.POST:
        form = FormBerau(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormBerau()
            pesan = "Data berhasil disimpan ke List DPT"
            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'berau/tambah-berau.html', konteks)
        else:
            error = "Terdapat kesalahan, periksa kembali Format Inputan dan wajib mengisi kolom bertanda (*) !"
            konteks = {
                'form': form,
                'error': error,
            }
            return render(request, 'berau/tambah-berau.html', konteks)
    else:
        form = FormBerau()
        konteks = {
            'form': form,
        }

    return render(request, 'berau/tambah-berau.html', konteks)
