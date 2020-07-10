from polls.models import Textz
from django.utils import timezone


def index_inform():
    text = Textz.objects.all()
    dict_inform = {}
    count = 1
    for i in list(text)[-4:]:
        dict_inform["text_id_" + str(count)] = i.text_id
        dict_inform["text_head_" + str(count)] = i.text_head
        dict_inform["text_user_" + str(count)] = i.text_user
        dict_inform["text_jianjie_" + str(count)] = i.text_jianjie
        dict_inform["text_date_" + str(count)] = timezone.datetime.today().day - i.text_date.day
        count += 1
    del (dict_inform["text_jianjie_1"])
    return dict_inform


def entry_inform(id):
    if len(Textz.objects.filter(text_id=id)) == 0:
        return None
    entry_text = Textz.objects.get(text_id=id)
    dict_inform_entry = {"favorites": entry_text.text_favourite,
                         "entry_id": entry_text.text_id,
                         "writer_name": entry_text.text_user,
                         "date": timezone.datetime.today().day - entry_text.text_date.day,
                         "text_head": entry_text.text_head,
                         "text": entry_text.text_tt}
    return dict_inform_entry
