import React, { useState, useEffect } from "react";
import { FaCalendar } from "react-icons/fa";
import { FaLocationDot } from "react-icons/fa6";
import { GiHamburgerMenu } from "react-icons/gi";

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
    <div>
      <h2 className="text-2xl font-bold mb-4 ml-4 text-fourth"><GiHamburgerMenu className="inline mr-4"/>Dashboard</h2>
      <div className="grid grid-cols-3 gap-4">
        {events.map((event) => (
          <div key={event.id} className="bg-white rounded-md shadow-md p-4">
            <h3 className="text-lg text-fourth font-semibold">{event.title}</h3>
            <p className="text-fourth text-sm italic">"{event.event_description}"</p>
            <p className="text-fourth text-sm font-medium "><FaLocationDot  className="inline mr-2"/> {event.location}</p>
            <p className="text-fourth mt-2 text-sm font-medium"><FaCalendar className="inline mr-2" /> {event.period}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Dashboard;
