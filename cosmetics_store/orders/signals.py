from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from cosmetics_store import settings
from cosmetics_store.core.utils import send_email
from cosmetics_store.orders.models import OrderModel


@receiver(post_save, sender=OrderModel)
def order_confirm_sent_email(sender, instance, created, **kwargs):
    if not created and instance.is_ordered is True:
        context = {
            "user": instance.user,
            "order": instance,
        }

        send_email(
            subject="Order confirmation",
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[instance.user.email,],
            template_name="emails/placed_order.html",
            context=context,
        )