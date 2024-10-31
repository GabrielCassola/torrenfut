from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import render
from .models import Camiseta, CamisetaTamanho, TipoProduto

def obter_opcoes_filtro():
    # Obter opções únicas para filtro
    cores_disponiveis = Camiseta.objects.values_list('cor_principal', flat=True).distinct()
    estilos_disponiveis = Camiseta.objects.values_list('estilo', flat=True).distinct()
    times_disponiveis = Camiseta.objects.values_list('time', flat=True).distinct()
    temporadas_disponiveis = Camiseta.objects.values_list('temporada', flat=True).distinct()
    tipos_produto_disponiveis = TipoProduto.objects.all()
    
    return {
        'cores_disponiveis': cores_disponiveis,
        'estilos_disponiveis': estilos_disponiveis,
        'times_disponiveis': times_disponiveis,
        'temporadas_disponiveis': temporadas_disponiveis,
        'tipos_produto_disponiveis': tipos_produto_disponiveis,
    }


def store(request):
    camisetas = Camiseta.objects.all()
    template = loader.get_template('home.html')
    opcoes_filtro = obter_opcoes_filtro()
    context = {
        'camisetas': camisetas,
        **opcoes_filtro,
    }
    return HttpResponse(template.render(context, request))


def produto(request, time, estilo, temporada):
    try:
        # Usando get() para buscar uma única camiseta
        camiseta = Camiseta.objects.get(time=time, estilo=estilo, temporada=temporada)
        tamanhos = CamisetaTamanho.objects.filter(camiseta=camiseta)
    except Camiseta.DoesNotExist:
        raise Http404("Camiseta não encontrada.")
    
    template = loader.get_template('produto.html')
    opcoes_filtro = obter_opcoes_filtro()
    context = {
        'camiseta': camiseta, 
        'tamanhos': tamanhos,
        **opcoes_filtro,

    }
    return HttpResponse(template.render(context, request))




def filtrar_camisetas(request):
    cor = request.GET.get('cor')
    estilo = request.GET.get('estilo')
    time = request.GET.get('time')
    temporada = request.GET.get('temporada')
    tipo_produto = request.GET.get('tipo_produto')

    # Buscar todas as camisetas
    camisetas = Camiseta.objects.all()
    if cor:
        camisetas = camisetas.filter(cor_principal=cor)
    if estilo:
        camisetas = camisetas.filter(estilo=estilo)
    if time:
        camisetas = camisetas.filter(time=time)
    if temporada:
        camisetas = camisetas.filter(temporada=temporada)
    if tipo_produto:
        camisetas = camisetas.filter(tipo_produto__id=tipo_produto)

    # Obter opções únicas para filtro
    cores_disponiveis = Camiseta.objects.values_list('cor_principal', flat=True).distinct()
    estilos_disponiveis = Camiseta.objects.values_list('estilo', flat=True).distinct()
    times_disponiveis = Camiseta.objects.values_list('time', flat=True).distinct()
    temporadas_disponiveis = Camiseta.objects.values_list('temporada', flat=True).distinct()
    tipos_produto_disponiveis = TipoProduto.objects.all()  # Presumindo que você tenha um modelo TipoProduto

    return render(request, 'home.html', {
        'camisetas': camisetas,
        'cores_disponiveis': cores_disponiveis,
        'estilos_disponiveis': estilos_disponiveis,
        'times_disponiveis': times_disponiveis,
        'temporadas_disponiveis': temporadas_disponiveis,
        'tipos_produto_disponiveis': tipos_produto_disponiveis,
    })
