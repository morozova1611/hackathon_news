# Generated by Django 4.0.3 on 2022-04-21 07:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='files/')),
            ],
        ),
        migrations.CreateModel(
            name='Predpriyatie',
            fields=[
                ('bin_id', models.CharField(max_length=12, primary_key=True, serialize=False, unique=True, verbose_name='БИН')),
                ('full_name', models.CharField(max_length=50, unique=True, verbose_name='Полное наименование')),
                ('address', models.CharField(max_length=60, unique=True, verbose_name='Адрес')),
                ('phone', models.CharField(max_length=11, unique=True, verbose_name='Телефон')),
                ('fio_ruk', models.CharField(max_length=50, unique=True, verbose_name='ФИО руководителя')),
                ('uchrediteli', models.CharField(max_length=200, unique=True, verbose_name='Учредители')),
                ('history', models.TextField(verbose_name='История')),
            ],
            options={
                'verbose_name_plural': 'Предприятия',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=30, verbose_name='Тег')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Тема')),
                ('content', models.TextField(verbose_name='Описание')),
                ('bin_news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.predpriyatie', verbose_name='БИН предприятия')),
                ('file', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='files', to='app.file', verbose_name='Файл')),
                ('tags', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tags', to='app.tag', verbose_name='Теги')),
            ],
            options={
                'verbose_name_plural': 'Новости',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=100, null=True, verbose_name='имя пользователя')),
                ('text', models.CharField(max_length=5000, verbose_name='текст комментария')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news', to='app.news', verbose_name='Новость')),
            ],
        ),
    ]
