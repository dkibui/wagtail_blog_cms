# Generated by Django 4.2.5 on 2023-10-05 05:02

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):
    dependencies = [
        ("blog", "0002_blogcategory_tag_postpagetags_postpage_tags_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="postpage",
            name="body",
            field=wagtail.fields.StreamField(
                [
                    ("h1", wagtail.blocks.CharBlock()),
                    ("paragraph", wagtail.blocks.RichTextBlock()),
                    (
                        "image_carousel",
                        wagtail.blocks.ListBlock(
                            wagtail.images.blocks.ImageChooserBlock()
                        ),
                    ),
                    (
                        "bullet_list",
                        wagtail.blocks.ListBlock(wagtail.blocks.CharBlock()),
                    ),
                    (
                        "image_text",
                        wagtail.blocks.StructBlock(
                            [
                                ("image1", wagtail.images.blocks.ImageChooserBlock()),
                                ("caption1", wagtail.blocks.CharBlock()),
                                ("image2", wagtail.images.blocks.ImageChooserBlock()),
                                ("caption2", wagtail.blocks.CharBlock()),
                            ]
                        ),
                    ),
                    (
                        "quote",
                        wagtail.blocks.StructBlock(
                            [
                                ("quote_by", wagtail.blocks.CharBlock()),
                                ("quotes", wagtail.blocks.RichTextBlock()),
                            ]
                        ),
                    ),
                ],
                blank=True,
                use_json_field=True,
            ),
        ),
    ]
