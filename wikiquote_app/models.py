from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.text import slugify


from django.template.defaultfilters import slugify as django_slugify

alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
            'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
            'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'i', 'э': 'e', 'ю': 'yu',
            'я': 'ya'}

def slugify(s):
    """
    Overriding django slugify that allows to use russian words as well.
    """
    return django_slugify(''.join(alphabet.get(w, w) for w in s.lower()))

# Create your models here.



class Category(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(default='', null=False, db_index=True, max_length=250)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

class Article(models.Model):
    title = models.CharField(max_length=200)
    language = models.CharField(max_length=10)
    wiki = models.CharField(max_length=40)
    auxiliary_text = ArrayField(models.CharField(max_length=100), blank=True)
    create_timestamp = models.DateTimeField()
    timestamp = models.DateTimeField()

    category = models.ManyToManyField(Category, default=[])

    def __str__(self):
        return self.title



