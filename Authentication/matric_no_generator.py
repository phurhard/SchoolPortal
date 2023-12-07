import random
from datetime import datetime
from main.models import CustomUser, Student, Teacher
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404


def matric_no(request, data):
    '''Returns a matric number in this format
    yy/acronymOfSchool/acronymOfName+RegNumber
    e.g
    23/ALIS/ABY213'''
    today = datetime.now()
    year = today.strftime('%y')
    school = 'ALIS'
    name = data.first_name[:3]
    # name = request.user.get('first_name')[:3]
    try:
        user = get_object_or_404(CustomUser, id=data)
        if user.student:
            all_std = Student.objects.all()
            std = len(all_std)
            last_std = all_std[std - 1].id
    except ObjectDoesNotExist:
        pass
    return number