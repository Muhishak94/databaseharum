from django.shortcuts import render, redirect, HttpResponse
from bontang.models import Bontang
from bontang.forms import FormBontang
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from bontang.resource import BontangResource


@login_required(login_url=settings.LOGIN_URL)
def index(request):
    return render(request, 'bontang/index.html')


@login_required(login_url=settings.LOGIN_URL)
def export_xls(request):
    bontang = BontangResource()
    dataset = bontang.export()
    response = HttpResponse(
        dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Data DPT.xls"'
    return response


@login_required(login_url=settings.LOGIN_URL)
def hapus_bontang(request, id_bontang):
    bontang = Bontang.objects.filter(id=id_bontang)
    bontang.delete()

    messages.success(request, "Data Berhasil dihapus")
    return redirect('bontang')


@login_required(login_url=settings.LOGIN_URL)
def ubah_bontang(request, id_bontang):
    bontang = Bontang.objects.get(id=id_bontang)
    template = 'bontang/ubah-bontang.html'
    if request.POST:
        form = FormBontang(request.POST, request.FILES, instance=bontang)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Data Telah Berhasil diperbaharui")
            return redirect('bontang')
        else:
            form = FormBontang(instance=bontang)
            messages.success(
                request, "Terdapat kesalahan pada saat penginputan, Pastikan format Tanggal benar ! ")
            error = "Terdapat kesalahan pada saat penginputan, Pastikan format Tanggal benar !"
            konteks = {
                'form': form,
                'bontang': bontang,
                'error': error,
            }
            return render(request, template, konteks)
    else:
        form = FormBontang(instance=bontang)
        konteks = {
            'form': form,
            'bontang': bontang,
        }
        return render(request, template, konteks)


@login_required
def bontang(request):
    bontangg = Bontang.objects.all()
    konteks = {
        'bontangg': bontangg,
    }
    return render(request, 'bontang/bontang.html', konteks)


@login_required(login_url=settings.LOGIN_URL)
def tambah_bontang(request):
    if request.POST:
        form = FormBontang(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormBontang()
            pesan = "Data berhasil disimpan ke List DPT"
            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'bontang/tambah-bontang.html', konteks)
        else:
            error = "Terdapat kesalahan, periksa kembali Format Inputan dan wajib mengisi kolom bertanda (*) !"
            konteks = {
                'form': form,
                'error': error,
            }
            return render(request, 'bontang/tambah-bontang.html', konteks)
    else:
        form = FormBontang()
        konteks = {
            'form': form,
        }

    return render(request, 'bontang/tambah-bontang.html', konteks)
