from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from empresarios.models import Empresas,Documento
from .models import PropostaInvestimento
from django.contrib import messages
from django.contrib.messages import constants
# Create your views here.

def sugestao(request):
    if not request.user.is_authenticated:
        return redirect('/usuarios/logar')
    areas = Empresas.area_choices
    if request.method == "GET":   
        return render(request, 'sugestao.html', {'areas': areas})
    elif request.method == "POST":
        tipo = request.POST.get('tipo')
        area = request.POST.getlist('area')
        valor = request.POST.get('valor')

        if tipo == 'C':
            empresas = Empresas.objects.filter(tempo_existencia='+5').filter(estagio="E")
        elif tipo == 'D':
            empresas = Empresas.objects.filter(tempo_existencia__in=['-6', '+6', '+1']).exclude(estagio="E")
        #TODO: Criar tipo generico
        empresas = empresas.filter(area__in=area)
        
        empresas_selecionadas = []
        for empresa in empresas:
            percentual = (float(valor) * 100) / float(empresa.valuation)
            if percentual >= 1:
                empresas_selecionadas.append(empresa)

        return render(request, 'sugestao.html', {'empresas': empresas_selecionadas, 'areas': areas})

def ver_empresa(request, id):
    empresa = Empresas.objects.get(id=id)
    documentos = Documento.objects.filter(empresa=empresa)
    #TODO: Filtrar as metricas dinamicamente
    return render(request, 'ver_empresa.html', {'empresa': empresa, 'documentos': documentos})

def realizar_proposta(request, id):
    valor = request.POST.get('valor')
    percentual = request.POST.get('percentual')
    empresa = Empresas.objects.get(id=id)

    propostas_aceitas = PropostaInvestimento.objects.filter(empresa=empresa).filter(status='PA')
    total = 0
    for pa in propostas_aceitas:
        total= total + pa.percentual
    
    if total + float(percentual) >empresa.percentual_equity:
        messages.add_message(request, constants.WARNING, 'O percentual supera o percentual restante para investimento.')
        return redirect(f'/investidores/ver_empresa/{id}')
    
    valuation = (100 * int(valor)) / int(percentual)

    if valuation < (int(empresa.valuation/2)):
        messages.add_message(request, constants.WARNING, f'O valor da sua proposta foi {valuation} e o minimo é {empresa.valuation}.')
        return redirect(f'/investidores/ver_empresa/{id}')
    pi = PropostaInvestimento(
        valor=valor,
        percentual=percentual,
        empresa=empresa,
        investidor=request.user
    )
    pi.save()
    return redirect(f'/investidores/assinar_contrato/{pi.id}')

def assinar_contrato(request, id):
    pi = PropostaInvestimento.objects.get(id=id)
    if pi.status != "AS":
        raise Http404()
    
    if request.method == "GET":
        return render(request, 'assinar_contrato.html', {'pi': pi})
    elif request.method == "POST":
        selfie = request.FILES.get('selfie')
        rg = request.FILES.get('rg')

        pi.selfie = selfie
        pi.rg = rg
        pi.status = 'PE'
        pi.save()
        messages.add_message(request, constants.SUCCESS, f'Contrato assinado com sucesso, sua proposta foi enviada a empresa.')
        return redirect(f'/investidores/ver_empresa/{pi.empresa.id}')
        
    

