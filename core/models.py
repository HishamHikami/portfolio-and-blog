from django.db import models
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field
from django.urls import reverse

# Create your models here.

RATING = (
    (1,  "★☆☆☆☆"),
    (2,  "★★☆☆☆"),
    (3,  "★★★☆☆"),
    (4,  "★★★★☆"),
    (5,  "★★★★★"),
)

STATUS = (
    ("draft", "Draft"),
    ("in_review", "In Review"),
    ("published", "Published"),
)
    
class Technology(models.Model):
    title = models.CharField(max_length=70, default="Logo")
    logo = models.ImageField(upload_to="tech-logos", default='tech-logo.png')

    class Meta:
        verbose_name_plural = "Technologies"

    def __str__(self):
        return self.title

class Service(models.Model):
    name = models.CharField(max_length=40, default="Service")
    heading_h1 = models.CharField(max_length=60)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.CharField(max_length=550)
    cover = models.ImageField(upload_to='services', default='service.jpg')
    status = models.CharField(choices=STATUS, max_length=20, default="draft")
    date = models.DateField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('core:service_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name_plural = "Services"

    def __str__(self):
        return self.heading_h1

class ServiceHighlight(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='service_highlight')
    highlight = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Highlights"

    def __str__(self):
        return self.highlight
    
class ServiceSection1(models.Model):
    service = models.OneToOneField(Service, on_delete=models.CASCADE, related_name='service_section_1')
    heading_h2 = models.CharField(max_length=150)
    paragraph_1 = models.TextField(max_length=1000)
    heading_h3 = models.CharField(max_length=150)
    paragraph_1_1 = models.TextField(max_length=1000)
    image_1 = models.ImageField(upload_to='services', default='service-1.jpg')
    image_2 = models.ImageField(upload_to='services', default='service-2.jpg')

    class Meta:
        verbose_name_plural = "Service Section 1"

    def __str__(self):
        return self.heading_h2
    
class ServiceTechnicalHighlight(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='technical_highlight')
    technical = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Tech Highlights"

    def __str__(self):
        return self.technical
    
class ServiceSection2(models.Model):
    service = models.OneToOneField(Service, on_delete=models.CASCADE, related_name='service_section_2')
    heading_h2 = models.CharField(max_length=150)
    paragraph_1 = models.TextField(max_length=1000)
    image_1 = models.ImageField(upload_to='services', default='service-3.jpg')

    class Meta:
        verbose_name_plural = "Service Section 2"

    def __str__(self):
        return self.heading_h2

class ServiceFAQ(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='faqs')
    question = models.CharField(max_length=200)
    answer = models.TextField(max_length=1000)

    class Meta:
        verbose_name_plural = "FAQs"

    def __str__(self):
        return self.question
    
class CSCategory(models.Model):
    title = models.CharField(max_length=40)
    slug = models.SlugField(blank=True, null=True, unique=True, max_length=80)
    description = models.CharField(max_length=160, default="Description")
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
    title = models.CharField(max_length=40, default="Company")
    slug = models.SlugField(blank=True, null=True, unique=True, max_length=80)
    short_description = models.CharField(max_length=160, null=True, blank=True)
    image = models.ImageField(upload_to='case-studies', default='case-study.jpg')
    link = models.URLField(null=True, blank=True)
    category = models.ForeignKey(CSCategory, on_delete=models.SET_NULL, null=True)
    date = models.DateField(auto_now_add=True)
    heading = models.CharField(max_length=100, null=True, blank=True)
    description = CKEditor5Field(config_name='extends', null=True, blank=True)
    status = models.CharField(choices=STATUS, max_length=20, default="draft")

    def clean_title(self):
        self.title = self.title.strip()
        return self.title.replace(" ", "-").lower()

    def save(self, *args, **kwargs):
        clean_title = self.clean_title()
        self.slug = f"{clean_title}-{self.pk}"
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('core:case-study', kwargs={'slug': self.slug})

    class Meta:
        verbose_name_plural = "Case Studies"

    def __str__(self):
        return self.title

class FAQ(models.Model):
    question = models.CharField(max_length=100, default="How helps?")
    answer = models.CharField(max_length=550, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Homepage FAQs"

    def __str__(self):
        return self.question
    
class Testimonial(models.Model):
    name = models.CharField(max_length=40, default="John Doe")
    profession = models.CharField(max_length=40, default="Engineer")
    message = models.CharField(max_length=600, null=True, blank=True)
    rating = models.IntegerField(choices=RATING, default=None)

class Contact(models.Model):
    full_name = models.CharField(max_length=40, default="John Doe")
    email = models.CharField(max_length=40, default="john@email.com")
    phone = models.CharField(max_length=40, default="+1 234567890")
    subject = models.CharField(max_length=200, null=True, blank=True)
    message = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.full_name
    
class ServicePageLead(models.Model):
    name = models.CharField(max_length=40, default="John Doe")
    phone = models.CharField(max_length=40, default="+1 234567890")
    message = models.TextField(null=True, blank=True)
    page_url = models.URLField(max_length=200, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Service Page Leads"

    def __str__(self):
        return self.name
    
class GetQuote(models.Model):
    email = models.CharField(max_length=40, default="john@email.com")

    class Meta:
        verbose_name_plural = "Quotation Requests"

    def __str__(self):
        return self.email

class SEOHomepage(models.Model):
    title = models.CharField(max_length=80, default="SEO title")
    description = models.CharField(max_length=160, default="SEO description")
    canonical = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Homepage Metadata"

    def __str__(self):
        return self.title