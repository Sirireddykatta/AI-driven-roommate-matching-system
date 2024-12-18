from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.core.exceptions import ValidationError
import PIL
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """Create and return a regular user with an email and password."""
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and return a superuser."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)
# Custom validator to check if the uploaded file is an image
def validate_image(file):
    try:
        img = PIL.Image.open(file)
        img.verify()  # Verify that this is indeed an image
    except (IOError, SyntaxError):
        raise ValidationError("The uploaded file is not a valid image.")
    
class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=255,null=False,blank=False)
    last_name = models.CharField(max_length=255,null=False,blank=False)
    username = models.CharField(max_length=255,unique=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', validators=[validate_image], blank=True, null=True)
   
    location = models.CharField(max_length=100)
    
    # 1. Lifestyle and Routine
    
    daily_schedule = models.CharField( max_length=255,verbose_name="What is your daily schedule like?")
    early_riser_night_owl = models.CharField(
        max_length=50, 
        choices=[('early_riser', 'Early Riser'), ('night_owl', 'Night Owl')], 
        verbose_name="Are you an early riser or a night owl?"
    )
    work_location = models.CharField(
        max_length=50, 
        choices=[('home', 'Work from Home'), ('out_of_house', 'Out of the House')],
        verbose_name="Do you work from home, or will you be out of the house most of the time?"
    )
    weekend_activities = models.CharField(max_length=255,verbose_name="How do you spend your weekends?")
    
    # 2. Cleanliness and Tidiness
    
    cleaning_schedule_preference = models.CharField(
        max_length=50, 
        choices=[('yes', 'Yes'), ('no', 'No')], 
        verbose_name="Do you prefer a cleaning schedule?"
    )
    importance_of_tidiness = models.IntegerField(
        choices=[(i, str(i)) for i in range(1, 6)], 
        verbose_name="How important is keeping common areas tidy to you? (1-5)",default=1
    )
    clean_up_frequency = models.CharField(
        max_length=50, 
        choices=[('immediately', 'Immediately'), ('daily', 'Daily'), ('weekly', 'Weekly')],
        verbose_name="How often do you clean up after yourself, especially in shared spaces?"
    )
    
    # 3. Social Habits
    guest_frequency = models.CharField(
        max_length=50, 
        choices=[('often', 'Often'), ('sometimes', 'Sometimes'), ('rarely', 'Rarely')], 
        verbose_name="Do you plan to have friends or family over often?"
    )
    preference_for_guests = models.CharField(
        max_length=50, 
        choices=[('comfortable', 'Comfortable'), ('neutral', 'Neutral'), ('uncomfortable', 'Uncomfortable')], 
        verbose_name="How do you feel about guests?"
    )
    handling_conflict = models.TextField(verbose_name="How do you handle conflict or disagreements with roommates?")
    
    
# 4. Noise and Personal Space

    noise_tolerance = models.CharField(
        max_length=50, 
        choices=[('quiet', 'Quiet'), ('moderate', 'Moderate'), ('loud', 'Loud')], 
        verbose_name="How do you feel about noise levels, like music or TV in common areas?"
    )
    alone_vs_socializing_time = models.TextField(verbose_name="How much time do you like to spend alone versus socializing?")
    personal_space_expectations = models.TextField(verbose_name="What are your expectations around personal space and privacy?")



# 5. Financial Responsibility
    rent_utilities_affordability = models.CharField(
        max_length=50, 
        choices=[('yes', 'Yes'), ('no', 'No')], 
        verbose_name="Can you comfortably afford rent and utilities?"
    )
    proof_of_income_willingness = models.BooleanField(verbose_name="Are you willing to share proof of income if needed?",default=False)
    bill_splitting_preference = models.CharField(
        max_length=50, 
        choices=[('equal', 'Split Equally'), ('other', 'Other Arrangement')],
        verbose_name="Are you open to splitting bills equally?"
    )
    handling_unexpected_costs = models.TextField(verbose_name="How do you handle unexpected costs, like repairs or shared purchases?")

# 6. Pets
    has_pets = models.CharField(
        max_length=50, 
        choices=[('yes', 'Yes'), ('no', 'No')],
        verbose_name="Do you have any pets, or are you planning to get one?"
    )
    pet_tolerance = models.CharField(
        max_length=50, 
        choices=[('okay', 'Okay with pets'), ('not_okay', 'Not okay with pets')],
        verbose_name="Are you okay with living with someone who has pets?"
    )
    pet_allergies = models.CharField(
        max_length=50, 
        choices=[('yes', 'Yes'), ('no', 'No')],
        verbose_name="Do you have any allergies or concerns about pets in the apartment?"
    )

# 7. Smoking/Drinking Habits

    smoking_habits = models.CharField(
        max_length=50, 
        choices=[('smoker', 'Smoker'), ('non_smoker', 'Non-Smoker')],
        verbose_name="Do you smoke, or do you mind if others do?"
    )
    drinking_habits = models.TextField(verbose_name="How often do you drink, and do you prefer a party-friendly or low-key living environment?")

# 8. Shared Interests and Hobbies

    hobbies_interests = models.TextField(verbose_name="Do you have any hobbies or interests that might affect living together?")
    friendship_preference = models.CharField(
        max_length=50, 
        choices=[('friend', 'Looking for a Friend'), ('independent', 'Prefer Keeping to Myself')],
        verbose_name="Are you looking for a roommate who is more of a friend or someone who keeps to themselves?"
    )

# 9. Expectations and House Rules

    house_rules = models.TextField(verbose_name="Do you have any specific house rules or boundaries you'd like to establish?")
    grocery_shopping_preference = models.CharField(
        max_length=50, 
        choices=[('separately', 'Separately'), ('together', 'Together')],
        verbose_name="How do you handle grocery shopping?"
    )
    shared_space_decoration = models.TextField(verbose_name="How do you feel about decorating or arranging shared spaces?")


# 10 Personal Details
    gender = models.CharField(
        max_length=100,
        choices=(
            ('male','Male'),('female','Female')
        ),
        verbose_name="What is your gender?"
    )
    age = models.PositiveIntegerField(verbose_name="What is your Age?",default=0)


    # Set the manager for the custom user model
    objects = CustomUserManager()

    USERNAME_FIELD = 'username'  # Use email to log in
    REQUIRED_FIELDS = []  # Email and password are required by default

    def __str__(self):
        return self.username
    
     # Optionally, you can resize the image after upload
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.profile_picture:
            img = PIL.Image.open(self.profile_picture.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.profile_picture.path)
