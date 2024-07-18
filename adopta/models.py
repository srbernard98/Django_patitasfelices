from django.db import models

class Usuario(models.Model):
    TIPO_USUARIO_CHOICES = [
        ('adoptante', 'Adoptante'),
        ('administrativo', 'Administrativo'),
    ]

    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=255)
    dirección = models.CharField(max_length=255)
    teléfono = models.CharField(max_length=20)
    tipo_usuario = models.CharField(max_length=20, choices=TIPO_USUARIO_CHOICES)

    def _str_(self):
        return f'{self.nombre} {self.apellido}'

class Mascota(models.Model):
    SEXO_CHOICES = [
        ('macho', 'Macho'),
        ('hembra', 'Hembra'),
    ]

    ESTADO_CHOICES = [
        ('disponible', 'Disponible'),
        ('adoptado', 'Adoptado'),
    ]

    nombre = models.CharField(max_length=255)
    especie = models.CharField(max_length=255)
    raza = models.CharField(max_length=255)
    edad = models.IntegerField()
    sexo = models.CharField(max_length=10, choices=SEXO_CHOICES)
    descripción = models.TextField()
    fecha_ingreso = models.DateField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES)

    def _str_(self):
        return self.nombre

class Adopcion(models.Model):
    ESTADO_ADOPCION_CHOICES = [
        ('en proceso', 'En proceso'),
        ('completada', 'Completada'),
        ('cancelada', 'Cancelada'),
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    fecha_adopcion = models.DateField()
    estado_adopcion = models.CharField(max_length=20, choices=ESTADO_ADOPCION_CHOICES)

    def _str_(self):
        return f'Adopción de {self.usuario} - {self.mascota}'

class Solicitud(models.Model):
    ESTADO_SOLICITUD_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('aprobada', 'Aprobada'),
        ('rechazada', 'Rechazada'),
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    fecha_solicitud = models.DateField()
    estado_solicitud = models.CharField(max_length=20, choices=ESTADO_SOLICITUD_CHOICES)

    def _str_(self):
        return f'Solicitud de {self.usuario} para {self.mascota}'

class Comentario(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    comentario = models.TextField()
    fecha_comentario = models.DateField()

    def _str_(self):
        return f'Comentario de {self.usuario} sobre {self.mascota}'

class Cita(models.Model):
    ESTADO_CITA_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('realizada', 'Realizada'),
        ('cancelada', 'Cancelada'),
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)
    fecha_cita = models.DateField()
    hora_cita = models.TimeField()
    estado_cita = models.CharField(max_length=20, choices=ESTADO_CITA_CHOICES)

    def _str_(self):
        return f'Cita de {self.usuario} para {self.mascota} el {self.fecha_cita} a las {self.hora_cita}'