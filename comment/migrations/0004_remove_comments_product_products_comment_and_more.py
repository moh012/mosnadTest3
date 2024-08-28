# Generated by Django 5.0 on 2024-08-26 10:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_alter_products_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='product',
        ),
        migrations.AddField(
            model_name='products',
            name='comment',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='comments', to='comment.comments'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
