# Generated by Django 3.0.5 on 2020-04-14 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ControleAluno', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='cpf',
            field=models.CharField(max_length=11),
        ),
    ]
