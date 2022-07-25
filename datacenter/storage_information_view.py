from datacenter.models import Visit, is_visit_long
from datacenter.time_processing import format_duration, get_duration
from django.shortcuts import render
from django.utils import timezone


def storage_information_view(request):
    opened_visits = Visit.objects.filter(leaved_at=None)
    serialized_visits = []
    for visit in opened_visits:
        time_passed = get_duration(visit.entered_at)
        time_entered = timezone.localtime(visit.entered_at)
        is_strange = is_visit_long(visit)
        visit_details = {
            'who_entered': f'{visit.passcard}',
            'entered_at': f'{time_entered}',
            'duration': f'{time_passed}',
            'is_strange': f'{is_strange}'}
        serialized_visits.append(visit_details)
    context = {
        'non_closed_visits': serialized_visits,
    }
    return render(request, 'storage_information.html', context)
