from blog.models import Textz, Unfavourable


def user_favourite(id):
    if len(Textz.objects.filter(text_id=id)) == 0:
        return None
    text = Textz.objects.get(text_id=id)
    return text


def my_favourite_DAO(id):
    if len(Unfavourable.objects.filter(user_id=id)) == 0:
        return False
    user = Unfavourable.objects.get(user_id=id)
    return user


def get_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]  # 所以这里是真实的ip
    else:
        ip = request.META.get('REMOTE_ADDR')  # 这里获得代理ip
    return ip


def new_text(head, jj, name, text:str):
    t = Textz(text_user=name, text_head=head, text_jianjie=jj, text_tt=text)
    print(text)
    t.save()
    return t.text_id
