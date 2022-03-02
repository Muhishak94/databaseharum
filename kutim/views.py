from django.shortcuts import render, redirect, HttpResponse
from kutim.models import Kutim
from kutim.forms import FormKutim
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from kutim.resource import KutimResource


@login_required(login_url=settings.LOGIN_URL)
def index(request):
    return render(request, 'kutim/index.html')


@login_required(login_url=settings.LOGIN_URL)
def export_xls(request):
    kutim = KutimResource()
    dataset = kutim.export()
    response = HttpResponse(
        dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Data DPT.xls"'
    return response


@login_required(login_url=settings.LOGIN_URL)
def hapus_kutim(request, id_kutim):
    kutim = Kutim.objects.filter(id=id_kutim)
    kutim.delete()

    messages.success(request, "Data Berhasil dihapus")
    return redirect('kutim')


@login_required(login_url=settings.LOGIN_URL)
def ubah_kutim(request, id_kutim):
    kutim = Kutim.objects.get(id=id_kutim)
    template = 'kutim/ubah-kutim.html'
    if request.POST:
        form = FormKutim(request.POST, request.FILES, instance=kutim)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Data Telah Berhasil diperbaharui")
            return redirect('kutim')
        else:
            form = FormKutim(instance=kutim)
            messages.success(
                request, "Terdapat kesalahan pada saat penginputan, Pastikan format Tanggal benar ! ")
            error = "Terdapat kesalahan pada saat penginputan, Pastikan format Tanggal benar !"
            konteks = {
                'form': form,
                'kutim': kutim,
                'error': error,
            }
            return render(request, template, konteks)
    else:
        form = FormKutim(instance=kutim)
        konteks = {
            'form': form,
            'kutim': kutim,
        }
        return render(request, template, konteks)


@login_required
def kutim(request):
    kutimm = Kutim.objects.all()
    konteks = {
        'kutimm': kutimm,
    }
    return render(request, 'kutim/kutim.html', konteks)


@login_required(login_url=settings.LOGIN_URL)
def tambah_kutim(request):
    if request.POST:
        form = FormKutim(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormKutim()
            pesan = "Data berhasil disimpan ke List DPT"
            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'kutim/tambah-kutim.html', konteks)
        else:
            error = "Terdapat kesalahan, periksa kembali Format Inputan dan wajib mengisi kolom bertanda (*) !"
            konteks = {
                'form': form,
                'error': error,
            }
            return render(request, 'kutim/tambah-kutim.html', konteks)
    else:
        form = FormKutim()
        konteks = {
            'form': form,
        }

    return render(request, 'kutim/tambah-kutim.html', konteks)
