# from django.contrib.auth import get_user_model
# from django.db.models.signals import post_save
# from django.dispatch import receiver
#
# from cosmetics_store import settings
# from cosmetics_store.accounts.utils import send_email
#
# UserModel = get_user_model()
#
#
# @receiver(post_save, sender=UserModel)
# def successful_created_user_sent_email(sender, instance, created, **kwargs):
#     if created:
#         context = {
#             "user": instance,
#         }
#         send_email(
#             subject="Welcome!",
#             from_email=settings.EMAIL_HOST_USER,
#             recipient_list=(instance.email, ),
#             template_name="emails/welcome.html",
#             context=context,
#         )
#         print("sent")