from django.shortcuts import render, redirect, HttpResponse
from mahulu.models import Mahulu
from mahulu.forms import FormMahulu
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from mahulu.resource import MahuluResource


@login_required(login_url=settings.LOGIN_URL)
def index(request):
    return render(request, 'mahulu/index.html')


@login_required(login_url=settings.LOGIN_URL)
def export_xls(request):
    mahulu = MahuluResource()
    dataset = mahulu.export()
    response = HttpResponse(
        dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Data DPT.xls"'
    return response


@login_required(login_url=settings.LOGIN_URL)
def hapus_mahulu(request, id_mahulu):
    mahulu = Mahulu.objects.filter(id=id_mahulu)
    mahulu.delete()

    messages.success(request, "Data Berhasil dihapus")
    return redirect('mahulu')


@login_required(login_url=settings.LOGIN_URL)
def ubah_mahulu(request, id_mahulu):
    mahulu = Mahulu.objects.get(id=id_mahulu)
    template = 'mahulu/ubah-mahulu.html'
    if request.POST:
        form = FormMahulu(request.POST, request.FILES, instance=mahulu)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Data Telah Berhasil diperbaharui")
            return redirect('mahulu')
        else:
            form = FormMahulu(instance=mahulu)
            messages.success(
                request, "Terdapat kesalahan pada saat penginputan, Pastikan format Tanggal benar ! ")
            error = "Terdapat kesalahan pada saat penginputan, Pastikan format Tanggal benar !"
            konteks = {
                'form': form,
                'mahulu': mahulu,
                'error': error,
            }
            return render(request, template, konteks)
    else:
        form = FormMahulu(instance=mahulu)
        konteks = {
            'form': form,
            'mahulu': mahulu,
        }
        return render(request, template, konteks)


@login_required
def mahulu(request):
    mahuluu = Mahulu.objects.all()
    konteks = {
        'mahuluu': mahuluu,
    }
    return render(request, 'mahulu/mahulu.html', konteks)


@login_required(login_url=settings.LOGIN_URL)
def tambah_mahulu(request):
    if request.POST:
        form = FormMahulu(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormMahulu()
            pesan = "Data berhasil disimpan ke List DPT"
            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'mahulu/tambah-mahulu.html', konteks)
        else:
            error = "Terdapat kesalahan, periksa kembali Format Inputan dan wajib mengisi kolom bertanda (*) !"
            konteks = {
                'form': form,
                'error': error,
            }
            return render(request, 'mahulu/tambah-mahulu.html', konteks)
    else:
        form = FormMahulu()
        konteks = {
            'form': form,
        }

    return render(request, 'mahulu/tambah-mahulu.html', konteks)
