from django.shortcuts import render, HttpResponse, redirect
from harum.models import Database
from harum.forms import FormDatabase
from django.contrib.auth.decorators import login_required
from harum.resource import DatabaseResource


def export_xls(request):
    database = DatabaseResource()
    # Khusus untuk download filter data tertentu
    # queryset = Database.objects.filter(nama_dpt='haris')
    # dataset = database.export(queryset)
    dataset = database.export()
    response = HttpResponse(
        dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=DPT.xls'
    return response


@login_required
def delete(request, delete_id):
    Database.objects.filter(id=delete_id).delete()
    return redirect(request, 'harum/index.html',)


@login_required
def index(request):
    namapemilih = Database.objects.all()
    context = {
        'Namapemilih': namapemilih,
    }
    return render(request, 'harum/index.html', context)


@login_required
def input(request):
    if request.POST:
        form = FormDatabase(request.POST)
        if form.is_valid():
            form.save()
            form = FormDatabase()
            pesan = "Data Berhasil di Input !"
            konteks = {
                'form': form,
                'pesan': pesan,
            }
            return render(request, 'harum/input.html', konteks)
    else:
        form = FormDatabase()

        konteks = {
            'form': form,
        }
    return render(request, 'harum/input.html', konteks)


@login_required
def update(request, id_data):
    # databases = Database.objects.get(id=id_update)
    if request.POST:
        data = Database.objects.get(id=id_data)
        databases = FormDatabase(request.POST, instance=data)
        if databases.is_valid():
            databases.save()
            databases = FormDatabase()
            pesan = "Data Berhasil di Input !"
            konteks = {
                'databases': databases,
                'pesan': pesan,
            }
            return render(request, 'harum/update.html', konteks)
    else:
        databases = FormDatabase()

        konteks = {
            'databases': databases,
        }
    return render(request, 'harum/update.html', konteks)

# def update_data(request, id_update):
#     databases = Database.objects.get(1)
#     print(databases)
#     template = 'update.html'
#     if request.POST:
#         form = FormDatabase(request.POST, instance=databases)
#         if form.is_valid():
#             form.save()
#             # form = FormDatabase()
#             # pesan = "UPDATE BERHASIL !"
#             # konteks = {
#             #     'form': form,
#             #     'pesan': pesan,
#             # }
#             return redirect('update', id_databases=id_update)
#     else:
#         form = FormDatabase(instance=databases)
#         konteks = {
#             'form': form,
#             'databases': databases,
#         }
#     return render(request, template, konteks)
    # context = {'databases': databases}
    # return render(request, 'update.html', context)
