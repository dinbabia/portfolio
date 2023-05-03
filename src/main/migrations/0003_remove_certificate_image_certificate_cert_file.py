# Generated by Django 4.2 on 2023-05-03 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_certificate_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificate',
            name='image',
        ),
        migrations.AddField(
            model_name='certificate',
            name='cert_file',
            field=models.FileField(blank=True, null=True, upload_to='certificate'),
        ),
    ]
