from django.shortcuts import render, redirect, HttpResponse
from paser.models import Paser
from paser.forms import FormPaser
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from paser.resource import PaserResource


@login_required(login_url=settings.LOGIN_URL)
def index(request):
    return render(request, 'paser/index.html')


@login_required(login_url=settings.LOGIN_URL)
def export_xls(request):
    paser = PaserResource()
    dataset = paser.export()
    response = HttpResponse(
        dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Data DPT.xls"'
    return response


@login_required(login_url=settings.LOGIN_URL)
def hapus_paser(request, id_paser):
    paser = Paser.objects.filter(id=id_paser)
    paser.delete()

    messages.success(request, "Data Berhasil dihapus")
    return redirect('paser')


@login_required(login_url=settings.LOGIN_URL)
def ubah_paser(request, id_paser):
    paser = Paser.objects.get(id=id_paser)
    template = 'paser/ubah-paser.html'
    if request.POST:
        form = FormPaser(request.POST, request.FILES, instance=paser)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Data Telah Berhasil diperbaharui")
            return redirect('paser')
        else:
            form = FormPaser(instance=paser)
            messages.success(
                request, "Terdapat kesalahan pada saat penginputan, Pastikan format Tanggal benar ! ")
            error = "Terdapat kesalahan pada saat penginputan, Pastikan format Tanggal benar !"
            konteks = {
                'form': form,
                'paser': paser,
                'error': error,
            }
            return render(request, template, konteks)
    else:
        form = FormPaser(instance=paser)
        konteks = {
            'form': form,
            'paser': paser,
        }
        return render(request, template, konteks)


@login_required
def paser(request):
    paserr = Paser.objects.all()
    konteks = {
        'paserr': paserr,
    }
    return render(request, 'paser/paser.html', konteks)


@login_required(login_url=settings.LOGIN_URL)
def tambah_paser(request):
    if request.POST:
        form = FormPaser(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormPaser()
            pesan = "Data berhasil disimpan ke List DPT"
            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'paser/tambah-paser.html', konteks)
        else:
            error = "Terdapat kesalahan, periksa kembali Format Inputan dan wajib mengisi kolom bertanda (*) !"
            konteks = {
                'form': form,
                'error': error,
            }
            return render(request, 'paser/tambah-paser.html', konteks)
    else:
        form = FormPaser()
        konteks = {
            'form': form,
        }

    return render(request, 'paser/tambah-paser.html', konteks)
