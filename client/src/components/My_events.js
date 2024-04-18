import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { FaCalendar } from "react-icons/fa";
import { FaLocationDot } from "react-icons/fa6";
import { FaNoteSticky, FaHeart, FaCheck } from "react-icons/fa6";

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

  const handleLike = (eventId) => {
    // Logic to toggle the like status for the event with eventId
    setEvents(events.map(event => {
      if (event.id === eventId) {
        return { ...event, liked: !event.liked };
      }
      return event;
    }));
  };

  const handleDone = (eventId) => {
    // Logic to mark the event as done
    setEvents(events.map(event => {
      if (event.id === eventId) {
        return { ...event, done: !event.done };
      }
      return event;
    }));
  };

  return (
    <div className="ml-8 mt-8">
      <h2 className="text-2xl font-bold mb-4 ml-4"><FaNoteSticky className='inline mr-4'/>My Events</h2>
      <ul className="grid grid-cols-2 gap-x-8 gap-y-4 p-4">
        {events.map((event) => (
          <li key={event.id} className="border p-4 flex flex-col relative">
            <div className="flex justify-between items-center mb-2">
                <h3 className={`text-lg font-semibold ${event.done ? 'line-through' : ''}`}>{event.title}</h3>
                <div className="flex">
                <FaHeart
                    className={`cursor-pointer ${event.liked ? 'text-black' : 'text-gray-500'} text-2xl mr-2`}
                    onClick={() => handleLike(event.id)}
                />
                <FaCheck
                    className={`cursor-pointer ${event.done ? 'text-black' : 'text-gray-500'} text-2xl`}
                    onClick={() => handleDone(event.id)}
                />
                </div>
            </div>
            <div className={`text-black ${event.done ? 'line-through' : ''}`}>
                <p><FaLocationDot className="inline mr-2" />{event.location}</p>
                <p><FaCalendar className="inline mr-2" />{event.period}</p>
            </div>
        </li>
        ))}
      </ul>
    </div>
  );
}

export default MyEvents;
