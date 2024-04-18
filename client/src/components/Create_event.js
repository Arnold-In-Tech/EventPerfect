import React, { useState } from 'react';
import axios from 'axios';

function CreateEvent() {
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

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('/events', formData);
      console.log(response.data); // Log the created event
      // Clear form fields after successful submission
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
    } catch (error) {
      console.error('Error creating event:', error);
    }
  };

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
