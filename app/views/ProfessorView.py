import datetime
from django.contrib import messages

from django.shortcuts import redirect, render_to_response
from django.template import RequestContext

from app.models import Igreja, Classe, Pessoa, Professor, Departamento


def list_professores(request):
    igreja=None
    aluno=None
    professor=None
    categoria = int(request.session['categoria'])
    if categoria == 1:
        professor = Pessoa.objects.get(email=request.session['email']).professor_set.first()
    elif categoria == 2:
        aluno = Pessoa.objects.get(email=request.session['email']).aluno_set.first()
    else:
        igreja = Igreja.objects.get(email_responsavel=request.session['email'])
    return render_to_response('professores.html', {'igreja': igreja,
                                                   'aluno': aluno,
                                                   'professor': professor},
                              context_instance=RequestContext(request))


def add_professor(request):
    igreja = Igreja.objects.get(email_responsavel=request.session['email'])
    if request.method == 'GET':
        return render_to_response('add_professor.html', {'igreja': igreja},
                                  context_instance=RequestContext(request))
    elif request.method == 'POST':
        data = request.POST
        try:
            new_pessoa = Pessoa(nome=data['nome'], sexo=data['sexo'], nome_pai=data['nome_pai'],
                                nome_mae=data['nome_mae'],
                                data_nascimento=get_data_formated(data['data_nascimento']),
                                estado_civil=data['estado_civil'],
                                idade=data['idade'], email=data['email'],
                                telefone_residencial=data['telefone_residencial'],
                                telefone_comercial=data['telefone_comercial'],
                                telefone_celular=data['telefone_celular'],
                                endereco=data['endereco'], numero=data['numero'],
                                bairro=data['bairro'], cidade=data['cidade'], cep=data['cep'], estado=data['estado'])
            new_pessoa.save()
            new_professor = Professor(pessoa=new_pessoa)
            new_professor.foto = 'http://lorempixel.com/128/128/'
            if 'habilitado' in data:
                new_professor.habilitado = True
            new_professor.save()
            depto = Departamento.objects.get(id=data['id_depto'])
            depto.professores.add(new_professor)
            depto.save()
            igreja.professores.add(new_professor)
            igreja.save()
            messages.success(request, 'Professor adicionado com sucesso.')
            return redirect('/professores')
        except:
            messages.error(request, 'Houve algum erro.')
            return redirect('/add-professor')


def edit_professor(request, id):
    pessoa = Pessoa.objects.get(id=id)
    igreja = Igreja.objects.get(email_responsavel=request.session['email'])
    if request.method == 'GET':
        return render_to_response('edit_professor.html', {'igreja': igreja,
                                                          'pessoa': pessoa},
                                  context_instance=RequestContext(request))
    elif request.method == 'POST':
        data = request.POST
        try:
            pessoa.nome = data['nome']
            pessoa.sexo = data['sexo']
            pessoa.nome_pai = data['nome_pai']
            pessoa.nome_mae = data['nome_mae']
            pessoa.estado_civil = data['estado_civil']
            pessoa.idade = data['idade']
            pessoa.email = data['email']
            pessoa.telefone_residencial = data['telefone_residencial']
            pessoa.telefone_celular = data['telefone_celular']
            pessoa.telefone_comercial = data['telefone_comercial']
            pessoa.endereco = data['endereco']
            pessoa.numero = data['numero']
            pessoa.bairro = data['bairro']
            pessoa.cidade = data['cidade']
            pessoa.cep = data['cep']
            pessoa.estado = data['estado']
            pessoa.save()
            professor = pessoa.professor_set.first()
            if 'habilitado' in data:
                professor.habilitado = True
            else:
                professor.habilitado = False
            professor.save()
            messages.success(request, 'Professor editado com sucesso.')
            return redirect('/professores')
        except:
            messages.error(request, 'Nao foi possivel editar o professor.')
            return redirect('/professores')


def view_professor(request, id):
    pessoa = Pessoa.objects.get(id=id)
    igreja = Igreja.objects.get(email_responsavel=request.session['email'])
    if request.method == 'GET':
        return render_to_response('view_professor.html', {'igreja': igreja,
                                                          'pessoa': pessoa},
                                  context_instance=RequestContext(request))
    else:
        return redirect('/professores')


def remove_professor(request, id):
    igreja = Igreja.objects.get(email_responsavel=request.session['email'])
    try:
        professor = Professor.objects.get(id=id)
        igreja.professores.remove(professor)
        igreja.save()
        try:
            classe = Classe.objects.get(id=professor.classe_set.all()[0].id)
            classe.professor = None
            classe.save()
        except:
            pass
        professor.delete()
        messages.success(request, 'Professor removido com sucesso.')
        return redirect('/professores')
    except:
        messages.error(request, 'Nao foi possivel remover o professor.')
        return redirect('/professores')


def get_data_formated(data):
    # replace = data.replace('/', '-')
    date = datetime.datetime.strptime(data, '%d/%m/%Y')
    new_d = datetime.datetime.strftime(date, '%Y-%m-%d')
    return new_d
