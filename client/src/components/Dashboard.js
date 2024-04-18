import React, { useState, useEffect } from "react";
import { FaCalendar } from "react-icons/fa";
import { FaLocationDot } from "react-icons/fa6";
import { GiHamburgerMenu } from "react-icons/gi";
import Carousel from "./Carousel";
import LandingPage from "./Landing_page";
import Gallery from "./Gallery";
import AllEvents from "./AllEvents";
import MyEvents from "./My_events";
import Reviews from "./Reviews";

const Dashboard = () => {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    const fetchData = () => {
      fetch("/events")
        .then((response) => response.json())
        .then((data) => {
          setEvents(data);
        })
        .catch((error) => {
          console.error("Error fetching data:", error);
        });
    };

    fetchData();
  }, []);

  return (
    <div className="mt-8">
      {/* <Carousel /> */}
      <LandingPage />
      <Gallery />
      <h2 className="text-4xl font-bold mb-4 mt-8 text-center ml-4 text-fourth">Upcoming Events</h2>
      <div className="grid grid-cols-2 gap-4 p-8">
        {events.map((event) => (
          <div key={event.id} className="bg-white rounded-md shadow-md p-4">
            <h3 className="text-lg text-fourth font-semibold">{event.title}</h3>
            <p className="text-fourth text-sm italic">"{event.event_description}"</p>
            <p className="text-fourth text-sm font-medium "><FaLocationDot  className="inline mr-2"/> {event.location}</p>
            <p className="text-fourth mt-2 text-sm font-medium"><FaCalendar className="inline mr-2" /> {event.period}</p>
          </div>
        ))}
      </div>
      <AllEvents />
      <MyEvents />
      <Reviews />
    </div>
  );
};

export default Dashboard;
