from django.db.models.signals import m2m_changed, post_save
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from accounts.models import CustomUser
from posts.models import Like, Post, Comment   # assuming you already have Comment
from .models import Notification


# --- FOLLOW NOTIFICATION ---
@receiver(m2m_changed, sender=CustomUser.following.through)
def create_follow_notification(sender, instance, action, pk_set, **kwargs):
    if action == "post_add":
        for user_id in pk_set:
            recipient = CustomUser.objects.get(pk=user_id)
            if recipient != instance:  # prevent self-follow
                Notification.objects.create(
                    recipient=recipient,
                    actor=instance,
                    verb="followed you",
                    target=recipient,
                    target_content_type=ContentType.objects.get_for_model(CustomUser),
                    target_object_id=recipient.id,
                )


# --- LIKE NOTIFICATION ---
@receiver(post_save, sender=Like)
def create_like_notification(sender, instance, created, **kwargs):
    if created and instance.post.author != instance.user:
        Notification.objects.create(
            recipient=instance.post.author,
            actor=instance.user,
            verb="liked your post",
            target=instance.post,
            target_content_type=ContentType.objects.get_for_model(Post),
            target_object_id=instance.post.id,
        )


# --- COMMENT NOTIFICATION ---
@receiver(post_save, sender=Comment)
def create_comment_notification(sender, instance, created, **kwargs):
    if created and instance.post.author != instance.author:
        Notification.objects.create(
            recipient=instance.post.author,
            actor=instance.author,
            verb="commented on your post",
            target=instance.post,
            target_content_type=ContentType.objects.get_for_model(Post),
            target_object_id=instance.post.id,
        )
