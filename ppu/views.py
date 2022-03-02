from django.shortcuts import render, redirect, HttpResponse
from ppu.models import Ppu
from ppu.forms import FormPpu
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from ppu.resource import PpuResource


@login_required(login_url=settings.LOGIN_URL)
def index(request):
    return render(request, 'ppu/index.html')


@login_required(login_url=settings.LOGIN_URL)
def export_xls(request):
    ppu = PpuResource()
    dataset = ppu.export()
    response = HttpResponse(
        dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Data DPT.xls"'
    return response


@login_required(login_url=settings.LOGIN_URL)
def hapus_ppu(request, id_ppu):
    ppu = Ppu.objects.filter(id=id_ppu)
    ppu.delete()

    messages.success(request, "Data Berhasil dihapus")
    return redirect('ppu')


@login_required(login_url=settings.LOGIN_URL)
def ubah_ppu(request, id_ppu):
    ppu = Ppu.objects.get(id=id_ppu)
    template = 'ppu/ubah-ppu.html'
    if request.POST:
        form = FormPpu(request.POST, request.FILES, instance=ppu)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Data Telah Berhasil diperbaharui")
            return redirect('ppu')
        else:
            form = FormPpu(instance=ppu)
            messages.success(
                request, "Terdapat kesalahan pada saat penginputan, Pastikan format Tanggal benar ! ")
            error = "Terdapat kesalahan pada saat penginputan, Pastikan format Tanggal benar !"
            konteks = {
                'form': form,
                'ppu': ppu,
                'error': error,
            }
            return render(request, template, konteks)
    else:
        form = FormPpu(instance=ppu)
        konteks = {
            'form': form,
            'ppu': ppu,
        }
        return render(request, template, konteks)


@login_required
def ppu(request):
    ppuu = Ppu.objects.all()
    konteks = {
        'ppuu': ppuu,
    }
    return render(request, 'ppu/ppu.html', konteks)


@login_required(login_url=settings.LOGIN_URL)
def tambah_ppu(request):
    if request.POST:
        form = FormPpu(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = FormPpu()
            pesan = "Data berhasil disimpan ke List DPT"
            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'ppu/tambah-ppu.html', konteks)
        else:
            error = "Terdapat kesalahan, periksa kembali Format Inputan dan wajib mengisi kolom bertanda (*) !"
            konteks = {
                'form': form,
                'error': error,
            }
            return render(request, 'ppu/tambah-ppu.html', konteks)
    else:
        form = FormPpu()
        konteks = {
            'form': form,
        }

    return render(request, 'ppu/tambah-ppu.html', konteks)
