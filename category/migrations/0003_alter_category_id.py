# Generated by Django 3.2.6 on 2021-09-05 14:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_auto_20210801_1608'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]