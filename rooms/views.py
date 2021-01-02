from math import ceil
from django.shortcuts import render
from . import models


# config-settings.py의 templates-DIRS에 template 경로를 등록한다
# view의 이름은 core-urls의 view 이름과 같아야한다.
def all_rooms(request):
    page = request.GET.get("page", 1)
    page = int(page or 1)
    page_size = 10
    limit = page_size * page
    offset = limit - page_size
    all_rooms = models.Room.objects.all()[offset:limit]
    page_count = models.Room.objects.count() / page_size
    return render(
        request,
        "rooms/home.html",
        context={"rooms": all_rooms, "page": page, "page_count": ceil(page_count)},
    )
    # html은 templates 내부의 html 파일 이름과 같아야한다.
