from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy

from config import db, bcrypt

class Organizer(db.Model, SerializerMixin):
    __tablename__ = 'organizers'
    serialize_rules = ('-events.organizer',)

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String, unique=True, nullable=False)
    affiliation =  db.Column(db.String)
    location  = db.Column(db.String)
    contact = db.Column(db.String)
    username = db.Column(db.String, unique=True, nullable=False)
    _password_hash = db.Column(db.String)
    image_url = db.Column(db.String, nullable=False)
    bio = db.Column(db.String)
    user_role = db.Column(db.String)


    events = db.relationship('Event', back_populates="organizer")	
    
    # Association proxy to get attendees for this organizer through events
    attendees = association_proxy("events", "attendee",
                              creator=lambda user_obj: Event(user=user_obj))

    @hybrid_property
    def password_hash(self):
        raise AttributeError('Password hashes may not be viewed.')

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(
            password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(
            self._password_hash, password.encode('utf-8'))

    def __repr__(self):
        return f'Organizer {self.username}, Name {self.full_name}, ID: {self.id}'


class Attendee(db.Model, SerializerMixin):
    __tablename__ = 'attendees'
    serialize_rules = ('-events.attendee',)

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String, unique=True, nullable=False)
    affiliation =  db.Column(db.String)
    location  = db.Column(db.String)
    contact = db.Column(db.String)
    username = db.Column(db.String, unique=True, nullable=False)
    _password_hash = db.Column(db.String)
    image_url = db.Column(db.String, nullable=False)
    bio = db.Column(db.String)
    user_role = db.Column(db.String)
    invitation_code = db.Column(db.Integer, nullable=False)

    events = db.relationship('Event', back_populates="attendee")	
    reviews = db.relationship("Review", back_populates="attendee")

    @hybrid_property
    def password_hash(self):
        raise AttributeError('Password hashes may not be viewed.')

    @password_hash.setter
    def password_hash(self, password):
        password_hash = bcrypt.generate_password_hash(
            password.encode('utf-8'))
        self._password_hash = password_hash.decode('utf-8')

    def authenticate(self, password):
        return bcrypt.check_password_hash(
            self._password_hash, password.encode('utf-8'))

    def __repr__(self):
        return f'Attendee {self.username}, Name {self.full_name}, ID: {self.id}'


class Event(db.Model, SerializerMixin):
    __tablename__ = 'events'
    serialize_rules = ('-organizer.events', '-attendee.events',)

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    logo = db.Column(db.String, nullable=False)
    name = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    period =  db.Column(db.String, nullable=False)
    event_description =  db.Column(db.String, nullable=False)
    organizer_id = db.Column(db.Integer, db.ForeignKey('organizers.id'))  
    attendee_id = db.Column(db.Integer, db.ForeignKey('attendees.id'))  

    organizer = db.relationship('Organizer', back_populates="events")
    attendee = db.relationship('Attendee', back_populates="events")
    reviews = db.relationship("Review", back_populates="event")

    # Association proxy to get attendees for this event through reviews
    attendees = association_proxy("reviews", "attendee",
                              creator=lambda user_obj: Event(user=user_obj))


class Review(db.Model, SerializerMixin):
    __tablename__ = "reviews"

    # serialize_rules = ("-event.reviews", "-attendee.reviews",)
    serialize_only = ('id', 'score', 'comment', 'created_at', 'updated_at', 'event.name', 'attendee.full_name',)
    serialize_rules = ()

    id = db.Column(db.Integer, primary_key=True)
    score = db.Column(db.Integer)
    comment = db.Column(db.String)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    event_id = db.Column(db.Integer, db.ForeignKey("events.id"))
    attendee_id = db.Column(db.Integer, db.ForeignKey("attendees.id"))

    event = db.relationship("Event", back_populates="reviews")
    attendee = db.relationship("Attendee", back_populates="reviews")

    def __repr__(self):
        return f"<Review ({self.id}) of {self.event} by  {self.attendee}: {self.score}/10>"
