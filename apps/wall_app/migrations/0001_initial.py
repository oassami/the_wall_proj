# Generated by Django 3.1.7 on 2021-06-06 04:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_txt', models.TextField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='login_app.user')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_txt', models.TextField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('messages', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='wall_app.message')),
                ('users', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='login_app.user')),
            ],
        ),
    ]
