from django.http import HttpResponse

from .models import ScrumyGoals

def get_grading_parameters(request):
    goal = ScrumyGoals.objects.get(pk=1)
    return HttpResponse(goal)