
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('codigo', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('fechaNacimiento', models.CharField(max_length=50)),
                #('creditos', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
