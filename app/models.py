from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    title = models.CharField('タイトル', max_length=255)
    thumbnail = models.CharField('サムネイル', max_length=255)
    user = models.ForeignKey(User, related_name='boards', on_delete=models.CASCADE)
    # user = models.ManyToManyField(
    #     User,
    #     through="Like",
    # )
    created_date = models.DateTimeField('作成日時', auto_now_add=True)
    update_date = models.DateTimeField('更新日時', auto_now=True)

    def __str__(self):
        return self.name



class Card(models.Model):
    title = models.CharField('タイトル', max_length=255)
    comment = models.CharField('コメント', max_length=255)
    URL = models.CharField('URL', max_length=255)
    thumbnail = models.CharField('サムネイル', max_length=255)
    positionX = models.IntegerField('x座標')
    positionY = models.IntegerField('y座標')
    board =  models.ForeignKey("Board", related_name='cards', on_delete=models.CASCADE)
    created_date = models.DateTimeField('作成日時', auto_now_add=True)
    update_date = models.DateTimeField('更新日時', auto_now=True)

    def __str__(self):
        return self.name



class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    board = models.ForeignKey("Board", on_delete=models.CASCADE)



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    board = models.ForeignKey("Board", on_delete=models.CASCADE)
    comment = models.CharField(max_length=255)


class From_To_Card(models.Model):
    from_board = models.ForeignKey("Board", related_name='from+', on_delete=models.CASCADE)
    to_board = models.ForeignKey("Board",  related_name='to+', on_delete=models.CASCADE)
    label = models.CharField(max_length=255)
