from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_email(subject, from_email, recipient_list, template_name, context):

    # renders an HTML email message by loading an email template; rendering it with the context
    html_message = render_to_string(template_name=template_name, context=context)

    # generates a plain text version of the email message by stripping HTML tags from the HTML
    plain_message = strip_tags(html_message)

    return send_mail(
        subject=subject,
        message=plain_message,
        html_message=html_message,
        from_email=from_email,
        recipient_list=recipient_list,
    )