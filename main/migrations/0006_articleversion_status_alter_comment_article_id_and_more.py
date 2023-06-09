# Generated by Django 4.2 on 2023-06-08 16:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_articleversion_article_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='articleversion',
            name='status',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AlterField(
            model_name='comment',
            name='article_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comment', to='main.article'),
        ),
        migrations.AlterField(
            model_name='like',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='like', to='main.article'),
        ),
        migrations.AlterField(
            model_name='share',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='share', to='main.article'),
        ),
    ]
