from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].help_text=''
        self.fields['password2'].help_text=''


class DietForm(forms.Form):
    DIET_CHOICES = (
        ('anything', 'Anything'),
        ('vegetarian', 'Vegetarian'),
        ('vegan', 'Vegan'),
        ('pescatarian', 'Pescatarian'),
        ('flexitarian', 'Flexitarian'),
        # Add more diet types as needed
    )
    diet_type = forms.ChoiceField(choices=DIET_CHOICES, widget=forms.RadioSelect)


class AllergyForm(forms.Form):
    ALLERGIES = (
        ('gluten', 'Gluten'),
        ('peanuts', 'Peanuts'),
        ('eggs', 'Eggs'),
        ('fish', 'Fish'),
        ('dairy', 'Dairy'),
        # Add more diet types as needed
    )

    allergies = forms.MultipleChoiceField(choices=ALLERGIES, widget=forms.CheckboxSelectMultiple, required=False)


class PersonalInformationForm(forms.Form):
    GOAL = (
        ('lose_fat', 'Lose Fat'),
        ('maintain_weight', 'Maintain Weight'),
        ('build_muscle', 'Build Muscle'),
        # Add more diet types as needed
    )

    goal = forms.ChoiceField(choices=GOAL, widget=forms.RadioSelect)

    SEX = (
        ('male', 'Male'),
        ('female', 'Female'),
        # Add more diet types as needed
    )

    sex = forms.ChoiceField(choices=SEX, widget=forms.RadioSelect)

    height = forms.IntegerField(label="Height (cm)")
    weight = forms.IntegerField(label="Weight (kg)")
    age = forms.IntegerField(label="Age (years)")

    ACTIVITY = (
        ('sedentary', 'Sedentary (Office Job)'),
        ('light_exercise', 'Light Exercise (1-2 days/week)'),
        ('moderate_exercise', 'Moderate Exercise (3-5 days/week)'),
        ('heavy_exercise', 'Heavy Exercise (6-7 days/week)'),
        ('athlete', 'Athlete (2x per day )'),
        # Add more diet types as needed
    )

    activity = forms.ChoiceField(choices=ACTIVITY, widget=forms.Select)
