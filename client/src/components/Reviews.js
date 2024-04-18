import React, { useState, useEffect } from "react";

const Reviews = () => {
  const [reviews, setReviews] = useState([]);

  useEffect(() => {
    fetch("/reviews") // Assuming your backend serves review data at '/reviews' endpoint
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

  return (
    <div>
      <h2 className="text-2xl font-bold mb-4">Reviews</h2>
      <div className="grid grid-cols-3 gap-4">
        {reviews.map((review) => (
          <div key={review.id} className="bg-white rounded-md shadow-md p-4">
            <h3 className="text-lg font-semibold">Rating: {review.score}</h3>
            <p className="text-gray-600">{review.comment}</p>
            <p className="text-gray-500 mt-2">
              Event Name: {review.event["name"]}
            </p>
            <p className="text-gray-500">
              Attendee Name: {review.attendee["full_name"]}
            </p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Reviews;
