from .models import Quiz,QuizUserSolution,UserResumeCourse
from User.models import User
from Course.models import Course
from fpdf import FPDF
from fpdf import XPos
from fpdf import YPos
from django.core.files.base import ContentFile
from Notification.models import Notification

def get_higher_grade_for_a_quiz(iduser,idquiz):
    user = User.objects.get(pk = iduser)
    quiz = Quiz.objects.get(pk = idquiz)
    myAttempts = QuizUserSolution.objects.filter(user = user, quiz=quiz)
    myAttempts = sorted(myAttempts,key= lambda x: x.qualification,reverse=True)
    if len(myAttempts) !=0:
        return myAttempts[0]
    else:
        return 0
def set_final_grades(iduser,idcourse):
    user = User.objects.get(pk = iduser)
    course = Course.objects.get(pk = idcourse)
    myquizzes = course.quizzes.all().filter(state = 'Available')
    num_of_quizzes = len(myquizzes)
    grade = 0
    for quiz in myquizzes:
        try:
            grade+= get_higher_grade_for_a_quiz(user.id,quiz.id).qualification/quiz.total_points
        except:
            pass
    grade = grade/num_of_quizzes
    state = True
    if grade < 0.5:
        state = False
        UserResumeCourse.objects.create(user = user , course = course,grade_prom=grade*20,passed=state)
    else:
        pdf = FPDF(orientation='L',unit='mm',format=(866,1300))
        
        pdf.add_font('Blackadder','',r'C:/Windows/Fonts/ITCBLKAD.TTF',uni=True)
        pdf.set_page_background('./Images/Certificado.jpg')
        pdf.add_page()
        
        pdf.set_font('Blackadder','',150)
        pdf.set_text_color(0,0,0)
        pdf.cell(w=50,h=270,new_x=XPos.LMARGIN,new_y=YPos.NEXT,)
        pdf.cell(pdf.w,10,text = user.first_name + ' ' + user.last_name,align='C',new_x=XPos.LMARGIN,new_y=YPos.NEXT)
        pdf.cell(w=50,h=140,new_x=XPos.LMARGIN,new_y=YPos.NEXT,)
        pdf.cell(pdf.w,20,text = course.name,align='C',new_x=XPos.LMARGIN,new_y=YPos.NEXT)
        pdf.cell(pdf.w,70,text = 'Nota',align='C',new_x=XPos.LMARGIN,new_y=YPos.NEXT)
        pdf.cell(pdf.w,50,text = str(round(grade*20,4)),align='C',new_x=XPos.LMARGIN,new_y=YPos.NEXT)
        print(type(pdf))
        pdf_bytes = pdf.output(dest='S')
        user_resume_course = UserResumeCourse.objects.create(user = user , course = course,grade_prom=grade*20,passed=state)
        notification = Notification.objects.create(send_to = user, typenotification = f'El curso {course.name} ha terminado. Revisa el Apartado Certificados.')
        user_resume_course.certificate.save('certificate.pdf', ContentFile(pdf_bytes))
     