#!/usr/bin/env python3

from flask import request, session, make_response
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError
from flask import jsonify

from config import app, db, api
from models import Organizer, Attendee, Event, Review

@app.before_request				
def check_if_logged_in():		
    open_access_list = [
        'signup',
        'check_session',
        'login',
        'logout',
        'home',
        'events',
        'attendees',    # comment this out after creating front-end login
        'organizers',   # comment this out after creating front-end login
        'reviews',       # comment this out after creating front-end login
        'eventbyids',   # same
        'organizer_attendees_by_ids', # same 
        'event_attendees_by_ids'    # same
    ]				
    if (request.endpoint) not in open_access_list and (not session.get('user_id')):
        return {'error': '401 Unauthorized'}, 401


class Signup(Resource):
    def post(self):
        json = request.get_json()

        full_name = json.get('full_name')
        affiliation = json.get('affiliation')
        location  = json.get('location')
        contact = json.get('contact')
        username = json.get('username')
        password = json.get('password')
        image_url = json.get('image_url')
        bio = json.get('bio')

        if json.get('user_role').lower() == "organizer":
            new_user = Organizer(
                full_name = full_name,
                affiliation = affiliation,
                location = location,
                contact = contact,
                username = username,
                image_url = image_url,
                bio = bio
            )  
            new_user.password_hash = password  
            try:
                db.session.add(new_user)
                db.session.commit()
                session['organizer_id'] = new_user.id
                return new_user.to_dict(), 201
            except IntegrityError:
                return {'error': '422 Unprocessable Entity'}, 422
        elif json.get('user_role').lower() == "attendee":
            new_user = Attendee(
                full_name = full_name,
                affiliation = affiliation,
                location = location,
                contact = contact,
                username = username,
                image_url = image_url,
                bio = bio
            )  
            new_user.password_hash = password  
            try:
                db.session.add(new_user)
                db.session.commit()
                session['attendee_id'] = new_user.id
                return new_user.to_dict(), 201
            except IntegrityError:
                return {'error': '422 Unprocessable Entity'}, 422


class CheckSession(Resource):
   def get(self):
        if session.get('organizer_id'):            
            organizer = Organizer.query.filter(Organizer.id == session['organizer_id']).first()
            return organizer.to_dict(), 200
        elif session.get('attendee_id'): 
            attendee = Attendee.query.filter(Attendee.id == session['attendee_id']).first()
            return attendee.to_dict(), 200
        else:
            return {'error': 'Unauthorized'}, 401

class Login(Resource):
    def post(self):

        username = request.get_json()['username']
        password = request.get_json()['password']
        user_role = request.get_json()['user_role']     # The fronted login should ask to select user_role

        if user_role.lower() == 'organizer':
            organizer = Organizer.query.filter(Organizer.username == username).first()
            if organizer:
                if organizer.authenticate(password):	
                    session['organizer_id'] = organizer.id			
                    return organizer.to_dict(), 200
            else:
                return {'error': 'Unauthorized: invalid username or password'}, 401
            
        elif user_role.lower() == 'attendee':
            attendee = Attendee.query.filter(Attendee.username == username).first()
            if attendee:
                if attendee.authenticate(password):	
                    session['attendee_id'] = attendee.id			
                    return attendee.to_dict(), 200
            else:
                return {'error': 'Unauthorized: invalid username or password'}, 401


class Logout(Resource):
    def delete(self):
        if session['attendee_id']:
            session['attendee_id'] = None
            return {}, 204
        elif session['organizer_id']:
            session['organizer_id'] = None
            return {}, 204

        return {'error': 'Unauthorized: user is not logged in'}, 401
            

class Home(Resource):
    def get(self):
        return '<h1>Code challenge</h1>'


### GET /organizers
class Organizers(Resource):
    def get(self):
        organizers = [organizer.to_dict() for organizer in Organizer.query.all()]

        response = make_response(
            [{'id': organizer['id'],'Fullname': organizer['full_name']} for organizer in organizers],
            200,
            {"Content-Type": "application/json"},
            )
        return response


### GET /attendees
class Attendees(Resource):
    def get(self):
        attendees = [attendee.to_dict() for attendee in Attendee.query.all()]

        response = make_response(
            [{'id': attendee['id'],'Fullname': attendee['full_name']} for attendee in attendees],
            200,
            {"Content-Type": "application/json"},
            )
        return response


# List of events
### GET /events
class Events(Resource):
    def get(self):
        events = [event.to_dict() for event in Event.query.all()]

        response = make_response(
            events,
            200,
            {"Content-Type": "application/json"},
            )
        return response


# List of reviews
### GET /reviews
class Reviews(Resource):
    def get(self):
        reviews = [review.to_dict() for review in Review.query.all()]

        # Return reviews as JSON using Flask's jsonify
        # return jsonify(reviews), 200
        response = make_response(
            jsonify(reviews),
            200,
            {"Content-Type": "application/json"},
        )
        return response
        



# Event by ID
### GET '/event/<int:id>'
class EventById(Resource):
    def get(self, id):
        event = Event.query.filter(Event.id==id).first()

        event_dict = event.to_dict()

        response = make_response(
            event_dict,
            200,
            {"Content-Type": "application/json"},
        )
        return response


# list of attendees for a specific organizer
### GET /organizer/attendees/<int:id>
class Organizer_attendees_by_id(Resource):
    def get(self, id):
        organizer = Organizer.query.filter(Organizer.id==id).first()

        # use association proxy to get attendees for an organiser through events
        attendees = [attendee.to_dict(rules=("-events",)) for attendee in organizer.attendees]

        response = make_response(
            attendees,
            200,
            {"Content-Type": "application/json"},
            )
        return response
    

# list of attendees for a specific event
### GET /event/attendees/<int:id>
class Event_attendees_by_id(Resource):
    def get(self, id):
        event = Event.query.filter(Event.id==id).first()

        # use association proxy to get attendees for an organiser through events
        attendees = [attendee.to_dict(rules=("-reviews",)) for attendee in event.attendees]

        response = make_response(
            attendees,
            200,
            {"Content-Type": "application/json"},
            )
        return response


# List of reviews for a specific event
### GET /event/reviews
class Event_attendees_by_id(Resource):
    def get(self, id):
        event = Event.query.filter(Event.id==id).first()

        # use association proxy to get attendees for an organiser through events
        attendees = [attendee.to_dict(rules=("-reviews",)) for attendee in event.attendees]

        response = make_response(
            attendees,
            200,
            {"Content-Type": "application/json"},
            )
        return response



api.add_resource(Home, '/', endpoint='home' )    
api.add_resource(Signup, '/signup', endpoint='signup')
api.add_resource(CheckSession, '/check_session', endpoint='check_session')
api.add_resource(Login, '/login', endpoint='login')
api.add_resource(Logout, '/logout', endpoint='logout')
api.add_resource(Organizers, '/organizers', endpoint='organizers')
api.add_resource(Attendees, '/attendees', endpoint = 'attendees')
api.add_resource(Events, '/events', endpoint = 'events')
api.add_resource(Reviews, '/reviews',  endpoint = 'reviews')
api.add_resource(EventById, '/event/<int:id>', endpoint='eventbyids')
api.add_resource(Organizer_attendees_by_id, '/organizer/attendees/<int:id>', endpoint='organizer_attendees_by_ids')
api.add_resource(Event_attendees_by_id, '/event/attendees/<int:id>', endpoint='event_attendees_by_ids')


if __name__ == '__main__':
    app.run(port=5555, debug=True)