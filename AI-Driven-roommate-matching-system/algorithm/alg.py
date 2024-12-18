from sklearn.neighbors import NearestNeighbors
import numpy as np

class RoommateMatchingAlgorithm:
    def __init__(self, n_neighbors=2):
        self.model = NearestNeighbors(n_neighbors=n_neighbors, metric='euclidean')

    def prepare_data(self, profiles):
        """
        Convert the user profiles into a numerical format for the algorithm.
        """
        data = []
        for profile in profiles:
            user_data = []
            # Lifestyle and Routine
            user_data.append(1 if profile.early_riser_night_owl == 'early_riser' else 0)
            user_data.append(1 if profile.work_location == 'home' else 0)
            
            # Cleanliness and Tidiness
            user_data.append(int(profile.importance_of_tidiness))
            user_data.append(1 if profile.cleaning_schedule_preference == 'yes' else 0)
            
            # Social Habits
            user_data.append(1 if profile.guest_frequency == 'often' else 0)
            user_data.append(1 if profile.preference_for_guests == 'comfortable' else 0)
            
            # Noise and Personal Space
            user_data.append(1 if profile.noise_tolerance == 'quiet' else 0)
            
            # Financial Responsibility
            user_data.append(1 if profile.rent_utilities_affordability == 'yes' else 0)
            
            # Pets
            user_data.append(1 if profile.has_pets == 'yes' else 0)
            user_data.append(1 if profile.pet_tolerance == 'okay' else 0)
            
            # Smoking/Drinking
            user_data.append(1 if profile.smoking_habits == 'smoker' else 0)
            
            # Shared Interests and Hobbies
            user_data.append(1 if profile.friendship_preference == 'friend' else 0)
            
            data.append(user_data)
            print (data)
        return np.array(data)

    def fit(self, profiles):
        """
        Fit the model with user profiles.
        """
        data = self.prepare_data(profiles)
        self.model.fit(data)

    def find_matches(self, profile, profiles):
        """
        Find the top matching users for a given user profile and return their match scores.
        """
        
        
        data = self.prepare_data([profile])
        print(data)
        distances, indices = self.model.kneighbors(data)
        matched_profiles = [(profiles[int(i)], distances[0][idx]) for idx, i in enumerate(indices[0])]
        return matched_profiles
