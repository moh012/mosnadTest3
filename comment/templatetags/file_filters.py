from django import template

register = template.Library()


@register.filter
def is_image(file_url):
    return file_url.endswith(('.jpg', '.jpeg', '.png'))


@register.filter
def is_video(file_url):
    return file_url.endswith(('.mp4', '.avi', '.mov'))


@register.filter
def is_audio(file_url):
    return file_url.endswith(('.mp3', '.wav', '.ogg'))