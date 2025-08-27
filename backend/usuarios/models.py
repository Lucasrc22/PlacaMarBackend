#Esse é o arquivo de modelos do Django, onde você define como serão representados os dados no banco de dados.

from django.contrib.auth.models import AbstractUser #É a classe base do Django que já vem com um modelo de usuário pronto...
                                                    #...(com campos como username, password, first_name, last_name, etc.).
from django.db import models #É o módulo do Django que contém os tipos de campos para criar tabelas no banco de dados.

class Usuario(AbstractUser): 
    email = models.EmailField(unique=True)

#Aqui você está herdando do AbstractUser. 
#Isso significa que o seu modelo Usuario vai ter todos os campos de usuário padrão do Django.
#O campo 'email', que é uma variável,está sendo subescrito para garantir que ele seja único no banco (unique=True).
    #Isso impede que dois usuários tenham o mesmo e-mail.

    USERNAME_FIELD = "username" #define qual campo será usado para login. Aqui está como "username", ...
                                #... ou seja, o login será feito com o nome de usuário.

    REQUIRED_FIELDS = ["email"] #Campos que o Django vai exigir quando você criar um usuário pelo comando createsuperuser.

#Neste caso, além de username e password (que já são padrão), ele vai pedir também email.

#-----------------Representação do objeto:

    def __str__(self):
        return self.username

#Define como o objeto Usuario vai ser mostrado em lugares como o Django Admin.
#Aqui ele mostra o username do referido usuário.



#*Em caso dos comentários estiverem representados de maneira equivocada, ...
#... qualquer dev presente pode ficar à vontade de agregar com as devidas correções.