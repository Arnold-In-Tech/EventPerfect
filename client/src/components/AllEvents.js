import React, { useState, useEffect } from "react";

const AllEvents = () => {
  const [events, setEvents] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

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
          // setIsLoading(false);
          console.log(data);
        })
        .catch((error) => {
          console.error("Error fetching data:", error);
          setError(error);
          setIsLoading(false);
        });
    };

    fetchData();
  }, []);

  if (isLoading) {
    return <div>Loading...</div>;
  }

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  return (
    <div>
      <h2 className="text-2xl font-bold mb-4">All Events</h2>
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

export default AllEvents;
