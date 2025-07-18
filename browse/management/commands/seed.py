# scripts/management/commands/seed.py
from django.core.management.base import BaseCommand
from faker.providers import DynamicProvider
import random
from faker import Faker
from user_authentication.models import UserProfile
from reviewsapp.models import Review
from contactapp.models import ContactMessage
from skills.models import AddSkills, RequestSkills
from django.contrib.auth import get_user_model

User = get_user_model()

TC_provider = DynamicProvider(
     provider_name="TC",
     elements=["Python", "Physics", "Math", "Electrical Engineering", "Computer Science", "C programming", "AGI"],
)
CR_provider = DynamicProvider(
     provider_name="CR",
     elements=["Sewing", "Sculpting", "Painting", "Origami", "Set Design", "Woodcarving", "Knitting"],
)

LN_provider = DynamicProvider(
    provider_name ="LN",
    elements=["English", "Swedish", "Spanish", "Chinese", "Hindi", "Urdu", "French"],
)

OT_provider = DynamicProvider(
    provider_name ="OT",
    elements=["Violin", "Weight Lifting", "Job Search", "Communication", "Leadership", "Habits", "Meditation"],
)

category_provider = DynamicProvider(
    provider_name="category",
    elements=["TC", "CR", "LN", "OT"],
)

fake = Faker()

# then add new provider to faker instance
fake.add_provider(TC_provider)
fake.add_provider(CR_provider)
fake.add_provider(LN_provider)
fake.add_provider(OT_provider)
fake.add_provider(category_provider)

NUM_USERS = 200
NUM_SKILLS = 250
NUM_CONTACTS = 50
NUM_REVIEWS = 600

class Command(BaseCommand):
    help = "Populate the DB with demo data (users, exchanges, contact messages)"


    def handle(self, *args, **options):
        users = []
        profiles = []
        for _ in range(NUM_USERS):
            user = User.objects.create_user(
                username=fake.unique.user_name(),
                email=fake.unique.email(),
                password=fake.password(length=12),
            )
            profile = UserProfile.objects.create(
                user=user,
                portfolio=fake.url(),
                profile_pic='media/profile_pics/default.jpg',
            )
            users.append(user)
            profiles.append(profile)
        
        skills_objs = []
        for _ in range(NUM_SKILLS):
            owner = random.choice(users)
            cat = fake.category()
            title = getattr(fake, cat)()

            
            skill =AddSkills.objects.create(
                user=owner,
                created=fake.date(),
                category=cat,
                title=title,
                availability=fake.boolean(),
                location=fake.country(),
                description=fake.sentence(),
            )
            skills_objs.append(skill)

        contacts_objs = []
        for _ in range(NUM_CONTACTS):
            sender_profile = random.choice(users)
            
            contact = ContactMessage.objects.create(
                sender=sender_profile,
                recipient=random.choice(users),
                skill=random.choice(skills_objs),
                email=sender_profile.email,
                submitted_at=fake.date(),
            )
            contacts_objs.append(contact)

        reviews_objs = []
        for _ in range(NUM_REVIEWS):
            skill = random.choice(skills_objs)
            
            review = Review.objects.create(
                skill=skill,
                reviewer = random.choice(users),
                reviewee = skill.user,
                rating = random.randrange(1,6),
                comment = fake.sentence(),
                created_at = fake.date_time_this_year(),
            )
            reviews_objs.append(review)
        
        self.stdout.write(self.style.SUCCESS(f"Created {NUM_USERS} user profiles with {NUM_SKILLS} skills, written {NUM_REVIEWS} reviews and {NUM_CONTACTS} of contacts was made between users."))
