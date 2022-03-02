from django.shortcuts import render, redirect, HttpResponse
from kukar.models import Kukar
from kukar.forms import FormKukar
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from kukar.resource import KukarResource


@login_required(login_url=settings.LOGIN_URL)
def index(request):
    return render(request, 'kukar/index.html')


@login_required(login_url=settings.LOGIN_URL)
def export_xls(request):
    kukar = KukarResource()
    dataset = kukar.export()
    response = HttpResponse(
        dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Data DPT.xls"'
    return response


@login_required(login_url=settings.LOGIN_URL)
def hapus_kukar(request, id_kukar):
    kukar = Kukar.objects.filter(id=id_kukar)
    kukar.delete()

    messages.success(request, "Data Berhasil dihapus")
    return redirect('kukar')


@login_required(login_url=settings.LOGIN_URL)
def ubah_kukar(request, id_kukar):
    kukar = Kukar.objects.get(id=id_kukar)
    template = 'kukar/ubah-kukar.html'
    if request.POST:
        form = FormKukar(request.POST, request.FILES, instance=kukar)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Data Telah Berhasil diperbaharui")
            return redirect('kukar')
        else:
            form = FormKukar(instance=kukar)
            messages.success(
                request, "Terdapat kesalahan pada saat penginputan, Pastikan format Tanggal benar ! ")
            error = "Terdapat kesalahan pada saat penginputan, Pastikan format Tanggal benar !"
            konteks = {
                'form': form,
                'kukar': kukar,
                'error': error,
            }
            return render(request, template, konteks)
    else:
        form = FormKukar(instance=kukar)
        konteks = {
            'form': form,
            'kukar': kukar,
        }
        return render(request, template, konteks)


@login_required
def kukar(request):
    kukarr = Kukar.objects.all()
    konteks = {
        'kukarr': kukarr,
    }
    return render(request, 'kukar/kukar.html', konteks)


@login_required(login_url=settings.LOGIN_URL)
def tambah_kukar(request):
    if request.POST:
        form = FormKukar(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormKukar()
            pesan = "Data berhasil disimpan ke List DPT"
            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'kukar/tambah-kukar.html', konteks)
        else:
            error = "Terdapat kesalahan, periksa kembali Format Inputan dan wajib mengisi kolom bertanda (*) !"
            konteks = {
                'form': form,
                'error': error,
            }
            return render(request, 'kukar/tambah-kukar.html', konteks)
    else:
        form = FormKukar()
        konteks = {
            'form': form,
        }

    return render(request, 'kukar/tambah-kukar.html', konteks)
