from django.db import models


class TimeStampedModel(models.Model):

    """ TimeStamped Model """

    created = models.DateTimeField(
        auto_now_add=True
    )  # auto_now_add는 모델이 생성된 날짜를 구하는 방식
    updated = models.DateTimeField(auto_now=True)  # auto_now 는 새로운 날짜로 업데이트 해주는 방식

    class Meta:
        abstract = True
