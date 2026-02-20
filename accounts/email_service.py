import logging
from django.core.mail import send_mail
from django.conf import settings

logger = logging.getLogger(__name__)


class EmailService:
    """Reusable email notification service for all auth events."""

    @staticmethod
    def _send(subject, message, recipient_email):
        """Internal helper — sends email and gracefully handles failures."""
        try:
            send_mail(
                subject=subject,
                message=message,
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=[recipient_email],
                fail_silently=False,
            )
            logger.info(f"Email sent to {recipient_email}: {subject}")
            return True
        except Exception as e:
            logger.warning(f"Email failed to {recipient_email}: {e}")
            return False

    @classmethod
    def send_welcome_email(cls, user):
        """Sent after successful registration."""
        cls._send(
            subject="Store | Welcome to Our Store!",
            message=(
                f"Hi {user.first_name or user.email},\n\n"
                f"Welcome aboard! Your account has been created successfully.\n\n"
                f"You can now browse our premium collections, add items to your cart, "
                f"and enjoy a seamless shopping experience.\n\n"
                f"If you have any questions, feel free to reach out.\n\n"
                f"Happy Shopping!\n"
                f"— The Store Team"
            ),
            recipient_email=user.email,
        )

    @classmethod
    def send_login_notification(cls, user):
        """Sent when a user successfully logs in."""
        from datetime import datetime
        login_time = datetime.now().strftime("%B %d, %Y at %I:%M %p")
        cls._send(
            subject="Store | New Login to Your Account",
            message=(
                f"Hi {user.first_name or user.email},\n\n"
                f"A new login to your account was detected on {login_time}.\n\n"
                f"If this was you, no action is needed.\n"
                f"If you did not log in, please change your password immediately.\n\n"
                f"Stay safe!\n"
                f"— The Store Team"
            ),
            recipient_email=user.email,
        )

    @classmethod
    def send_logout_notification(cls, user):
        """Sent when a user logs out."""
        cls._send(
            subject="Store | You've Been Logged Out",
            message=(
                f"Hi {user.first_name or user.email},\n\n"
                f"You have been successfully logged out of your Store account.\n\n"
                f"See you again soon!\n"
                f"— The Store Team"
            ),
            recipient_email=user.email,
        )

    @classmethod
    def send_order_confirmation(cls, user, order):
        """Sent when a user successfully places an order."""
        items_text = ""
        for item in order.items.all():
            items_text += f"  • {item.product.name} × {item.quantity} — ${item.price}\n"

        cls._send(
            subject=f"Store | Order #{order.id} Confirmed",
            message=(
                f"Hi {user.first_name or user.email},\n\n"
                f"Great news! Your order has been placed successfully.\n\n"
                f"Order #{order.id}\n"
                f"─────────────────────────\n"
                f"{items_text}\n"
                f"Total: ${order.total_amount}\n"
                f"Status: {order.status}\n\n"
                f"We'll notify you when your order ships.\n\n"
                f"Thank you for shopping with us!\n"
                f"— The Store Team"
            ),
            recipient_email=user.email,
        )
