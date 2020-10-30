from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from .models import Question
from core.utils import generate_random_string

@receiver(pre_save,sender=Question)
def add_slug_to_question(sender,instance,*args, **kwargs):
    if instance and not instance.slug:
        print("instance",instance)
        slug=slugify(instance.content )
        print("slug",slug)
        random_string=generate_random_string()
        instance.slug= slug + "-" + random_string





