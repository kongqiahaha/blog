from django.http import HttpResponse
from django.core.cache import cache
from polls.inform import index_inform, entry_inform
from django.shortcuts import render
from polls.userfavourite import user_favourite, my_favourite_DAO, get_ip


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
    dict_inform = index_inform()
    dict_inform["my_favourite"] = my_favourite.favourite
    return render(request, "index.html", dict_inform)


def about(request):
    return render(request, "about.html")


def entry(request):
    dict_entry = entry_inform(int(request.GET["id"]))
    if dict_entry is None:
        return HttpResponse(status=404)
    return render(request, "entry.html", dict_entry)


def message(request):
    return render(request, "message.html")


def text_list(request):
    return render(request, "text_list.html")


def test_writer(request):
    return render(request, "test_writer.html")
