from django.shortcuts import render
from .alg import RoommateMatchingAlgorithm
from user_profile.models import User
def match_users(request):
    # Get the logged-in user's profile
    current_user = request.user
    
    # Collect all user profiles (excluding the logged-in user)
    profiles = User.objects.exclude(id=current_user.id)
    
    # Initialize the matching algorithm
    algo = RoommateMatchingAlgorithm()
    algo.fit(profiles)

    # Fetch the current user's profile and find the top 20 matches
    current_user_profile = User.objects.get(id=current_user.id)
    top_matches = algo.find_matches(current_user_profile, profiles)
    print(top_matches)
    # Prepare data for the HTML table
    match_data = []
    for profile, score in top_matches:
        print(profile.first_name)
        match_data.append({
            'username': profile.username,
            'first_name': profile.first_name,
            'last_name': profile.last_name,
            'location': profile.location,
            'score': round(score, 2)  # Rounded match score
        })
        
        print(match_data)
        
        
    
    return render(request, 'algorithm/matches.html', {'matches': match_data})
