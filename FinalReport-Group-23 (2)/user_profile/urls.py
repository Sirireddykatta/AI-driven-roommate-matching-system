from django.urls import path

from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    
     # 1. Lifestyle and Routine
    path('lifestyle-routine/add/', views.lifestyle_routine_create, name='lifestyle_routine_create'),
     # 2. Cleanliness and Tidiness
    path('cleanliness-tidiness/add/', views.cleanliness_tidiness_create, name='cleanliness_tidiness_create'),
     # 3. Social Habits
    path('social-habits/add/', views.social_habits_create, name='social_habits_create'),
     # 4. Noise and Personal Space
    path('noise-personal-space/add/', views.noise_personal_space_create, name='noise_personal_space_create'),

    # 5. Financial Responsibility
    path('financial-responsibility/add/', views.financial_responsibility_create, name='financial_responsibility_create'),

    # 6. Pets
    path('pets/add/', views.pets_create, name='pets_create'),

    # 7. Smoking/Drinking Habits
    path('smoking-drinking/add/', views.smoking_drinking_create, name='smoking_drinking_create'),

    # 8. Shared Interests and Hobbies
    path('shared-interests-hobbies/add/', views.shared_interests_hobbies_create, name='shared_interests_hobbies_create'),

    # 9. Expectations and House Rules
    path('expectations-house-rules/add/', views.expectations_house_rules_create, name='expectations_house_rules_create'),
    # 10. Personal Details
    path('personal-details/update/', views.update_personal_details, name='update_personal_details'),

  
]
r =  """
    

   

   

    """