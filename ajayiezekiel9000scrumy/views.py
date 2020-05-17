from django.http import HttpResponse
from django.contrib.auth.models import User

from .models import ScrumyGoals, ScrumyHistory, GoalStatus

import random

def get_grading_parameters(request):
    goal = ScrumyGoals.objects.filter(goal_name='Learn Django')
    return HttpResponse(goal)

def move_goal(request, goal_id):
    goal = ScrumyGoals.objects.get(goal_id=goal_id)
    return HttpResponse(goal)

def add_goal(request):
    weekly = GoalStatus.objects.get(status_name='Weekly Goal')
    the_user = User.objects.get(username='louis')
    sample_dict = {}
    number = random.randint(1000,9999)
    if number not in sample_dict:
        ScrumyGoals.objects.create(goal_name='Keep Learning Django',
                                    goal_id=number,
                                    created_by='Louis',
                                    moved_by='Louis',
                                    owner='Louis',
                                    goal_status=weekly,
                                    user=the_user
                                )
        sample_dict[number] = number

def home(request):
    goals = ScrumyGoals.objects.filter(goal_name='Keep Learning Django')
    output = ', '.join([eachgoal.goal_name for eachgoal in goals])
    return HttpResponse(output)