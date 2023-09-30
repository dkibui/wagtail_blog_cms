from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page
from wagtail.images.blocks import ImageChooserBlock


class BlogPage(Page):
    description = models.CharField(max_length=255, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("description"),
    ]


class PostPage(Page):
    header_image = models.ForeignKey("wagtailimages.Image", on_delete=models.SET_NULL, null=True, blank=True, related_name="+")

    content_panels = Page.content_panels + [
        FieldPanel("header_image"),
    ]