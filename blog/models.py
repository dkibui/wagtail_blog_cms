from django.db import models
from django.db.models import CASCADE, SET_NULL
from modelcluster.fields import ParentalKey
from taggit.managers import TaggableManager
from taggit.models import Tag as TaggitTag
from taggit.models import TaggedItemBase
from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.models import Page
from wagtail.snippets.models import register_snippet


class BlogPage(Page):
    description = models.CharField(max_length=255, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("description"),
    ]


class PostPage(Page):
    header_image = models.ForeignKey("wagtailimages.Image", on_delete=SET_NULL, null=True, blank=True,
                                     related_name="+")
    tags = TaggableManager(through="PostPageTags", blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("header_image"),
        FieldPanel("tags"),
        InlinePanel("categories", label="category"),
    ]


class PostPageBlogCategory(models.Model):
    page = ParentalKey("blog.PostPage", on_delete=CASCADE, blank=True, related_name="categories")
    blog_category = models.ForeignKey("BlogCategory", on_delete=CASCADE, blank=True, related_name="post_pages")

    panels = [
        FieldPanel("blog_category"),
    ]

    class Meta:
        unique_together = ("page", "blog_category",)


class PostPageTags(TaggedItemBase):
    content_object = ParentalKey("blog.PostPage", blank=True)


@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255, blank=True)
    slug = models.SlugField(max_length=255, unique=True)

    panels = [
        FieldPanel("name"),
        FieldPanel("slug"),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


@register_snippet
class Tag(TaggitTag):
    class Meta:
        proxy = True
