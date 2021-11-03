# Generated by Django 3.2.8 on 2021-11-03 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('food_management_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizacion',
            name='visibilidad',
            field=models.BooleanField(default=1),
        ),
        migrations.AlterField(
            model_name='organizacion',
            name='pagina_web',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='food_management_app.organizacion', verbose_name='Organizacion'),
        ),
    ]
