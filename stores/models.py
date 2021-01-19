from django.core.validators import RegexValidator

from django.db import models

# Create your models here.

class TimeStampedModel(models.Model):
    """
        An abstract base class model that provides selfupdating ``created``
        and ``updated`` fields.
    """
    created_at = models.DateTimeField('created_at', auto_now_add=True)
    updated_at = models.DateTimeField('updated_at', auto_now=True)


    class Meta:
        abstract = True


#
class Store(TimeStampedModel):

    name_store = models.CharField('name', max_length=100)
    rif_store = models.CharField('rif', max_length=15, blank=True)
    description = models.TextField('description', max_length=2000, blank=True)
    email = models.EmailField('email', blank=True)
    logo_store = models.ImageField('logo', upload_to='store/logo', blank=True) 
    banner_store = models.ImageField('banner', upload_to='store/banner', blank=True)

    class Meta:
        verbose_name = 'store'
        verbose_name_plural = 'stores'

    def __str__(self):
        return self.name_store
    
    def get_absolute_url(self):
        return reverse('store_details', kwargs={'pk': self.id})

#
class Location(TimeStampedModel):

    state = models.CharField('state', max_length=100)
    municipality = models.CharField('municipality', max_length=100)
    city = models.CharField('city', max_length=100)
    addres = models.CharField('addres', max_length=200, blank=True)
    postal_code = models.CharField('postal code', max_length=6, blank=True)
    store = models.ForeignKey(Store,  on_delete=models.CASCADE,
                    related_name='locations')
    

    class Meta:
        verbose_name = 'location'
        verbose_name_plural = 'locations'

    def __str__(self):
        return self.city


#
class Phone(TimeStampedModel):

    type_phone = models.CharField('type phone', max_length=50, default='cell phone')
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    phone_number = models.CharField(validators=[phone_regex], 
                    max_length=17, blank=True) # validators should be a list
    store = models.ForeignKey(Store,  on_delete=models.CASCADE,
                    related_name='phones')

    class Meta:
        verbose_name = 'phone'
        verbose_name_plural = 'phones'

    def __str__(self):
        return self.type_phone  

#
class SocialMedia(TimeStampedModel):

    name_social_media = models.CharField('social media', max_length=50)
    url = models.URLField ('url', max_length = 200, blank=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE, 
                related_name='socialmedias')


    class Meta:
        verbose_name = 'social media'
        verbose_name_plural = 'social media'

    def __str__(self):
        return self.name_social_media