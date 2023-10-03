from django.db import models
from wagtail.fields import RichTextField
from wagtail.models import Page


class HomePage(Page):
    name = models.TextField(blank=True)
    body = RichTextField(blank=True)
    date = models.DateField("Post date")
    feed_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
