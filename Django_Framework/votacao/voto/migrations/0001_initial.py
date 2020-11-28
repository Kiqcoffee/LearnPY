# Generated by Django 3.1.2 on 2020-11-28 17:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pergunta_texto', models.CharField(max_length=100)),
                ('data_pub', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='Escolha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('escolha_texto', models.CharField(max_length=100)),
                ('votos', models.IntegerField(default=0)),
                ('pergunta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='voto.pergunta')),
            ],
        ),
    ]
