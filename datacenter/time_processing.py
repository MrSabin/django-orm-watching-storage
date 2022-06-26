from django.utils import timezone


def get_duration(entered, leaved=False):
    if leaved:
        duration = timezone.localtime(leaved) - timezone.localtime(entered)
        return format_duration(duration)
    else:
        duration = timezone.localtime() - timezone.localtime(entered)
        return format_duration(duration)


def format_duration(duration):
    hours = duration.days * 24 + duration.seconds // 3600
    minutes = (duration.seconds % 3600) // 60
    seconds = (duration.seconds % 60)
    return f"{hours}:{minutes}:{seconds}"
