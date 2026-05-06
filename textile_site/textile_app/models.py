from django.db import models

# 🟢 BUSINESS MODEL (Company Info)
class Business(models.Model):
    name = models.CharField(max_length=200)
    owner_name = models.CharField(max_length=100)
    year_established = models.IntegerField()
    gst_number = models.CharField(max_length=20)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()

    # HERO SECTION
    tagline = models.CharField(max_length=300, blank=True, null=True)
    hero_description = models.TextField(blank=True, null=True)

    # TRUST SECTION
    years_experience = models.CharField(max_length=50, blank=True, null=True)
    happy_clients = models.CharField(max_length=50, blank=True, null=True)
    monthly_production = models.CharField(max_length=100, blank=True, null=True)
    delivery_area = models.CharField(max_length=100, blank=True, null=True)

    # ABOUT SECTION
    about_company = models.TextField(blank=True, null=True)

    # WHY CHOOSE US
    point1 = models.CharField(max_length=200, blank=True, null=True)
    point2 = models.CharField(max_length=200, blank=True, null=True)
    point3 = models.CharField(max_length=200, blank=True, null=True)
    point4 = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name


# 🟢 PRODUCT MODEL (Main Data)
class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    count_gsm = models.CharField(max_length=50)
    width = models.CharField(max_length=50, blank=True, null=True)
    colors = models.CharField(max_length=200)
    moq = models.CharField(max_length=50)
    packaging = models.CharField(max_length=200)
    usage = models.CharField(max_length=200)
    delivery_time = models.CharField(max_length=100)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name


# 🟢 INFRASTRUCTURE MODEL (Factory Details)
class Infrastructure(models.Model):
    factory_size = models.CharField(max_length=100)
    machines = models.IntegerField()
    machine_details = models.TextField()
    production_capacity = models.CharField(max_length=100)
    workers = models.IntegerField()
    quality_process = models.TextField()

    def __str__(self):
        return "Factory Details"


# 🟢 ENQUIRY MODEL (Contact Form Data)
class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    product = models.CharField(max_length=100)
    quantity = models.CharField(max_length=50, null=True, blank=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class WhyChooseUs(models.Model):

    title = models.CharField(max_length=200)

    description = models.TextField(
        blank=True,
        null=True
    )

    icon = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    def __str__(self):
        return self.title
        
class Testimonial(models.Model):

    client_name = models.CharField(max_length=100)

    company_name = models.CharField(max_length=100)

    review = models.TextField()

    def __str__(self):
        return self.client_name