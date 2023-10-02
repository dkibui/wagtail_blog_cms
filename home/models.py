from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField


class HomePage(Page):
    title = models.TextField()
    body = RichTextField()
    date = models.DateField("Post date")
    feed_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
