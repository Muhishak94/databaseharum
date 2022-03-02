from django.shortcuts import render, redirect, HttpResponse
from balikpapan.models import Balikpapan
from balikpapan.forms import FormBalikpapan
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from balikpapan.resource import BalikpapanResource


@login_required(login_url=settings.LOGIN_URL)
def index(request):
    return render(request, 'balikpapan/index.html')


@login_required(login_url=settings.LOGIN_URL)
def export_xls(request):
    balikpapan = BalikpapanResource()
    dataset = balikpapan.export()
    response = HttpResponse(
        dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Data DPT.xls"'
    return response


@login_required(login_url=settings.LOGIN_URL)
def hapus_balikpapan(request, id_balikpapan):
    balikpapan = Balikpapan.objects.filter(id=id_balikpapan)
    balikpapan.delete()

    messages.success(request, "Data Berhasil dihapus")
    return redirect('balikpapan')


@login_required(login_url=settings.LOGIN_URL)
def ubah_balikpapan(request, id_balikpapan):
    balikpapan = Balikpapan.objects.get(id=id_balikpapan)
    template = 'balikpapan/ubah-balikpapan.html'
    if request.POST:
        form = FormBalikpapan(request.POST, request.FILES, instance=balikpapan)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Data Telah Berhasil diperbaharui")
            return redirect('balikpapan')
        else:
            form = FormBalikpapan(instance=balikpapan)
            messages.success(
                request, "Terdapat kesalahan pada saat penginputan, Pastikan format Tanggal benar ! ")
            error = "Terdapat kesalahan pada saat penginputan, Pastikan format Tanggal benar !"
            konteks = {
                'form': form,
                'balikpapan': balikpapan,
                'error': error,
            }
            return render(request, template, konteks)
    else:
        form = FormBalikpapan(instance=balikpapan)
        konteks = {
            'form': form,
            'balikpapan': balikpapan,
        }
        return render(request, template, konteks)


@login_required
def balikpapan(request):
    balikpapann = Balikpapan.objects.all()
    konteks = {
        'balikpapann': balikpapann,
    }
    return render(request, 'balikpapan/balikpapan.html', konteks)


@login_required(login_url=settings.LOGIN_URL)
def tambah_balikpapan(request):
    if request.POST:
        form = FormBalikpapan(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormBalikpapan()
            pesan = "Data berhasil disimpan ke List DPT"
            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'balikpapan/tambah-balikpapan.html', konteks)
        else:
            error = "Terdapat kesalahan, periksa kembali Format Inputan dan wajib mengisi kolom bertanda (*) !"
            konteks = {
                'form': form,
                'error': error,
            }
            return render(request, 'balikpapan/tambah-balikpapan.html', konteks)
    else:
        form = FormBalikpapan()
        konteks = {
            'form': form,
        }

    return render(request, 'balikpapan/tambah-balikpapan.html', konteks)
