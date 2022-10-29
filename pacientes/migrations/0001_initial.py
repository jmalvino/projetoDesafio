# Generated by Django 4.1.2 on 2022-10-29 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pacientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('telefone', models.CharField(max_length=255)),
                ('endereco', models.CharField(max_length=255)),
                ('numero', models.CharField(max_length=50)),
                ('cidade', models.CharField(max_length=100)),
                ('uf', models.CharField(max_length=2)),
                ('pais', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=8)),
                ('dataDeCriacao', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
