import React, { useState, useEffect } from "react";
import { FaStar, FaStarHalfAlt } from 'react-icons/fa';
import { MdReviews } from "react-icons/md";
import { IoMdContact } from "react-icons/io";

const Reviews = () => {
  const [reviews, setReviews] = useState([]);
  const [newReview, setNewReview] = useState({ score: 0, comment: "", attendee: { full_name: "" }, event: { name: "" } });

  useEffect(() => {
    fetch("/reviews") 
      .then((response) => {
        if (!response.ok) {
          throw new Error("Failed to fetch reviews");
        }
        return response.json();
      })
      .then((data) => {
        setReviews(data);
      })
      .catch((error) => {
        console.error("Error fetching reviews:", error);
      });
  }, []);

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setNewReview({ ...newReview, [name]: value });
  };

  const handleStarClick = (value) => {
    setNewReview({ ...newReview, score: value });
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    fetch("/reviews", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(newReview),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Network response was not ok");
        }
        return response.json();
      })
      .then((data) => {
        setReviews([...reviews, data]);
        setNewReview({ score: 0, comment: "", attendee: { full_name: "" }, event: { name: "" } });
      })
      .catch((error) => {
        console.error("Error posting review:", error);
      });
  };

  return (
    <div className="mt-8">
      <h2 className="text-2xl font-bold mb-1 ml-4 text-fourth"><MdReviews className="inline mr-4"/>Reviews</h2>
      <div className="grid grid-cols-2 p-12 gap-4 space-y-6">
        {reviews.map((review) => (
          <div key={review.id} className="bg-white rounded-md shadow-md p-4">
            <p className="text-fourth ">
              <IoMdContact className="inline mr-4 text-4xl"/>{review.attendee ? review.attendee.full_name : 'Jane Wanjiru'}
            </p>
            <p className="text-fourth text-md font-bold mt-2">
              {review.event ? review.event.name : 'AI Bootcamp'}
            </p>
            <p className="text-fourth italic text-sm mt-2 mb-2">"{review.comment}"</p>
            <div className="flex items-center">
              {[...Array(5)].map((_, index) => {
                const starValue = index + 1;
                if (review.score >= starValue) {
                  return <FaStar key={index} className="text-fourth" />;
                } else if (review.score + 0.5 === starValue) {
                  return <FaStarHalfAlt key={index} className="text-yellow-400" />;
                } else {
                  return <FaStar key={index} className="text-gray-300" onClick={() => handleStarClick(starValue)} />;
                }
              })}
              <span className="text-sm text-fourth font-medium ml-1">
                ({review.score}/5)
              </span>
            </div>
          </div>
        ))}
      </div>
      <form onSubmit={handleSubmit} className="bg-white rounded-md shadow-md p-12 w-1/2" ml-24>
        <h3 className="text-lg font-bold mb-2">Review an event</h3>
        <input type="text" name="attendee" value={newReview.attendee.full_name} onChange={handleInputChange} placeholder="Enter your full name" className="border rounded-md p-2 mb-2 block w-full" />
        <input type="text" name="event" value={newReview.event.name} onChange={handleInputChange} placeholder="Enter the name of the event your want to review" className="border rounded-md p-2 mb-2 block w-full" />
        <textarea name="comment" value={newReview.comment} onChange={handleInputChange} placeholder="Please give us your review" rows="4" className="border rounded-md p-2 mb-2 block w-full"></textarea>
        <div className="flex items-center mb-2">
          {[...Array(5)].map((_, index) => {
            const starValue = index + 1;
            return <FaStar key={index} className="text-gray-300" onClick={() => handleStarClick(starValue)} />;
          })}
          <span className="text-sm text-fourth font-medium ml-1">
            ({newReview.score}/5)
          </span>
        </div>
        <button type="submit" className="bg-black text-white font-bold py-2 px-4 rounded">Submit</button>
      </form>
    </div>
  );
}

export default Reviews;
