from django.contrib import admin

# Taskモデルをインポート
from .models import Board
from .models import Card
from .models import Like
from .models import Comment
from .models import From_To_Card

# 管理サイトへのモデルを登録
admin.site.register(Board)
admin.site.register(Card)
admin.site.register(Like)
admin.site.register(Comment)
admin.site.register(From_To_Card)
