# Generated by Django 3.0.8 on 2020-07-28 16:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='タイトル')),
                ('thumbnail', models.CharField(max_length=255, verbose_name='サムネイル')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Board')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='From_To_Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
                ('from_board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from+', to='app.Board')),
                ('to_board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to+', to='app.Board')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=255)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Board')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='タイトル')),
                ('comment', models.CharField(max_length=255, verbose_name='コメント')),
                ('URL', models.CharField(max_length=255, verbose_name='URL')),
                ('thumbnail', models.CharField(max_length=255, verbose_name='サムネイル')),
                ('positionX', models.IntegerField(verbose_name='x座標')),
                ('positionY', models.IntegerField(verbose_name='y座標')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='作成日時')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cards', to='app.Board')),
            ],
        ),
        migrations.AddField(
            model_name='board',
            name='user',
            field=models.ManyToManyField(through='app.Like', to=settings.AUTH_USER_MODEL),
        ),
    ]
