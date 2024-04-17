#!/usr/bin/env python3

# from config import db
from app import app
from models import db, Organizer, Attendee, Event, Review

with app.app_context():

    print("Deleting all records...")
    Organizer.query.delete()
    Attendee.query.delete()
    Review.query.delete()
    Event.query.delete()

    def seed():
        organizer1 = Organizer(
            full_name='Jane Wangari',
            affiliation='Wangari Foundation',
            location='Nairobi',
            contact='0722775059',
            username='Wangari_jane',
            image_url='image1.jpg',
            bio='Founder and CEO of Wangari Foundation',
            user_role='organizer'
        )
        organizer1.password_hash = 'lightbringer'

        organizer2 = Organizer(
            full_name='Mathia Mathew',
            affiliation='Baby Corp',
            location='Greece',
            contact='011251264',
            username='Mmathew',
            image_url='image2.jpg',
            bio='Lover of Life',
            user_role='organizer'
        )
        organizer2.password_hash = 'babiesforlife'

        organizer3 = Organizer(
            full_name='Arnold Swazzniger',
            affiliation='Swazz and Co',
            location='Kitale',
            contact='0722902963',
            username='Swazz',
            image_url='image3.jpg',
            bio='Social Activist',
            user_role='organizer'
        )
        organizer3.password_hash = 'rizzmaster'


        # Create instances of attendees
        attendee1 = Attendee(
            full_name='Alex Wafulla',
            affiliation='Tech bros',
            location='Nairobi',
            contact='0712345678',
            username='wafulla the goat',
            image_url='image1.jpg',
            bio='Aspiring data analyst',
            user_role='attendee',
            invitation_code=1234
        )
        attendee1.password_hash = 'thegoat'

        attendee2 = Attendee(
            full_name='Jaime Nia',
            affiliation='Karmasky Air',
            location='Nairobi',
            contact='0781289792',
            username='Nia',
            image_url='image2.jpg',
            bio='Social media manager for Karmasky Air.',
            user_role='attendee',
            invitation_code=4567
        )
        attendee2.password_hash = 'sneakers'

        # Create instances of events
        event1 = Event(
            title='Step Into The Tech World',
            logo='logo1.jpg',
            name='Tech Summit',
            location='Mombasa',
            period='Period ',
            event_description='Come lets learn more about technology together.',
            organizer=organizer2,
            attendee = attendee1
        )

        event2 = Event(
            title='Cancer Summit',
            logo='logo2.jpg',
            name='Spreading Lung Cancer Awareness',
            location='KICC',
            period='Period ',
            event_description='Together lets fight Cancer',
            organizer=organizer1,
            attendee = attendee2
        )

        # Create instances of reviews
        review1 = Review(
            score=8,
            comment='Great event!',
            event=event1,
            attendee=attendee1
        )

        review2 = Review(
            score=10,
            comment='Absolutely insightful',
            event=event2,
            attendee=attendee2
        )

        # Add instances to the session
        db.session.add_all([organizer1, organizer2, organizer3, attendee1, attendee2, event1, event2, review1, review2])

        # Commit the changes
        db.session.commit()

    seed()