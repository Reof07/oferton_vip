from django.contrib import admin

from .models import Store, Location, Phone, SocialMedia

# Register your models here.

@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    list_display = ("id","name_store", "rif_store")

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ("id","state", "municipality", "city","addres","store")

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ("id","type_phone", "phone_number")

@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ("id","name_social_media", "url")