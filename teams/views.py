from django.shortcuts import render

from .forms import TeamForm

from .models import Team


# Create your views here.
def team_list_view(request, *args, **kwargs):
    obj = Team.objects.all().filter(isactive__exact=1)
    context = {
        'object': obj
    }
    return render(request, "teams/index.html", context)


def team_create_view(request):
    context = {}
    return render(request, "teams/create.html", context)


# def team_create_view(request):
#     form = TeamForm(request.POST or None)
#
#     if form.is_valid():
#         form.save()
#         form = TeamForm()
#
#     context = {
#         'form': form
#     }
#     return render(request, "teams/create.html", context)


def team_detail_view(request):
    obj = Team.objects.get(id=1)
    context = {
        'object': obj
    }
    return render(request, "teams/detail.html", context)
