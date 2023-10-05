from wagtail.blocks import StructBlock, CharBlock, RichTextBlock, StreamBlock, ListBlock
from wagtail.images.blocks import ImageChooserBlock


class ImageText(StructBlock):
    image1 = ImageChooserBlock()
    caption1 = CharBlock()
    image2 = ImageChooserBlock()
    caption2 = CharBlock()


class Quote(StructBlock):
    quote_by = CharBlock()
    quotes = RichTextBlock()


class BodyBlock(StreamBlock):
    h1 = CharBlock()
    paragraph = RichTextBlock()
    image_carousel = ListBlock(ImageChooserBlock())
    bullet_list = ListBlock(CharBlock())
    image_text = ImageText()
    quote = Quote()



