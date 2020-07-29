from django.contrib.auth import authenticate
from django.http import HttpResponse, JsonResponse
from django.core.cache import cache
from blog.inform import *
from django.shortcuts import render, redirect

from blog.models import Person
from blog.userfavourite import *


def user_favourite_add(request):
    rep = HttpResponse()
    if request.method == "POST":
        if "id" in request.POST:
            ip = get_ip(request)
            if cache.get("id:" + str(ip) + "&&" + str(request.POST["id"])) is not None:
                return HttpResponse(-1)
            else:
                fav = user_favourite(int(request.POST["id"]))
                fav.text_favourite += 1
                fav.save()
                cache.set("id:" + str(ip) + "&&" + str(request.POST["id"]), "true", timeout=60 * 60 * 24)
                rep.write(str(fav.text_favourite))
        if "my_id" in request.POST:
            ip = get_ip(request)
            if cache.get("my_id:" + str(ip) + "&&" + str(request.POST["my_id"])) is not None:
                return HttpResponse(-1)
            else:
                cache.set("my_id:" + str(ip) + "&&" + str(request.POST["my_id"]), "true", timeout=60 * 60 * 24)
                myfav = my_favourite_DAO(int(request.POST["my_id"]))
                myfav.favourite += 1
                myfav.save()
                rep.write(str(myfav.favourite))
    return rep


def index(request):
    my_favourite = my_favourite_DAO(1)
    dict_inform = {"index_text_list": index_inform()}
    if my_favourite is False:
        dict_inform["my_favourite"] = None
    else:
        dict_inform["my_favourite"] = my_favourite.favourite
    return render(request, "index.html", dict_inform)


def about(request):
    return render(request, "about.html")


def entry(request):
    dict_entry = entry_inform(int(request.GET["id"]))
    if dict_entry is None:
        return redirect("/index.html")
    return render(request, "entry.html", dict_entry)


def message(request):
    return render(request, "message.html")


def text_list(request):
    dict_text = {'text_list': text_list_inform()}
    return render(request, "text_list.html", dict_text)


def test_writer(request):
    try:
        if request.session["is_login"]:
            return render(request, "test_writer.html")
    finally:
        return redirect("/sign_in")


def new_text_get_text(request):
    a = new_text(request.POST["user_head"], request.POST["user_jj"], request.session["username"],
                 request.POST["user_text"])
    return redirect("index.html")


def sign_in_page(request):
    if request.method == "POST":
        d = {}
        username = request.POST["username"]
        password = request.POST["password"]
        person = authenticate(request, username=username, password=password)
        if person:
            d["code"] = 100
            request.session.set_expiry(60*60*24*7)
            request.session["username"]=request.POST["username"]
            request.session["is_login"]=True
        else:
            d["code"] = 200
        return JsonResponse(d)
    else:
        try:
            if request.session["is_login"]:
                return redirect("testwriter")
        finally:
            return render(request, 'sign_in.html')


def sign_up_page(request):
    if request.method == "POST":

        try:
            person = Person.objects.create_user(username=request.POST["username"], password=request.POST["password"],
                        email=request.POST["email"])
        except:
            return JsonResponse({"code": 200})
        return JsonResponse({"code":100})
    else:
        return render(request, 'sign_up.html')
