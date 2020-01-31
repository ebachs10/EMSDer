# Generated by Django 3.0.2 on 2020-01-31 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('components', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='created_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='component',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='component',
            name='modified_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='component',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='manufacture',
            name='created_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='manufacture',
            name='modified_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='signal',
            name='created_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='signal',
            name='modified_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='signalcategory',
            name='created_date',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='signalcategory',
            name='modified_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
