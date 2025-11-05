# agenda/forms.py (Actualizado)

from django import forms
from .models import Task
from django.contrib.auth.forms import UserCreationForm # <-- ¡Importación nueva!
from django.contrib.auth.models import User

# --- Formulario de Tareas (se mantiene igual) ---
class TaskForm(forms.ModelForm):
    # ... (tu código TaskForm se mantiene aquí) ...
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date']
        # ... (widgets, labels)
        widgets = {
             # ... (tus widgets anteriores)
             'title': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500 transition duration-150',
                'placeholder': 'Ej: Llamar al electricista'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500 resize-none transition duration-150',
                'rows': 3,
                'placeholder': 'Detalles: Revisar presupuesto, comprar materiales...'
            }),
            'due_date': forms.DateInput(attrs={
                'type': 'date', 
                'class': 'w-full p-3 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500 transition duration-150'
            }),
        }
        labels = {
            'title': 'Título de la Tarea',
            'description': 'Descripción (Opcional)',
            'due_date': 'Fecha Límite (Opcional)',
        }


# --- NUEVO Formulario de Registro con estilos Tailwind ---
class UserSignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Aplicar clases de Tailwind a los campos
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-blue-500 focus:border-blue-500 transition duration-150',
            })
    
    class Meta:
        model = User
        fields = ('username',) # Puedes añadir 'email' si lo quieres, pero el UserCreationForm solo usa username y password.