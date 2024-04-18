// My_events.js
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { FaCalendar } from "react-icons/fa";
import { FaLocationDot } from "react-icons/fa6";
// import { MdEvent } from "react-icons/md";
import { FaNoteSticky } from "react-icons/fa6";

function MyEvents() {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    const fetchEvents = async () => {
      try {
        const response = await axios.get('/events');
        setEvents(response.data);
      } catch (error) {
        console.error('Error fetching events:', error);
      }
    };
    fetchEvents();
  }, []);

  return (
    <div className=" ml-8">
      <h2 className="text-2xl font-bold mb-4 ml-4"><FaNoteSticky className='inline mr-4'/>My Events</h2>
      <ul className="grid grid-cols-2 gap-x-8  gap-y-4 p-4">
        {events.map((event) => (
          <li key={event.id} className="border p-4 flex flex-col">
            <h3 className="text-lg font-semibold">{event.title}</h3>
            <div className="text-black">
              <p><FaLocationDot  className="inline mr-2"/>{event.location}</p>
              <p><FaCalendar className="inline mr-2" />{event.period}</p>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
}  

export default MyEvents;
