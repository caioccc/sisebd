from django.shortcuts import redirect, render_to_response
from django.template import RequestContext

from app.models import Igreja, Departamento, Classe


def list_classes(request):
    igreja = Igreja.objects.get(email_responsavel=request.session['email'])
    return render_to_response('classes.html', {'igreja': igreja},
                              context_instance=RequestContext(request))


def add_classe(request):
    igreja = Igreja.objects.get(email_responsavel=request.session['email'])
    if request.method == 'GET':
        return render_to_response('add_classe.html', {'igreja': igreja},
                                  context_instance=RequestContext(request))
    elif request.method == 'POST':
        data = request.POST
        try:
            new_classe = Classe(nome=data['nome'], professor=data['id_professor'], idade_minima=data['idade_minima'],
                                idade_maxima=data['idade_maxima'])
            new_classe.save()
            depto = Departamento.objects.get(id=data['id_depto'])
            depto.classes.add(new_classe)
            depto.save()
            igreja.classes.add(new_classe)
            igreja.save()
            return redirect('/classes')
        except:
            return redirect('/add-classe')


def edit_classe(request, id):
    classe = Classe.objects.get(id=id)
    igreja = Igreja.objects.get(email_responsavel=request.session['email'])
    if request.method == 'GET':
        return render_to_response('edit_classe.html', {'igreja': igreja,
                                                       'classe': classe},
                                  context_instance=RequestContext(request))
    elif request.method == 'POST':
        data = request.POST
        try:
            classe.nome = data['nome']
            classe.idade_minima = data['idade_minima']
            classe.idade_maxima = data['idade_maxima']
            classe.save()
            return redirect('/classes')
        except:
            return redirect('/edit-classe')


def view_classe(request, id):
    classe = Classe.objects.get(id=id)
    igreja = Igreja.objects.get(email_responsavel=request.session['email'])
    if request.method == 'GET':
        return render_to_response('view_classe.html', {'igreja': igreja,
                                                       'clase': classe},
                                  context_instance=RequestContext(request))
    else:
        return redirect('/classes')