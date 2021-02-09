from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.dispatch import receiver

import logging
stdlogger = logging.getLogger(__name__)

# @receiver(pre_save, sender='api.MovieRating')
# def run_before_saving(sender, **kwargs):
#     # breakpoint()