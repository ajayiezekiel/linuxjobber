from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User

from .models import ScrumyGoals, ScrumyHistory, GoalStatus

import random

def get_grading_parameters(request):
    goal = ScrumyGoals.objects.filter(goal_name='Learn Django')
    return HttpResponse(goal)

# def move_goal(request, goal_id):
#     try:
#         obj = ScrumyGoals.objects.get(pk=goal_id)
#     except Exception as e:
#         return render(request, 'ajayiezekiel9000scrumy/exception.html', 
#                       {'error': 'A record with that goal id does not exist'}
#                       )
#     else:
#         return HttpResponse(obj.goal_name)

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
    goal = ScrumyGoals.objects.get(goal_name='Learn Django')
    return render(request, 'ajayiezekiel9000scrumy/home.html', 
                {'first_name': goal.user.username,
                 'goal_name': goal.goal_name,
                 'goal_id': goal.goal_id
                })


def move_goal(request, goal_id):
    
    dic = ({ 'error' : "A record with that goal id does not exist"})
    dictionary = {'dict1' : dic}
    try:
        obj1 = ScrumyGoals.objects.get(pk = goal_id)
    except Exception as e:
        return render (request, 'ajayiezekiel9000scrumy/exception.html', dictionary)
    
    else:
        return HttpResponse(obj1.goal_name)