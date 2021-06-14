from django.shortcuts import render
from .models import User,Room,Options,Questions,Voters
import json
from . import formscraper
from django.http import JsonResponse
username=""
def home(request):
    context = {
        "is_true":True
    }
    return render(request,"forms/home.html")
def join_room(request):
    name = request.POST["name"]
    request.session["thename"] = name
    password = request.POST["password"]
    if User.objects.filter(name=name).exists():
        real_password = ""
        for user in User.objects.filter(name=name):
            real_password = user.password
            user_id = user.id
        if real_password != password:
            context = {
                "is_true":False,
                "short_pass":False
            }
            return render(request,"forms/home.html",context)
        else:
            
            context = {
                "name":name,
                "user_id":user_id
            }
            return render(request,"forms/join_room.html",context)
    else:
        if len(password) < 4:
            context = {
                "is_true":True,
                "short_pass":True
            }
            return render(request,"forms/home.html",context)
        User.objects.create(name=name,password=password)
        user_id = User.objects.filter(name=name,password=password)[0].id
        context = {
            "name":name,
            "user_id":user_id
        }
        return render(request,"forms/join_room.html")


def room_url(request):
    name = request.POST["name"]
    room_name = request.POST["room_name"]
    password = request.POST["room_password"]
    
    if Room.objects.filter(room_name=room_name).exists():
        url = ""
        for room in Room.objects.filter(room_name=room_name):
            url = Room.url
            real_password = ""
            for pas in Room.objects.filter(room_name=room_name):
                real_password = pas.room_password
            
        if real_password != password:
            context = {
                "is_true":False,
                "short_pass":True,
                "short_name":True,
                "name":name,
            }
            return render(request,"forms/join_room.html",context)
        else:
            questions_list = []
            options_list = []
            votes_list = []
            option_id_list = []
            for question in Questions.objects.filter(room=room_name):
                questions_list.append(question.question)
                sub_option = []
                sub_votes = []
                sub_id = []
                for option in Options.objects.filter(question=question.question,room_name=room_name):
                    sub_option.append(option.option)
                    sub_votes.append(option.votes)
                    sub_id.append(option.id)
                options_list.append(sub_option)
                votes_list.append(sub_votes)
                option_id_list.append(sub_id)

            zipped_list = zip(votes_list,options_list,questions_list)
            name = request.session["thename"]
            context = {
                "zipped_list": zipped_list,
                "room_name":room_name,
                "name":name
            }
            return render(request,"forms/display_room.html",context)
    else:
        thename = request.session["thename"]
        context = {
            "room_name":room_name,
            "room_password":password,
            "name":thename,
        }
        return render(request,"forms/room_url.html",context)


def display_room(request):
    room_name = request.POST["room_name"]
    room_password = request.POST["room_password"]
    room_url = request.POST["url"]
    name = request.session["thename"]
    Room.objects.create(room_name=room_name, room_password=room_password,url=room_url)
    try:
        ques_ans_dict = formscraper.ques_dict(room_url)
    except:
        context = {
            "problem_occured":True,
            "room_name": room_name,
            "room_password": room_password,
            "name":name
        }
        return render(request,"forms/room_url.html",context)
    
    options_list = []
    votes_list = []
    questions_list = []
    option_id_list = []
    for question in ques_ans_dict:
        sub_option = []
        sub_vote = []
        sub_id = []
        questions_list.append(question)
        for option in ques_ans_dict[question]:
            Options.objects.create(option=option, question=question,votes=0,room_name=room_name)
            sub_option.append(option)
            sub_vote.append(0)
            for option in Options.objects.filter(option=option, question=question, room_name=room_name):
                sub_id.append(option.id)
            
        options_list.append(sub_option)
        votes_list.append(sub_vote)
        option_id_list.append(sub_id)
        Questions.objects.create(question=question, room=room_name)
    context = {
        "show_message":True,
        "name":name
    }
    return render(request, 'forms/join_room.html',context)

def vote_option(request):
    option = json.loads(request.body)
    id = option['id']
    question = option["question"]
    name = option["name"]
    sub_option = option["option"]
    room_name = option["room_name"]
    
    if Voters.objects.filter(name=name,question=question,room_name=room_name,option_id = id).exists():
        return JsonResponse({})
    else:
        if Voters.objects.filter(name=name,question=question,room_name=room_name).exists():
            option_voted_id = Voters.objects.filter(name=name,question=question,room_name=room_name)[0].option_id
            option = Options.objects.filter(id=option_voted_id)[0]
            option.votes -= 1
            option.save()
            option = Options.objects.filter(id=id)[0]
            option.votes += 1
            option.save()
            Voters.objects.filter(name=name,question=question,room_name=room_name,option_id=option_voted_id).delete()
            Voters.objects.create(name=name,question=question,room_name=room_name,option_id=id)
            return JsonResponse({})
        else:
            option = Options.objects.filter(id=id)[0]
            option.votes += 1
            option.save()

            Voters.objects.create(name=name,question=question,room_name=room_name,option_id=id)
            return JsonResponse({})
