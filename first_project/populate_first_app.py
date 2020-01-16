import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')

import django
django.setup()

## Fake pop settings

import random
from first_app.models import AccessRecord, Topic, Webpage, Users
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def addTopic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()

    return t

def populate(N=5):
    for _ in range(N):

        # Get topic for entry
        top = addTopic()

        # Create Fake data for object
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        # Create New Webpage Entry
        webpg = Webpage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]

        # Create fake access record for the webpage
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

        # Get Name for entry
        fake_username = fakegen.name().split()
        fake_firstName = fake_username[0]
        fake_lastName = fake_username[1]

        fake_email = fakegen.email()

        user = Users.objects.get_or_create(firstName=fake_firstName, lastName=fake_lastName, email=fake_email)[0]

if __name__ == "__main__":
    print('populating script')
    populate(20)