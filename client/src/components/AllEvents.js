import React, { useState, useEffect } from "react";

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
      <h2 className="text-2xl font-bold mb-4">All Events</h2>
      <ul className="grid grid-cols-2 gap-4">
        {events.map((event) => (
          <li key={event.id} className="mb-4">
            <div className="border border-gray-300 pb-4 p-4">
              <h3 className="text-xl font-semibold">{event.title}</h3>
              <p>
                <strong>Name:</strong> {event.name}
              </p>
              <p>
                <strong>Location:</strong> {event.location}
              </p>
              <p>
                <strong>Period:</strong> {event.period}
              </p>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default AllEvents;
