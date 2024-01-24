from medicSearch.models.Profile import Profile
from django.shortcuts import render
from django.db.models import Q


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

    #dicionário com valor da consulta SQL
    context = {
        'medics': medics
    }

    return render(request, template_name='medic/medics.html', context=context, status=200)