from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, DietForm, AllergyForm, PersonalInformationForm
from .models import Profile
import openai
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            messages.success(request, f"Account created for {username}!")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)  # Log in the user
                # Redirect to a success page or any desired URL after successful registration and authentication
                return redirect('diet_form')
        
    else:    
        form = UserRegisterForm()

    return render(request, 'users/register.html', context={"form": form})


def diet_form_view(request):
    if request.method == 'POST':
        form = DietForm(request.POST)
        if form.is_valid():
            # Process the form data if needed
            selected_diet = form.cleaned_data['diet_type']
            # Redirect or perform actions based on the selected diet

        profile, created = Profile.objects.get_or_create(user=request.user)
        profile.diet = selected_diet
        profile.save()
        return redirect('allergy_form')
    else:
        form = DietForm()

    return render(request, 'users/diet_form.html', {'form': form})

def allergy_form_view(request):
    if request.method == 'POST':
        form = AllergyForm(request.POST)
        if form.is_valid():
            # Process the form data if needed
            selected_allergy = form.cleaned_data['allergies']
            # Redirect or perform actions based on the selected diet

        profile, created = Profile.objects.get_or_create(user=request.user)
        profile.allergy = selected_allergy
        profile.save()
        return redirect('personal_information_form')


    else:
        form = AllergyForm()

    return render(request, 'users/allergy_form.html', {'form': form})

def personal_information_form_view(request):
    if request.method == 'POST':

        form = PersonalInformationForm(request.POST)
        if form.is_valid():
            # Process the form data if needed
            selected_goal = form.cleaned_data['goal']
            selected_sex = form.cleaned_data['sex']
            selected_height = form.cleaned_data['height']
            selected_weight = form.cleaned_data['weight']
            selected_age = form.cleaned_data['age']
            selected_activity = form.cleaned_data['activity']
            # Redirect or perform actions based on the selected diet
        info = tdee_calculator(selected_goal, selected_sex, selected_height, selected_weight, selected_age, selected_activity)

        profile, created = Profile.objects.get_or_create(user=request.user)

        # Update or create fields based on the new data
        profile.age = selected_age
        profile.height = selected_height
        profile.weight = selected_weight
        profile.sex = selected_sex
        profile.goal = selected_goal
        profile.activity = selected_activity
        profile.protein = info['protein']
        profile.carbs = info['carbs']
        profile.fat = info['fat']
        profile.calories = info['calories']
        profile.save()
        return redirect('profile')

    else:
        form = PersonalInformationForm()

    return render(request, 'users/personal_information_form.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')


def tdee_calculator(selected_goal, selected_sex, selected_height, selected_weight, selected_age, selected_activity):
    activity_factors = {
        'sedentary': 1.2,
        'light_exercise': 1.375,
        'moderate_exercise': 1.55,
        'heavy_exercise': 1.725,
        'athlete': 1.9
    }

    # Calculating Basal Metabolic Rate (BMR) using the Harris-Benedict equation
    if selected_sex == 'male':
        bmr = 88.362 + (13.397 * selected_weight) + (4.799 * selected_height) - (5.677 * selected_age)
    else:
        bmr = 447.593 + (9.247 * selected_weight) + (3.098 * selected_height) - (4.330 * selected_age)

    # Applying activity factor to get TDEE
    fat = carbs = tdee = 0
    protein = selected_weight * 2.2 
    activity_factor = activity_factors[selected_activity]
    tdee = bmr * activity_factor
    if selected_goal == "build_muscle":
        tdee += 500
        fat = selected_weight*1.6
    elif selected_goal == "lose_fat":
        tdee -= 500
        fat = selected_weight*1.0
    elif selected_goal == "maintain_weight":
        fat = selected_weight * 1.3

    carbs = (tdee - (4*protein + 9*fat)) / 4
    
    return {
        "age": selected_age,
        "height": selected_height,
        "weight": selected_weight,
        "sex": selected_sex,
        "goal": selected_goal,
        "activity": selected_activity,
        "protein": protein,
        "carbs": carbs,
        "fat": fat,
        "calories": tdee
    }



# openai.api_key = redacted

def get_completion(prompt): 
    print(prompt) 
    query = openai.Completion.create( 
        engine="text-davinci-003", 
        prompt=prompt, 
        max_tokens=1024, 
        n=1, 
        stop=None, 
        temperature=0.5, 
    ) 
  
    response = query.choices[0].text 
    print(response) 
    return response 

@login_required
def query_view(request): 
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        prompt = f"Create a 7-day meal plan that includes meals totaling {profile.calories} calories. Ensure the meals avoid ingredients or foods related to any of the following allergies: {profile.allergy}."
        response = get_completion(prompt) 
        return JsonResponse({'response': response}) 
    return render(request, 'users/meal_plan.html') 
