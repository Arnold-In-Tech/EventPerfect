import React, { useState, useEffect } from "react";

const Dashboard = () => {
  const [events, setEvents] = useState([]);

  useEffect(() => {
    const fetchData = () => {
      fetch("/events")
        .then((response) => {
          if (!response.ok) {
            throw new Error("Network response was not ok");
          }
          return response.json();
        })
        .then((data) => {
          // setEvents(data);
          console.log(data);
        })
        .catch((error) => {
          console.error("Error fetching data:", error);
        });
    };

    fetchData();
  }, []);

  return (
    <div>
      <h2 className="text-2xl font-bold mb-4">Dashboard</h2>
      <div className="grid grid-cols-3 gap-4">
        {events.map((event) => (
          <div key={event.id} className="bg-white rounded-md shadow-md p-4">
            <h3 className="text-lg font-semibold">{event.title}</h3>
            <p className="text-gray-600">{event.event_description}</p>
            <p className="text-gray-500 mt-2">Date: {event.period}</p>
            <p className="text-gray-500">Location: {event.location}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Dashboard;
