# Generated by Django 3.1.7 on 2021-03-03 10:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='text',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='date_added',
            new_name='created_time',
        ),
        migrations.RemoveField(
            model_name='article',
            name='topic',
        ),
        migrations.AddField(
            model_name='article',
            name='authors',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user', verbose_name='用户'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='click_nums',
            field=models.IntegerField(default=0, verbose_name='阅读数量'),
        ),
        migrations.AddField(
            model_name='article',
            name='is_deleted',
            field=models.BooleanField(default=True, verbose_name='是否删除'),
        ),
        migrations.AddField(
            model_name='article',
            name='title',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
    ]