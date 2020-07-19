from blog.models import Textz
from django.utils import timezone
import re


def index_inform():
    text = Textz.objects.all()
    count = 1
    index_text_list = []
    for i in reversed(list(text)[-4:]):
        dict_inform = {"text_id": i.text_id, "text_head": i.text_head, "text_user": i.text_user,
                       "text_jianjie": i.text_jianjie,
                       "text_date": (timezone.now().year - i.text_date.year) * 12 * 30 + (
                               timezone.now().month - i.text_date.month) * 30 + (timezone.now().day - i.text_date.day)}
        index_text_list.append(dict_inform)
        count += 1
    if count <= 4:
        for i in range(0, 5 - count):
            dict_inform = {"text_id": None, "text_head": None, "text_user": None, "text_jianjie": None,
                           "text_date": None}
            index_text_list.append(dict_inform)

    del (index_text_list[0]["text_jianjie"])
    return index_text_list


def entry_inform(id):
    if len(Textz.objects.filter(text_id=id)) == 0:
        return None
    entry_text = Textz.objects.get(text_id=id)
    a = re.split("\r|\n", entry_text.text_tt)
    while "" in a:
        a.remove("")
    print(a)
    dict_inform_entry = {"favorites": entry_text.text_favourite,
                         "entry_id": entry_text.text_id,
                         "writer_name": entry_text.text_user,
                         "date": (timezone.now().year - entry_text.text_date.year) * 12 * 30 + (
                                 timezone.now().month - entry_text.text_date.month) * 30 + (
                                         timezone.now().day - entry_text.text_date.day),
                         "text_head": entry_text.text_head,
                         "text": a}
    return dict_inform_entry


def text_list_inform():
    more_text_list = []
    for i in reversed(list(Textz.objects.all())[:-4]):
        more_dict_form = {"text_id": i.text_id, "text_head": i.text_head, "text_user": i.text_user,
                          "text_jianjie": i.text_jianjie,
                          "text_date": (timezone.now().year - i.text_date.year) * 12 * 30 + (
                                  timezone.now().month - i.text_date.month) * 30 + (
                                                   timezone.now().day - i.text_date.day)}
        more_text_list.append(more_dict_form)
    return more_text_list
