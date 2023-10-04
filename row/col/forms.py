from django import forms
from .models import Resume


class DateInput(forms.DateInput):
    input_type = 'date'


GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female')
]

COURSES_CHOICE = [
    ('Python', 'Python'),
    ('Java', 'Java'),
    ('DotNet', 'DotNet'),
    ('C and Cpp', 'C and Cpp'),
    ('Php', 'Php')
]


class ResumeForm(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)
    courses = forms.MultipleChoiceField(label='Selective Courses', choices=COURSES_CHOICE,
                                        widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Resume
        fields = '__all__'

        labels = {
            'name': 'Full Name',
            'dob': 'Date of Birth',
            'gender': 'Gender',
            'locality': 'Locality',
            'city': 'City',
            'pin_code': 'Pin code',
            'state': 'State',
            'mobile': 'Phone Number',
            'email': 'Email ID',
            'courses': 'Selective Courses'
        }

        widgets = {


            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'dob': DateInput(attrs={'class': 'form-control'}),
            'gender': forms.TextInput(attrs={'class': 'form-control'}),
            'locality': forms.TextInput(attrs={'class': 'form-control'}),
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'pin_code': forms.NumberInput(attrs={'class': 'form-control'}),
            'state': forms.Select(attrs={'class': 'form-control'}),
            'mobile': forms.NumberInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'courses': forms.TextInput(attrs={'class': 'form-control'})

        }
