# Evento

# Description
evento is a platform that enables organizers to create, manage, and promote their events efficiently, while providing attendees with a user-friendly interface for discovering, registering, and engaging with events. 

# Technology stack
![Static Badge](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Static Badge](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Static Badge](https://img.shields.io/badge/JavaScript-323330?style=for-the-badge&logo=javascript&logoColor=F7DF1E)
![Static Badge](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![Static Badge](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Static Badge](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white)
![Static Badge](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Static Badge](https://img.shields.io/badge/npm-CB3837?style=for-the-badge&logo=npm&logoColor=white)
![Static Badge](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
[![Static Badge](https://img.shields.io/badge/Licence-MIT-maroon?style=for-the-badge)](./LICENSE)


# Features

- Dashboard
- Login /sign up features
- Navigation bar
- Upcoming events
- Gallery section
- Create event
- Review event
- Like event
- Mark event as complete

# Installation

To install evento Project, follow these steps:

1. Clone the repository: 
```bash
git clone https://github.com/Arnold-In-Tech/eventPerfect.git
```
2. Navigate to the project directory: 
```bash
cd ./eventperfect
```

3. Install server side dependencies:
```bash
    pipenv --python /usr/bin/python3.xx.x
    pipenv install
    pipenv shell
```

4. Seed server side database:
```bash
python ./server/seed.py
```

5. Change directory to server and start the server:
```bash
    cd server
    python app.py
```

5. On a new terminal, change into client directory, and install client side dependencies:
```
    cd ./client
    npm install
```

4. Start the application: 
```bash
    npm start
```

# Usage

Once installed, you can start using evento immediately. Here are some basic commands:

- `login` as either an organizer or atttendee to access the home page.
- `signup` for new users either as an organizer or attendee
- users can view all events, view upcoming events, view my events, create events, provide reviews for an event, Like an event, and cross an event to indicate that it has ended. 


# Contributing

We welcome contributions from the community. To contribute to evento, follow these steps:

1. Fork the repository
2. Create a new branch: 
```bash
git checkout -b ft-newFeatureName
```
3. Make your changes and commit them: 
```bash
git commit -m "Add new information"
```
4. Push to the branch: 
```bash
git push origin ft-newFeatureName
```
5. Submit a pull request


# Deployment

The application has been deployed to production using Heroku, and can accessed through this link: 
[evento](https://infinite-sands-52806-2205d672ba83.herokuapp.com/)


# Future enhancements

- Provide a 'see more' utility for viewing details of an event: full description, associated attendees and reviews.
- Incorporate global conferences to promote cross-cultural interactions.
- Add google map utility to conferences to improve findability of conference locations by attendees.
- Incorporate social network API’s like Zoom, Google Meet.
- Send personalized reminders to the attendees and organizers concerning the events .
- Provide a payment platform for event ticketing.

# Authors
This is a collaborative project with contributions from Samuel Wanyua @samwanyua, Naomi Mogi @Naomi391, Hillary Wangui
@hillary-wangui, and Arnold Amusengeri @Arnold-In-Tech 

# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

