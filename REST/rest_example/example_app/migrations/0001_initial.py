# Generated by Django 3.1.3 on 2020-11-10 07:35

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('author', models.CharField(max_length=250)),
                ('isbn', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MaxValueValidator(9999999999)])),
                ('description', models.TextField(default='NA')),
                ('genre', models.CharField(max_length=50)),
                ('price', models.PositiveIntegerField(blank=True, null=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
