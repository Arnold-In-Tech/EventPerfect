# Evento

# Description
evento is a platform that enables organizers to create, manage, and promote their events efficiently, while providing attendees with a user-friendly interface for discovering, registering, and engaging with events. 

# Technology stack
![Static Badge](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
![Static Badge](https://img.shields.io/badge/PostgreSQL-316192?style=for-the-badge&logo=postgresql&logoColor=white)
![Static Badge](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Static Badge](https://img.shields.io/badge/JS-JavaScript-yellow?style=for-the-badge&logo=javascript)
![Static Badge](https://img.shields.io/badge/HTML-HTML_5-red?style=for-the-badge&logo=html5)
![Static Badge](https://img.shields.io/badge/CSS-CSS_3-blue?style=for-the-badge&logo=css3)
![Static Badge](https://img.shields.io/badge/npm-CB3837?style=for-the-badge&logo=npm&logoColor=white)
[![Static Badge](https://img.shields.io/badge/Licence-MIT-maroon?style=for-the-badge)](./LICENSE)


# Features

- login /sign in features
- navbar
- upcoming events
- gallery section
- create events
- review section

# Installation

To install evento Project, follow these steps:

1. Clone the repository: `git clone https://github.com/Arnold-In-Tech/eventPerfect.git`
2. Navigate to the project directory: 
`cd ./eventperfect`

3. Install server side dependencies:
    `pipenv --python /usr/bin/python3.xx.x`
    `pipenv install`
    `pipenv shell`

4. Seed server side database:
    `python ./server/seed.py`

5. Change directory to server and start the server:
    `cd server`
    `python app.py`

5. On a new terminal, change into client directory, and install client side dependencies:
    `cd ./client`
    `npm install`

4. Start the application: 
    `npm start`


# Usage

Once installed, you can start using evento immediately. Here are some basic commands:

- `login` as either an organizer or atttendee to access the home page.
- `signup` for new users either as an organizer or attendee
- users can view all events, view upcoming events, view my events, create events, provide reviews for an event, Like an event, and cross an event to indicate that it has ended. 


# Contributing

We welcome contributions from the community. To contribute to evento, follow these steps:

1. Fork the repository
2. Create a new branch: `git checkout -b feature`
3. Make your changes and commit them: `git commit -am 'Add new feature'`
4. Push to the branch: `git push origin feature/new-feature`
5. Submit a pull request

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for more details on our code of conduct, and the process for submitting pull requests.

# Deployment

The application has been deployed to production using Render, and can accessed through the following link:
[ `To be provided` ]

# Future enhancements

- Incorporate global conferences to promote cross-cultural interactions.
- Add google map utility to conferences to improve findability of conference locations by attendees.
- Incorporate social network API’s like Zoom, Google Meet.
- Send personalized reminders to the attendees and organizers concerning the events .
- Provide a payment platform for event ticketing.

# Authors
This is a collaborative project with contributions from Samuel Wanyua @samwanyua, Naomi Mogi @Naomi391, Hillary Wangui
hillary-wangui, and Arnold Amusengeri @Arnold-In-Tech 

# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

