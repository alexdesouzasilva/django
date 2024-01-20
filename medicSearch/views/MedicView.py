from django.http import HttpResponse
from medicSearch.models.Profile import Profile


def list_medics_view(request):
    name = request.GET.get("name")
    speciality = request.GET.get("speciality")
    neighborhood = request.GET.get("neighborhood")
    city = request.GET.get("city")
    state = request.GET.get("state")

    #Busca usando ORM do DJango
    medic = Profile.objects.filter(role=2).all()
    print(medic)

    return HttpResponse('Listagem de 1 ou mais médicos')