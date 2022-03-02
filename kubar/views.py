from django.shortcuts import render, redirect, HttpResponse
from kubar.models import Kubar
from kubar.forms import FormKubar
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from kubar.resource import KubarResource


@login_required(login_url=settings.LOGIN_URL)
def index(request):
    return render(request, 'kubar/index.html')


@login_required(login_url=settings.LOGIN_URL)
def export_xls(request):
    kubar = KubarResource()
    dataset = kubar.export()
    response = HttpResponse(
        dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Data DPT.xls"'
    return response


@login_required(login_url=settings.LOGIN_URL)
def hapus_kubar(request, id_kubar):
    kubar = Kubar.objects.filter(id=id_kubar)
    kubar.delete()

    messages.success(request, "Data Berhasil dihapus")
    return redirect('kubar')


@login_required(login_url=settings.LOGIN_URL)
def ubah_kubar(request, id_kubar):
    kubar = Kubar.objects.get(id=id_kubar)
    template = 'kubar/ubah-kubar.html'
    if request.POST:
        form = FormKubar(request.POST, request.FILES, instance=kubar)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Data Telah Berhasil diperbaharui")
            return redirect('kubar')
        else:
            form = FormKubar(instance=kubar)
            messages.success(
                request, "Terdapat kesalahan pada saat penginputan, Pastikan format Tanggal benar ! ")
            error = "Terdapat kesalahan pada saat penginputan, Pastikan format Tanggal benar !"
            konteks = {
                'form': form,
                'kubar': kubar,
                'error': error,
            }
            return render(request, template, konteks)
    else:
        form = FormKubar(instance=kubar)
        konteks = {
            'form': form,
            'kubar': kubar,
        }
        return render(request, template, konteks)


@login_required
def kubar(request):
    kubarr = Kubar.objects.all()
    konteks = {
        'kubarr': kubarr,
    }
    return render(request, 'kubar/kubar.html', konteks)


@login_required(login_url=settings.LOGIN_URL)
def tambah_kubar(request):
    if request.POST:
        form = FormKubar(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormKubar()
            pesan = "Data berhasil disimpan ke List DPT"
            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'kubar/tambah-kubar.html', konteks)
        else:
            error = "Terdapat kesalahan, periksa kembali Format Inputan dan wajib mengisi kolom bertanda (*) !"
            konteks = {
                'form': form,
                'error': error,
            }
            return render(request, 'kubar/tambah-kubar.html', konteks)
    else:
        form = FormKubar()
        konteks = {
            'form': form,
        }

    return render(request, 'kubar/tambah-kubar.html', konteks)
