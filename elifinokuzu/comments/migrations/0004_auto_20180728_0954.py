# Generated by Django 2.0.7 on 2018-07-28 09:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0003_auto_20180728_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_to_edge',
            name='edge',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_edge', to='dictionary.Edge'),
        ),
    ]
