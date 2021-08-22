from django.contrib import admin
from .models import *

# Register your models here.

class MaterialAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


class PersonaAdmin(admin.ModelAdmin):
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

class AlumnoInline(admin.StackedInline):
    model = Alumno
    extra = 0

class ProfesorInline(admin.StackedInline):
    model = Profesor
    extra = 0
    
class LibroInline(admin.StackedInline):
    model = Libro
    extra = 0

class RevistaInline(admin.StackedInline):
    model = Revista
    extra = 0

class PrestamoAdmin(admin.ModelAdmin):
    list_display = ['codigo','fechaSalida','fechaRegreso']
    list_display_links = ('codigo','fechaSalida', 'fechaRegreso')
    search_fields = ('codigo','fechaSalida', 'fechaRegreso')
    inlines = [AlumnoInline,ProfesorInline,LibroInline,RevistaInline]

class ProfesorAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Descripcion', {
          'fields': ('tipoPersona','nombre','apellido')  
        }),
        ('Datos', {
            'fields': ('correo','telefono',)
        }),
        ('Extra', {
          'fields': ('numLibros','adeudo','numEmpleado')  
        }),
    )
    list_display = ['numEmpleado',]
    list_display_links = ['numEmpleado',]
    search_fields = ['numEmpleado',]

class AlumnoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Descripcion', {
          'fields': ('tipoPersona','nombre','apellido')  
        }),
        ('Datos', {
            'fields': ('correo','telefono',)
        }),
        ('Extra', {
          'fields': ('numLibros','adeudo','matricula')  
        }),
    )
    list_display = ['matricula',]
    list_display_links = ['matricula',]
    search_fields = ['matricula',]

class LibroAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Descripcion', {
          'fields': ('tipoMaterial','autor','titulo','portada',)  
        }),
        ('Extra', {
            'fields': ('año','status','editorial','prestamo',)
        }),
    )
    list_display = ['tipoMaterial','autor','titulo','año','status','prestamo','editorial',]
    list_display_links = ['tipoMaterial','autor','titulo','año','status','prestamo','editorial',]
    search_fields = ['tipoMaterial','autor','titulo','año','status','prestamo','editorial',]

class RevistaAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Descripcion', {
          'fields': ('tipoMaterial','autor','titulo',)  
        }),
        ('Extra', {
            'fields': ('año','status',)
        }),
    )
    list_display = ['tipoMaterial','autor','titulo','año','status','prestamo']
    list_display_links = ['tipoMaterial','autor','titulo','año','status','prestamo']
    search_fields = ['tipoMaterial','autor','titulo','año','status','prestamo']

admin.site.register(Prestamo, PrestamoAdmin)
admin.site.register(Persona, PersonaAdmin)
admin.site.register(Profesor, ProfesorAdmin)
admin.site.register(Alumno, AlumnoAdmin)
admin.site.register(Material, MaterialAdmin)
admin.site.register(Libro, LibroAdmin)
admin.site.register(Revista, RevistaAdmin)
