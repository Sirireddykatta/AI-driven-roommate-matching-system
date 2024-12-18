from django import forms
from users.models import User

class BootstrapFormMixin(forms.ModelForm):
    def add_bootstrap_classes(self):
        for name, field in self.fields.items():
            # Apply the 'form-control' class
            field.widget.attrs.update({'class': 'form-control'})
            
            # If there are errors for the field, add the 'is-invalid' class
            if self.errors.get(name):
                field.widget.attrs.update({'class': 'form-control is-invalid'})


class LifestyleRoutineForm(BootstrapFormMixin):
    class Meta:
        model = User
        fields = ['daily_schedule', 'early_riser_night_owl', 'work_location', 'weekend_activities']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_bootstrap_classes()


class CleanlinessTidinessForm(BootstrapFormMixin):
    class Meta:
        model = User
        fields = ['cleaning_schedule_preference', 'importance_of_tidiness', 'clean_up_frequency']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_bootstrap_classes()


class SocialHabitsForm(BootstrapFormMixin):
    class Meta:
        model = User
        fields = ['guest_frequency', 'preference_for_guests', 'handling_conflict']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_bootstrap_classes()


class NoisePersonalSpaceForm(BootstrapFormMixin):
    class Meta:
        model = User
        fields = ['noise_tolerance', 'alone_vs_socializing_time', 'personal_space_expectations']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_bootstrap_classes()


class FinancialResponsibilityForm(BootstrapFormMixin):
    class Meta:
        model = User
        fields = ['rent_utilities_affordability', 'proof_of_income_willingness', 'bill_splitting_preference', 'handling_unexpected_costs']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_bootstrap_classes()


class PetsForm(BootstrapFormMixin):
    class Meta:
        model = User
        fields = ['has_pets', 'pet_tolerance', 'pet_allergies']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_bootstrap_classes()


class SmokingDrinkingForm(BootstrapFormMixin):
    class Meta:
        model = User
        fields = ['smoking_habits', 'drinking_habits']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_bootstrap_classes()


class SharedInterestsHobbiesForm(BootstrapFormMixin):
    class Meta:
        model = User
        fields = ['hobbies_interests', 'friendship_preference']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_bootstrap_classes()


class ExpectationsHouseRulesForm(BootstrapFormMixin):
    class Meta:
        model = User
        fields = ['house_rules', 'grocery_shopping_preference', 'shared_space_decoration']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_bootstrap_classes()


class PersonalDetailsForm(BootstrapFormMixin):
    class Meta:
        model = User
        fields = ['gender', 'age']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.add_bootstrap_classes()
