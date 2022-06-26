from datacenter.models import Visit, is_visit_long
from django.shortcuts import render
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


def storage_information_view(request):
    opened_visits = Visit.objects.filter(leaved_at=None)
    serialized_visits = []
    for visit in opened_visits:
        time_passed = get_duration(visit.entered_at)
        time_entered = timezone.localtime(visit.entered_at)
        flag = is_visit_long(visit)
        visit_details = {
            'who_entered': f'{visit.passcard}',
            'entered_at': f'{time_entered}',
            'duration': f'{time_passed}',
            'flag': f'{flag}'}
        serialized_visits.append(visit_details)
    context = {
        'non_closed_visits': serialized_visits,
    }
    return render(request, 'storage_information.html', context)
