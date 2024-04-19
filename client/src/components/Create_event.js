import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from "react-router-dom";

function CreateEvent() {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    title: '',
    logo: '',
    name: '',
    location: '',
    period: '',
    event_description: '',
    organizer_id: '',
    attendee_id: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  // Handle post request
  const handleSubmit = (e) => {
  e.preventDefault();
  fetch("/createEvents", {
      method: 'POST',
      body: JSON.stringify({
        title: formData.title,
        logo: formData.logo,
        name: formData.name,
        location: formData.location,
        period: formData.period,
        event_description: formData.event_description,
        organizer_id: formData.organizer_id,
        attendee_id: formData.attendee_id,
      }),
      headers: {
        'Content-type': 'application/json; charset=UTF-8',
      },
  })
      .then((res) => {
        return [res.json(), res.status]})
      .then((post) => {
        if (post[1] === 201) {
          alert(formData.title + " event successfully created.")
          setFormData({
            title: '',
            logo: '',
            name: '',
            location: '',
            period: '',
            event_description: '',
            organizer_id: '',
            attendee_id: '',
          });
        }else{
          alert("Error 401: " + formData.title + " event creation Unsuccessfull\n Please Login or Sign Up")
          navigate("/login")
        }
      })
      .catch((err) => {
        console.log(err.message);
      });
  }


  return (
    <div className="max-w-2xl ml-8">
      <h2 className="text-2xl font-bold mb-4">Create Event</h2>
      <form onSubmit={handleSubmit} className="space-y-4 w-2/3">
        <input type="text" name="title" value={formData.title} onChange={handleChange} placeholder="Title" className="w-full border rounded-md p-2" />
        <input type="text" name="logo" value={formData.logo} onChange={handleChange} placeholder="Logo URL" className="w-full border rounded-md p-2" />
        <input type="text" name="name" value={formData.name} onChange={handleChange} placeholder="Event Name" className="w-full border rounded-md p-2" />
        <input type="text" name="location" value={formData.location} onChange={handleChange} placeholder="Location" className="w-full border rounded-md p-2" />
        <input type="text" name="period" value={formData.period} onChange={handleChange} placeholder="Period" className="w-full border rounded-md p-2" />
        <textarea name="event_description" value={formData.event_description} onChange={handleChange} placeholder="Event Description" rows="4" className="w-full border rounded-md p-2"></textarea>
        <input type="text" name="organizer_id" value={formData.organizer_id} onChange={handleChange} placeholder="Organizer ID" className="w-full border rounded-md p-2" />
        <input type="text" name="attendee_id" value={formData.attendee_id} onChange={handleChange} placeholder="Attendee ID" className="w-full border rounded-md p-2" />
        <button type="submit" className="bg-black text-white font-bold py-2 px-4 rounded">Create Event</button>
      </form>
    </div>
  );
}

export default CreateEvent;
