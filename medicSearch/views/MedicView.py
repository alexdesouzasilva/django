from django.http import HttpResponse
from medicSearch.models.Profile import Profile


def list_medics_view(request):
    name = request.GET.get("name")
    speciality = request.GET.get("speciality")
    neighborhood = request.GET.get("neighborhood")
    city = request.GET.get("city")
    state = request.GET.get("state")

    #Busca usando ORM do DJango
    #Busca por perfis de médicos
    medics = Profile.objects.filter(role=2)

    #Filtra médico de acordo com o nome
    if name is not None and name != '':
        medics = medics.filter(user__first_name=name)
    if speciality is not None and speciality != '':
        medics = medics.filter(specialities_id=speciality)

        print(medics.all())


    print(medics)

    return HttpResponse('Listagem de 1 ou mais médicos')