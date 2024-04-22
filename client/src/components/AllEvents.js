import React, { useState, useEffect } from "react";
import { FaCalendar } from "react-icons/fa";
import { FaLocationDot } from "react-icons/fa6";
import { MdEvent } from "react-icons/md";


const AllEvents = () => {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    fetch("/events") // Assuming your backend serves events data at '/events' endpoint
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to fetch events");
        }
        return response.json();
      })
      .then((data) => {
        setEvents(data);
      })
      .catch((error) => {
        console.error("Error fetching events:", error);
      });
  }, []);

  return (
    <div className="bg-white rounded-lg shadow-lg p-6">
      <h2 className="text-2xl font-bold mb-4 text-fourth"><MdEvent className="inline mr-4"/>All Events</h2>
      <ul className="grid grid-cols-2 gap-4">
        {events.map((event) => (
          <li key={event.id} className="mb-4">
            <div className="border border-gray-300 pb-4 p-4">
              <h3 className="text-lg text-fourth font-semibold">{event.title}</h3>
              <p className="text-sm text-fourth italic	 ">
                "{event.name}"
              </p>
              <p className="text-sm text-fourth ">
                <FaLocationDot  className="inline mr-2"/>{event.location}
              </p>
              <p className="text-sm text-fourth ">
                <FaCalendar className="inline mr-2" /> {event.period}
              </p>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default AllEvents;
