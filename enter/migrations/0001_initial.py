# Generated by Django 2.2.1 on 2019-05-16 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='cdastro_livros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('edicao', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('ano', models.IntegerField()),
                ('editora', models.CharField(max_length=50)),
            ],
        ),
    ]