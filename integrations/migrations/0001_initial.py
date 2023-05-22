# Generated by Django 4.2 on 2023-05-18 02:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Integration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('client_id', models.CharField(blank=True, max_length=255, null=True)),
                ('client_secret', models.CharField(blank=True, max_length=255, null=True)),
                ('scope', models.TextField(blank=True, null=True)),
                ('redirect_uri', models.CharField(blank=True, max_length=255, null=True)),
                ('authorization_code', models.CharField(blank=True, max_length=255, null=True)),
                ('access_token', models.TextField(blank=True, null=True)),
                ('refresh_token', models.TextField(blank=True, null=True)),
                ('api_key', models.CharField(blank=True, max_length=200, null=True)),
                ('instance_id', models.CharField(blank=True, max_length=200)),
                ('auth_json', models.TextField(blank=True, null=True)),
                ('enabled', models.BooleanField(default=False)),
                ('expire_at', models.DateTimeField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]