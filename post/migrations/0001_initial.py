# Generated by Django 2.0.6 on 2019-11-15 23:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_title', models.CharField(max_length=200)),
                ('chapter_id', models.IntegerField(default=999)),
                ('page_count', models.IntegerField(default=999)),
                ('chapter_content', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Diary_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Diary_Contents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('daiary_content', models.TextField()),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Diary_Category')),
            ],
        ),
        migrations.CreateModel(
            name='Novel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('novel_comment', models.CharField(max_length=200)),
                ('novel_summary', models.TextField(max_length=3000)),
                ('total_page', models.IntegerField(default=999)),
                ('total_chapter', models.IntegerField(default=999)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AddField(
            model_name='chapter',
            name='title',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='post.Novel'),
        ),
    ]
