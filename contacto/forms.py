from django import forms


class FormularioContacto(forms.Form):
    nombre = forms.CharField(label="Nombre", required=True, max_length=200)
    email = forms.EmailField(label="Email", required=True, max_length=200)
    contenido = forms.CharField(label="Contenido", required=True, widget=forms.Textarea)  # Campo de texto con varias líneas