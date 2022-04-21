# Descripción
En este repositorio, se encuentran los códigos utilizados para automatizar el registro de usuario, el ingreso de usuario, el cambio de contraseña, el recuperar la contraseña y tambien usar fuerza bruta para el ingreso a una cuenta, en dos paginas web, una chilena y otra francesa. El código fue escrito en Python, en conjunto con el entorno de prueba Selenium.

Para poder ejecutar estos codigos de debe tener instalado Selenium y tambien haber descargado chromedriver. El ejecutable de chromedriver debe estar en la misma carpeta donde estan los codigos.

Las paginas auditadas fueron las siguientes:
* sitio Frances: https://www.rueducommerce.fr/
* sitio Chileno: https://www.reebok.cl/


## Desarrollo Actividades

#### 1) Registro

Para automatizar el registro de los sitios web, se utilizaron los codigos indicados a continuación:

* sitio Frances: LoginRuedu.py
* sitio Chileno: LoginReebok.py

#### 2) Login

Para automatizar el login de los sitios web, se utilizaron los codigos indicados a continuación:

* sitio Frances: RegistroRuedu.py
* sitio Chileno: RegistroReebok.py

##### 3) Cambio de contraseña

Para automatizar el cambio de contraseña de los sitios web, se utilizaron los codigos indicados a continuación:

* sitio Frances: CambioContraseniaRuedu.py
* sitio Chileno: CambioContraseniaReebook.py

#### 4) Recuperar contraseña

Para automatizar la recuperación de contraseña de los sitios web, se utilizaron los codigos indicados a continuación:

* sitio Frances: RecuperarContraseniaRuedu.py
* sitio Chileno: RecupererContraseniaReebok.py

Cabe mencionar que en ambos sitios, fue posible automatizar la recuperación de la contraseña hasta el punto de, que llegara el link al correo para recuperar contraseña, como se muestra en las siguientes imagenes:

![correo](images/recuperarContrasenia.png)

#### 5) Fuerza bruta en login

Para aplicar fuerza bruta en el login de los sitios web, se utilizaron los codigos indicados a continuación:

* sitio Frances: LoginFuerzaBrutaRuedu.py
* sitio Chileno: LoginFuerzaBrutaReebok.py

