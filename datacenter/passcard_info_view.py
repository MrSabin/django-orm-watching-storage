from datacenter.models import Passcard
from datacenter.models import is_visit_long
from datacenter.models import Visit
from datacenter.time_processing import get_duration, format_duration
from django.shortcuts import render
from django.utils import timezone


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)
    serialized_visits = []

    for visit in visits:
        time_passed = get_duration(visit.entered_at, visit.leaved_at)
        time_entered = timezone.localtime(visit.entered_at)
        flag = is_visit_long(visit)
        visit_details = {
            'entered_at': f'{time_entered}',
            'duration': f'{time_passed}',
            'is_strange': f'{flag}'
        }
        serialized_visits.append(visit_details)

    context = {
        'passcard': passcard,
        'this_passcard_visits': serialized_visits
    }
    return render(request, 'passcard_info.html', context)
