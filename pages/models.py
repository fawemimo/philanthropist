from django.db import models
from tinymce import models as tinymce_models
from django.core.validators import FileExtensionValidator, MinValueValidator
from .validates import *


class Testimony(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    display_pic = models.ImageField(        
        upload_to="testimony/displayPics/",
        validators=[
            validate_file_size,
            FileExtensionValidator(allowed_extensions=["jpg", "png", "jpeg"]),
        ],
        blank=True, null = True
    )
    description = tinymce_models.HTMLField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Testimonies"
        verbose_name_plural = "Testimonies"


class ReadOurNew(models.Model):
    title = models.CharField(max_length=255)
    news_display_pic = models.ImageField(
        default="",
        upload_to="readournews/displayPics/",
        validators=[
            validate_file_size,
            FileExtensionValidator(allowed_extensions=["jpg", "png", "jpeg"]),
        ],
        blank=True, null = True
    )
    description = tinymce_models.HTMLField()
    anchor_link = models.CharField(max_length=1000)
    date_created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Read Our New"
        verbose_name_plural = "Read Our News"


class Philanthropist(models.Model):
    name = models.CharField(max_length=255)
    display_pics = models.ImageField(
        upload_to="philanthropist/displayPics",
        validators=[
            validate_file_size,
            FileExtensionValidator(allowed_extensions=["jpg", "png", "jpeg"]),
        ],
        blank=True, null = True
    )
    prep_profile_descriptions = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    profile_descriptions = tinymce_models.HTMLField()
    others_right_side_profile = tinymce_models.HTMLField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Philanthropist"
        verbose_name_plural = "Philanthropists"


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
