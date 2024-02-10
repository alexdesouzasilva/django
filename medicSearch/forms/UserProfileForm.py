from django.forms import ModelForm
from django import forms
from medicSearch.models.Profile import Profile

class UserProfileFrom(ModelForm):
    def __init__(self, *args, **kwargs):
        super(UserProfileFrom, self).__init__(*args, **kwargs)
        if self.instance and self.instance.role != 1:
            del self.fields['role']

    class Meta:
        model = Profile
        fields = ['user', 'role', 'birthday', 'image']
        #Usamos '__all__' para exibir todos os campos como items do formulário
        #fields = '__all__'
        widgets = {
            'user': forms.HiddenInput(),
            'role': forms.Select(attrs={'class': "form-control"}),
            'birthday': forms.DateInput(attrs={'class': "form-control", "type": "date"}),
            'image': forms.FileInput(attrs={'class': "form-control"})
        }
