from medicSearch.models.Profile import Profile
from django.shortcuts import render
from django.db.models import Q
from django.core.paginator import Paginator


def list_medics_view(request):
    name = request.GET.get("name")
    speciality = request.GET.get("speciality")
    neighborhood = request.GET.get("neighborhood")
    city = request.GET.get("city")
    state = request.GET.get("state")


    ###ORM - USANDO QUERYSET
    #Busca usando ORM do DJango
    #Busca por perfis de médicos
    medics = Profile.objects.filter(role=2)

    #Filtra médico de acordo com o nome
    if name is not None and name != '':
        medics = medics.filter(Q(user__first_name__contains=name) | Q(user__username__contains=name))

    if speciality is not None:
        medics = medics.filter(specialties__id=speciality)

    if neighborhood is not None:
        medics = medics.filter(addresses__neighborhood=neighborhood)

    else:
        if city is not None:
            medics = medics.filter(addresses__neighborhood__city=city)
        elif state is not None:
            medics = medics.filter(addresses__neighborhood__city__state=state)
    #**Aqui finaliza a consulta***#

    #Adicionando paginação:
    if len(medics) > 0:

        paginator = Paginator(medics, 8)
        page = request.GET.get('page')
        #Verifica qual página foi selecionada
        medics = paginator.get_page(page)

    get_copy = request.GET.copy()
    #Para não perder os parâmetros da url nas trocas de página
    #Pega os parâmetros atuais da url e remove o parâmetro page
    parameters = get_copy.pop('page', True) and get_copy.urlencode()

    #dicionário com valor da consulta SQL
    context = {
        'medics': medics,
        #Add parameters da paginação
        'parameters': parameters
    }

    return render(request, template_name='medic/medics.html', context=context, status=200)