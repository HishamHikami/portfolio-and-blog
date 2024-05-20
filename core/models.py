from django.db import models
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.

RATING = (
    (1,  "★☆☆☆☆"),
    (2,  "★★☆☆☆"),
    (3,  "★★★☆☆"),
    (4,  "★★★★☆"),
    (5,  "★★★★★"),
)
    
class Technology(models.Model):
    title = models.CharField(max_length=70, null=True, blank=True)
    logo = models.ImageField(upload_to="tech-logos", default='tech-logo.png')

    class Meta:
        verbose_name_plural = "Technologies"

    def __str__(self):
        return self.title

class Service(models.Model):
    heading = models.CharField(max_length=60)
    description = models.CharField(max_length=550)
    bootstrap_icon = models.CharField(max_length=35, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Services"

    def __str__(self):
        return self.heading
    
class CSCategory(models.Model):
    title = models.CharField(max_length=40, null=True, blank=True)
    slug = models.SlugField(blank=True, null=True, unique=True, max_length=80)
    description = models.CharField(max_length=160, null=True, blank=True)
    c_filter = models.CharField(max_length=15, null=True, blank=True)

    def clean_title(self):
        self.title = self.title.strip()  # Remove leading/trailing spaces
        return self.title.replace(" ", "-").lower()
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.clean_title())
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Case Study Categories"

    def __str__(self):
        return self.title
    
class CaseStudy(models.Model):
    title = models.CharField(max_length=40, null=True, blank=True)
    slug = models.SlugField(blank=True, null=True, unique=True, max_length=80)
    short_description = models.CharField(max_length=160, null=True, blank=True)
    image = models.ImageField(upload_to='case-studies', default='case-study.jpg')
    link = models.URLField(null=True, blank=True)
    category = models.ForeignKey(CSCategory, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateField(auto_now_add=True)
    heading = models.CharField(max_length=100, null=True, blank=True)
    description = CKEditor5Field(config_name='extends', null=True, blank=True)

    def clean_title(self):
        self.title = self.title.strip()
        return self.title.replace(" ", "-").lower()

    def save(self, *args, **kwargs):
        clean_title = self.clean_title()
        self.slug = f"{clean_title}-{self.pk}"
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Case Studies"

    def __str__(self):
        return self.title

class FAQ(models.Model):
    question = models.CharField(max_length=100, null=True, blank=True)
    answer = models.CharField(max_length=550, null=True, blank=True)

    class Meta:
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.question
    
class Testimonial(models.Model):
    name = models.CharField(max_length=40, null=True, blank=True)
    profession = models.CharField(max_length=40, null=True, blank=True)
    message = models.CharField(max_length=600, null=True, blank=True)
    rating = models.IntegerField(choices=RATING, default=None)

class Contact(models.Model):
    full_name = models.CharField(max_length=40, null=True, blank=True)
    email = models.CharField(max_length=40, null=True, blank=True)
    phone = models.CharField(max_length=40, null=True, blank=True)
    subject = models.CharField(max_length=200, null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.full_name
    
class GetQuote(models.Model):
    email = models.CharField(max_length=40, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Quotation Requests"

    def __str__(self):
        return self.email

class SEOHomepage(models.Model):
    title = models.CharField(max_length=80, null=True, blank=True)
    description = models.CharField(max_length=160, null=True, blank=True)
    canonical = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Homepage Metadata"

    def __str__(self):
        return self.title