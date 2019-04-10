from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):

    ONE = '별 1개'
    TWO = '별 2개'
    THREE = '별 3개'
    FOUR = '별 4개'
    FIVE = '별 5개'

    SCORE_CHOICES = (
        (ONE, '별 1개'),
        (TWO, '별 2개'),
        (THREE, '별 3개'),
        (FOUR, '별 4개'),
        (FIVE, '별 5개'),
    )
    title = models.CharField(max_length=200)
    contents = models.TextField()
    price = models.FloatField()
    score = models.CharField(max_length=5, choices=SCORE_CHOICES)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
