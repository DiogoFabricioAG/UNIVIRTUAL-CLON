# Instalacion del Proyecto
![image](https://github.com/DiogoFabricioAG/UNIVIRTUAL-CLON/assets/126220077/61032a5b-1f6e-4a81-a982-1aee0a52e946)
## Instalación del Backend
Para utilizar el backend de Django es necesario tener lo siguiente:
- Python v3.12.1 [Click](https://www.python.org/downloads/release/python-3121/)
- Visual Studio Code (de preferencia) [Click](https://code.visualstudio.com)
### Pasos
1. Clonar/Descargar el repositorio (Con el comando en Git: git clone https://github.com/DiogoFabricioAG/UNIVIRTUAL-CLON.git /En el boton verde donde dice "code")
2. Ingresar a la carpeta con Visual Studio Code (Dentro de la carpeta creada)
3. Ingresar alguno de estos comandos por terminal: python -m venv env (Este), py -m venv env (O este). Solo uno de ellos, si da algun error probar con el otro.
4. Ingresar el siguiente comando por la misma terminal: .\env\Scripts\activate
5. Si aparece (env) al lado de tu ruta en la terminal colocar cd DjangoRestUNI (Para ingresar a la carpeta del mismo nombre)
6. Colocar el siguiente comando en el terminal: pip install -r requirements.txt
7. Finalmente, ingresar el siguiente comando: python ./manage.py migrate
8. Ahora ya estaria todo configurado, ingresar el comando: python ./manage.py runserver
Con esto iniciamos el Backend.

## Instalación del Frontend
El frontend esta alojado en el siguiente link https://univirtualplatform.netlify.app

Pero tambien puedes utilizar el frontend de manera local, para eso deberas instalar https://nodejs.org/en/download/current escoge tu sistema operativo. Si ya tienes node Js y npm obviar este paso.
1. Abrir otra terminal y ingresar el siguiente comando: cd VueUNI
2. Luego descargas axios con el siguiente comando: npm install axios
3. Finalmente correr el programa con el siguiente comando: npm run dev
4. Ya con esto estaria configurado el programa y listo para usar.

### Imagen dentro del Programa
![image](https://github.com/DiogoFabricioAG/UNIVIRTUAL-CLON/assets/126220077/b57d22da-d006-4bcb-9a37-3c26ad7a0260)

Una cosa mas, para tener los datos de las Facultades y carreras, correr el script **create_data.py** que esta en la carpeta scripts dentro de la carpeta DjangoRestUNI. Con esto obtienes los datos de las carreras para que puedan ser usadas a la hora de crear cursos en con el rol de Profesor.
