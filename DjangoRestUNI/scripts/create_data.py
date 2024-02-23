import django
import os
import sys
from django.core.files import File

sys.path.append(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE","DjangoRestUNI.settings")
django.setup()

from Career.models import College, Career

def initialize_data():
    # Creacion de Facultades
    FAUA = College.objects.create(name='Facultad de Arquitectura, Urbanismo y Arte', short_name='FAUA')
    FIA = College.objects.create(name='Facultad de Ingeniería Ambiental', short_name='FIA')
    FIIS = College.objects.create(name='Facultad de Ingeniería Industrial y de Sistemas', short_name='FIIS')
    FIEE = College.objects.create(name='Facultad de Ingeniería Eléctrica y Electrónica', short_name='FIEE')
    FIP = College.objects.create(name='Facultad de Ingeniería de Petróleo, Gas Natural y Petroquímica', short_name='FIP')
    FIQT = College.objects.create(name='Facultad de Ingeniería Química y Textil', short_name='FIQT')
    FC = College.objects.create(name='Facultad de Ciencias', short_name='FC')
    FIGMM = College.objects.create(name='Facultad de Ingeniería Geológica Minera y Metalúrgica', short_name='FIGMM')
    FIC = College.objects.create(name='Facultad de Ingeniería Civil', short_name='FIC')
    FIEECS = College.objects.create(name='Facultad de Ingeniería Económica, Estadística y Ciencias Sociales', short_name='FIEECS')
    FIM = College.objects.create(name='Facultad de Ingeniería Mecánica', short_name='FIM')

    # Creacion de Carreras
    Arquitectura = Career.objects.create(name = 'Arquitectura',college = FAUA)
    Ingeniería_Física = Career.objects.create(name='Ingeniería Física', college=FC)
    Química = Career.objects.create(name='Química', college=FC)
    Física = Career.objects.create(name='Física', college=FC)
    Matemática = Career.objects.create(name='Matemática', college=FC)
    Ciencia_de_la_Computación = Career.objects.create(name='Ciencia de la Computación', college=FC)
    
    Ingeniería_Sanitaria = Career.objects.create(name='Ingeniería Sanitaria', college=FIA)
    Ingeniería_de_Higiene_y_Seguridad_Industrial = Career.objects.create(name='Ingeniería de Higiene y Seguridad Industrial', college=FIA)
    Ingeniería_Ambiental = Career.objects.create(name='Ingeniería Ambiental', college=FIA)
    
    Ingeniería_Civil = Career.objects.create(name='Ingeniería Civil', college=FIC)
    
    Ingeniería_Económica = Career.objects.create(name='Ingeniería Económica', college=FIEECS)
    Ingeniería_Estadística = Career.objects.create(name='Ingeniería Estadística', college=FIEECS)
    
    Ingeniería_Eléctrica = Career.objects.create(name='Ingeniería Eléctrica', college=FIEE)
    Ingeniería_Electrónica = Career.objects.create(name='Ingeniería Electrónica', college=FIEE)
    Ingeniería_de_Telecomunicaciones = Career.objects.create(name='Ingeniería de Telecomunicaciones', college=FIEE)
    Ingeniería_de_Ciberseguridad =  Career.objects.create(name='Ingeniería de Ciberseguridad', college=FIEE)

    Ingeniería_de_Minas = Career.objects.create(name='Ingeniería de Minas', college=FIGMM)
    Ingeniería_Geológica = Career.objects.create(name='Ingeniería Geológica', college=FIGMM)
    Ingeniería_Metalúrgica = Career.objects.create(name='Ingeniería Metalúrgica', college=FIGMM)
    
    Ingeniería_Industrial = Career.objects.create(name='Ingeniería Industrial', college=FIIS)
    Ingeniería_de_Sistemas = Career.objects.create(name='Ingeniería de Sistemas', college=FIIS)
    Ingeniería_de_Software = Career.objects.create(name='Ingeniería de Software', college=FIIS)
    
    Ingeniería_Mecánica = Career.objects.create(name='Ingeniería Mecánica', college=FIM)
    Ingeniería_Mecánica_Eléctrica = Career.objects.create(name='Ingeniería Mecánica-Eléctrica', college=FIM)
    Ingeniería_Naval = Career.objects.create(name='Ingeniería Naval', college=FIM)
    Ingeniería_Mecatrónica = Career.objects.create(name='Ingeniería Mecatrónica', college=FIM)
    
    Ingeniería_de_Petróleo = Career.objects.create(name='Ingeniería de Petróleo', college=FIP)
    Ingeniería_Petroquímica = Career.objects.create(name='Ingeniería Petroquímica', college=FIP)
    
    Ingeniería_Química = Career.objects.create(name='Ingeniería Química', college=FIQT)
    Ingeniería_Textil = Career.objects.create(name='Ingeniería Textil', college=FIQT)




initialize_data()