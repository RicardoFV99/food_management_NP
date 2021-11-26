# Sistema Food Management Version 1.0

**Equipo de Desarrollo**:
	- Isaac Alejandro Díaz López
	- Ricardo Flores Vázquez
	- Erick Alexandro Pinalez Gonzáles
	- Kevin Javier Reyes Medina

USO GENERAL
-----------

Para implementar el proyecto en un ambiente Windows, Ubuntu o MacOS es necesario contar con la dependencia de Django instalada en el sistema o en su entorno virtual.

Para instalar las dependencias del proyecto es necesario ingresar el siguiente comando:

```bash
$ pip install -r requirements.txt
```

o

```bash
$ python -m pip install -r requirements.txt
```

Si no se tiene instalado pip verifique que sus aplicaciones instaladas y vuelva a intentar.

Para crear e implementar las migraciones del proyecto es necesario ingresar el siguiente script:

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

Después de tener las migraciones del sistema implementados el proyecto puede ser ejecutado con el siguiente comando:

```bash
$ python manage.py runserver 0.0.0.0:8000
```

El puerto en donde se implementa puede ser modificado.

NOTAS
-----------

v1.0. El sistema funciona utilizando la tecnología SQLite3, además de necesitar dependencias de Python 3.7.x para su correcto funcionamiento. El desempeño en un entorno de implementación diferentes no está garantizado.

Copyright: Null Pointers 2021. All rights reserved.