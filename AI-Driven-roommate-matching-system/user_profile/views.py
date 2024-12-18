from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from users.models import User
from django.contrib import messages
"""from .models import (
    LifestyleRoutine, CleanlinessTidiness, SocialHabits, NoisePersonalSpace,
    FinancialResponsibility, Pets, SmokingDrinking, SharedInterestsHobbies,
    ExpectationsHouseRules, PersonalDetails
)
"""
from .forms import (
    LifestyleRoutineForm, CleanlinessTidinessForm, SocialHabitsForm, 
    NoisePersonalSpaceForm, FinancialResponsibilityForm, PetsForm,
    SmokingDrinkingForm, SharedInterestsHobbiesForm, ExpectationsHouseRulesForm,
    PersonalDetailsForm
)


@login_required
def update_personal_details(request):
    user = request.user
 
    # Retrieve or create PersonalDetails instance for the user
    personal_details = User.objects.get(id= user.id)
    
    if request.method == 'POST':
        form = PersonalDetailsForm(request.POST, instance=personal_details)
        if form.is_valid():
            # Save the form data, user field will automatically be filled
            form.save()
            return redirect('profile')  # Redirect to a profile or success page
    else:
        form = PersonalDetailsForm(instance=personal_details)
    
    return render(request, 'profile/update.html', {'form': form,'title': 'Update Personal Details'})


# 1. Lifestyle and Routine
@login_required
def lifestyle_routine_create(request):
    user = request.user
    # Retrieve or create PersonalDetails instance for the user
    personal_details = User.objects.get(id= user.id)
    
    if request.method == 'POST':
        form = LifestyleRoutineForm(request.POST, instance=personal_details)
        print(request.POST.get('daily_scheduled'))
        if form.is_valid():
            # Save the form data, user field will automatically be filled
            form.save()
            return redirect('profile')  # Redirect to a profile or success page
    else:
        form = LifestyleRoutineForm(instance=personal_details)
    
    return render(request, 'profile/update.html', {'form': form,'title': 'Update Lifestyle Routine'})

# 2. Cleanliness and Tidiness
@login_required
def cleanliness_tidiness_create(request):
    user = request.user
    # Retrieve or create PersonalDetails instance for the user
    personal_details = User.objects.get(id= user.id)
    
    if request.method == 'POST':
        form = CleanlinessTidinessForm(request.POST, instance=personal_details)
       
        if form.is_valid():
            # Save the form data, user field will automatically be filled
            form.save()
            return redirect('profile')  # Redirect to a profile or success page
    else:
        form = CleanlinessTidinessForm(instance=personal_details)
    
    return render(request, 'profile/update.html', {'form': form,'title': 'Update Clealiness and Tidiness'})


# 3. Social Habits
@login_required
def social_habits_create(request):
    user = request.user
    # Retrieve or create PersonalDetails instance for the user
    personal_details = User.objects.get(id= user.id)
    
    if request.method == 'POST':
        form = SocialHabitsForm(request.POST, instance=personal_details)
       
        if form.is_valid():
            # Save the form data, user field will automatically be filled
            form.save()
            return redirect('profile')  # Redirect to a profile or success page
    else:
        form = SocialHabitsForm(instance=personal_details)
    
    return render(request, 'profile/update.html', {'form': form,'title': 'Update Social Habit'})
    
# 4. Noise and Personal Space
@login_required
def noise_personal_space_create(request):
    user = request.user
    # Retrieve or create PersonalDetails instance for the user
    personal_details = User.objects.get(id= user.id)
    
    if request.method == 'POST':
        form = NoisePersonalSpaceForm(request.POST, instance=personal_details)
       
        if form.is_valid():
            # Save the form data, user field will automatically be filled
            form.save()
            return redirect('profile')  # Redirect to a profile or success page
    else:
        form = NoisePersonalSpaceForm(instance=personal_details)
    
    return render(request, 'profile/update.html', {'form': form,'title': 'Update Noise and Personal Space'})
  

# 5. Financial Responsibility
@login_required
def financial_responsibility_create(request):
    user = request.user
    # Retrieve or create PersonalDetails instance for the user
    personal_details = User.objects.get(id= user.id)
    
    if request.method == 'POST':
        form = FinancialResponsibilityForm(request.POST, instance=personal_details)
       
        if form.is_valid():
            # Save the form data, user field will automatically be filled
            form.save()
            return redirect('profile')  # Redirect to a profile or success page
    else:
        form = FinancialResponsibilityForm(instance=personal_details)
    
    return render(request, 'profile/update.html', {'form': form,'title': 'Update Financial Resposibility'})
    

# 6. Pets
@login_required
def pets_create(request):
    user = request.user
    # Retrieve or create PersonalDetails instance for the user
    personal_details = User.objects.get(id= user.id)
    
    if request.method == 'POST':
        form = PetsForm(request.POST, instance=personal_details)
       
        if form.is_valid():
            # Save the form data, user field will automatically be filled
            form.save()
            return redirect('profile')  # Redirect to a profile or success page
    else:
        form = PetsForm(instance=personal_details)
    
    return render(request, 'profile/update.html', {'form': form,'title': 'Update Pets Details'})
  

# 7. Smoking/Drinking Habits
@login_required
def smoking_drinking_create(request):
    user = request.user
    # Retrieve or create PersonalDetails instance for the user
    personal_details = User.objects.get(id= user.id)
    
    if request.method == 'POST':
        form = SmokingDrinkingForm(request.POST, instance=personal_details)
       
        if form.is_valid():
            # Save the form data, user field will automatically be filled
            form.save()
            return redirect('profile')  # Redirect to a profile or success page
    else:
        form = SmokingDrinkingForm(instance=personal_details)
    
    return render(request, 'profile/update.html', {'form': form,'title': 'Update Smoking and Drinking Habits'})
  

# 8. Shared Interests and Hobbies
@login_required
def shared_interests_hobbies_create(request):
    user = request.user
    # Retrieve or create PersonalDetails instance for the user
    personal_details = User.objects.get(id= user.id)
    
    if request.method == 'POST':
        form = SharedInterestsHobbiesForm(request.POST, instance=personal_details)
       
        if form.is_valid():
            # Save the form data, user field will automatically be filled
            form.save()
            return redirect('profile')  # Redirect to a profile or success page
    else:
        form = SharedInterestsHobbiesForm(instance=personal_details)
    
    return render(request, 'profile/update.html', {'form': form,'title': 'Update Hobies'})
   

# 9. Expectations and House Rules
@login_required
def expectations_house_rules_create(request):
    user = request.user
    # Retrieve or create PersonalDetails instance for the user
    personal_details = User.objects.get(id= user.id)
    
    if request.method == 'POST':
        form = ExpectationsHouseRulesForm(request.POST, instance=personal_details)
       
        if form.is_valid():
            # Save the form data, user field will automatically be filled
            form.save()
            return redirect('profile')  # Redirect to a profile or success page
    else:
        form = ExpectationsHouseRulesForm(instance=personal_details)
    
    return render(request, 'profile/update.html', {'form': form,'title': 'Update House Rules'})
  



@login_required
def profile(request):
    user = request.user
    personal_details = User.objects.get(id= user.id)
    return render(request,'users/profile.html')