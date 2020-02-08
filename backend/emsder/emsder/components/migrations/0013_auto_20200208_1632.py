# Generated by Django 3.0.2 on 2020-02-08 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('systemarchitectures', '0006_auto_20200208_0955'),
        ('components', '0012_auto_20200208_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='component',
            name='system',
        ),
        migrations.CreateModel(
            name='PiComponent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now=True)),
                ('modified_date', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=200)),
                ('component', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='components.Component')),
                ('system', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='picomponents', to='systemarchitectures.System')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
