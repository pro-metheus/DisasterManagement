# Generated by Django 2.0.7 on 2018-11-02 09:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('D_ASSESSMENT', '0005_auto_20181102_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='disaster',
            name='place',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='D_ASSESSMENT.Place'),
        ),
    ]
