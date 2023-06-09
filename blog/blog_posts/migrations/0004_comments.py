# Generated by Django 4.2.1 on 2023-06-05 12:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_posts', '0003_post_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_email', models.EmailField(max_length=254)),
                ('user_name', models.CharField(max_length=50, verbose_name='Имя')),
                ('text_comments', models.TextField(max_length=200, verbose_name='Текст комментария')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog_posts.post', verbose_name='Публикация')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
            },
        ),
    ]
