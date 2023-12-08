# from main.models import Teacher, Student, Grade, Subject, ContinousAssessment
import random
# feed teacher
def gen_name():
    number = random.randint(1, 10)
    first_name = 'Fuhad'
    last_name = 'Yusuf'
    other_name = 'Django'
    email = 'sample@email.com'
    password = 'admin321'
    phone_number = '08056336247'
    return {
        'number': number,
        'first_name': first_name,
        'last_name': last_name,
        'other_name': other_name,
        'email': email,
        'password': password,
        'phone_number': phone_number
    }

# feed
# def Teacher():
#     teachers = Teacher.objects.create()

print(gen_name())