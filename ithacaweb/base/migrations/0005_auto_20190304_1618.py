# Generated by Django 2.1.7 on 2019-03-04 16:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers
import wagtail.core.models
import wagtail.images.models
import wagtail.search.index


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('base', '0004_auto_20180522_1856'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='title')),
                ('file', models.ImageField(height_field='height', upload_to=wagtail.images.models.get_upload_to, verbose_name='file', width_field='width')),
                ('width', models.IntegerField(editable=False, verbose_name='width')),
                ('height', models.IntegerField(editable=False, verbose_name='height')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='created at')),
                ('focal_point_x', models.PositiveIntegerField(blank=True, null=True)),
                ('focal_point_y', models.PositiveIntegerField(blank=True, null=True)),
                ('focal_point_width', models.PositiveIntegerField(blank=True, null=True)),
                ('focal_point_height', models.PositiveIntegerField(blank=True, null=True)),
                ('file_size', models.PositiveIntegerField(editable=False, null=True)),
                ('file_hash', models.CharField(blank=True, editable=False, max_length=40)),
                ('caption', models.CharField(blank=True, max_length=255)),
                ('collection', models.ForeignKey(default=wagtail.core.models.get_root_collection_id, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.Collection', verbose_name='collection')),
                ('tags', taggit.managers.TaggableManager(blank=True, help_text=None, through='taggit.TaggedItem', to='taggit.Tag', verbose_name='tags')),
                ('uploaded_by_user', models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='uploaded by user')),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail.search.index.Indexed, models.Model),
        ),
        migrations.CreateModel(
            name='CustomRendition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filter_spec', models.CharField(db_index=True, max_length=255)),
                ('file', models.ImageField(height_field='height', upload_to=wagtail.images.models.get_rendition_upload_to, width_field='width')),
                ('width', models.IntegerField(editable=False)),
                ('height', models.IntegerField(editable=False)),
                ('focal_point_key', models.CharField(blank=True, default='', editable=False, max_length=16)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='renditions', to='base.CustomImage')),
            ],
        ),
        migrations.AlterField(
            model_name='formpage',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='base.CustomImage'),
        ),
        migrations.AlterField(
            model_name='gallerypage',
            name='image',
            field=models.ForeignKey(blank=True, help_text='Landscape mode only; horizontal width between 1000px and 3000px.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='base.CustomImage'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='image',
            field=models.ForeignKey(blank=True, help_text='Homepage image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='base.CustomImage'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='promo_image',
            field=models.ForeignKey(blank=True, help_text='Promo image', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='base.CustomImage'),
        ),
        migrations.AlterField(
            model_name='people',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='base.CustomImage'),
        ),
        migrations.AlterField(
            model_name='standardpage',
            name='image',
            field=models.ForeignKey(blank=True, help_text='Landscape mode only; horizontal width between 1000px and 3000px.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='base.CustomImage'),
        ),
        migrations.AlterUniqueTogether(
            name='customrendition',
            unique_together={('image', 'filter_spec', 'focal_point_key')},
        ),
    ]
