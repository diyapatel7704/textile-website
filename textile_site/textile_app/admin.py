from django.contrib import admin

from .models import (
    Business,
    Product,
    Enquiry,
    Infrastructure,
    WhyChooseUs,
    Testimonial
)

admin.site.register(Business)
admin.site.register(Product)
admin.site.register(Enquiry)
admin.site.register(Infrastructure)
admin.site.register(WhyChooseUs)
admin.site.register(Testimonial)