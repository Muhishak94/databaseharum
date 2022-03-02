from django.shortcuts import render, redirect, HttpResponse
from samarinda.models import Samarinda
from samarinda.forms import FormSamarinda
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from samarinda.resource import SamarindaResource


@login_required(login_url=settings.LOGIN_URL)
def index(request):
    return render(request, 'samarinda/index.html')


@login_required(login_url=settings.LOGIN_URL)
def export_xls(request):
    samarinda = SamarindaResource()
    dataset = samarinda.export()
    response = HttpResponse(
        dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Data DPT.xls"'
    return response


@login_required(login_url=settings.LOGIN_URL)
def hapus_samarinda(request, id_samarinda):
    samarinda = Samarinda.objects.filter(id=id_samarinda)
    samarinda.delete()

    messages.success(request, "Data Berhasil dihapus")
    return redirect('samarinda')


@login_required(login_url=settings.LOGIN_URL)
def ubah_samarinda(request, id_samarinda):
    samarinda = Samarinda.objects.get(id=id_samarinda)
    template = 'samarinda/ubah-samarinda.html'
    if request.POST:
        form = FormSamarinda(request.POST, request.FILES, instance=samarinda)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Data Telah Berhasil diperbaharui")
            return redirect('samarinda')
        else:
            form = FormSamarinda(instance=samarinda)
            messages.success(
                request, "Terdapat kesalahan pada saat penginputan, Pastikan format Tanggal benar ! ")
            error = "Terdapat kesalahan pada saat penginputan, Pastikan format Tanggal benar !"
            konteks = {
                'form': form,
                'samarinda': samarinda,
                'error': error,
            }
            return render(request, template, konteks)
    else:
        form = FormSamarinda(instance=samarinda)
        konteks = {
            'form': form,
            'samarinda': samarinda,
        }
        return render(request, template, konteks)


@login_required
def samarinda(request):
    samarindaa = Samarinda.objects.all()
    konteks = {
        'samarindaa': samarindaa,
    }
    return render(request, 'samarinda/samarinda.html', konteks)


@login_required(login_url=settings.LOGIN_URL)
def tambah_samarinda(request):
    if request.POST:
        form = FormSamarinda(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormSamarinda()
            pesan = "Data berhasil disimpan ke List DPT"
            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'samarinda/tambah-samarinda.html', konteks)
        else:
            error = "Terdapat kesalahan, periksa kembali Format Inputan dan wajib mengisi kolom bertanda (*) !"
            konteks = {
                'form': form,
                'error': error,
            }
            return render(request, 'samarinda/tambah-samarinda.html', konteks)
    else:
        form = FormSamarinda()
        konteks = {
            'form': form,
        }

    return render(request, 'samarinda/tambah-samarinda.html', konteks)
