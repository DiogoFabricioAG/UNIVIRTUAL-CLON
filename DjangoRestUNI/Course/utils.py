from User.models import User
from .models import Course

def add_new_member(user:User,course:Course):
    if user in course.professors.all() or user in course.students.all():
        raise 'El usuario ya se encuentra registrado en este curso'
    else:
        if user.role == 'Professor':
            course.professors.add(user)
        elif user.role == 'Student':
            course.students.add(user)
        course.save()
def set_admin(user:User,course:Course):
    course.admin = user
    course.save()

