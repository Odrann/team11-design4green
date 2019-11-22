# Generated by Django 2.2 on 2019-11-21 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0009_auto_20191121_1424'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proprietaire',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_nom', models.CharField(default='', max_length=50)),
                ('p_pre', models.CharField(default='', max_length=50)),
                ('p_soc', models.CharField(default='', max_length=50)),
                ('p_loclink', models.ManyToManyField(to='home_page.Logement')),
            ],
        ),
    ]