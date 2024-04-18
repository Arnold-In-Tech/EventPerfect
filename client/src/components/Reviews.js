import React, { useState, useEffect } from "react";
import { FaStar, FaStarHalfAlt } from 'react-icons/fa';
import { MdReviews } from "react-icons/md";

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
      <h2 className="text-2xl font-bold mb-4 ml-4 text-fourth"><MdReviews className="inline mr-4"/>Reviews</h2>
      <div className="grid grid-cols-3 gap-4">
        {reviews.map((review) => (
          <div key={review.id} className="bg-white rounded-md shadow-md p-4">
            <p className="text-fourth text-md font-bold mt-2">
              {review.event.name}
            </p>
            <p className="text-fourth font-style: italic">"{review.comment}"</p>
            <p className="text-fourth ml-32">
              ~ {review.attendee.full_name}
            </p>
            <div className="flex items-center">
              {[...Array(5)].map((_, index) => {
                const starValue = index + 1;
                if (review.score >= starValue) {
                  return <FaStar key={index} className="text-fourth" />;
                } else if (review.score + 0.5 === starValue) {
                  return <FaStarHalfAlt key={index} className="text-yellow-400" />;
                } else {
                  return <FaStar key={index} className="text-gray-300" />;
                }
              })}
              <span className="text-sm text-fourth font-medium ml-1">
                ({review.score}/5)
              </span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
export default Reviews;
