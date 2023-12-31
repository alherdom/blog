# Generated by Django 4.2.6 on 2023-10-10 14:12

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('blog', '0003_commen'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Commen',
            new_name='Comment',
        ),
        migrations.RenameIndex(
            model_name='comment',
            new_name='blog_commen_created_0e6ed4_idx',
            old_name='blog_commen_created_6eb24a_idx',
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
