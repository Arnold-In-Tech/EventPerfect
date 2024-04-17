import React, { useState, useEffect } from "react";

const Reviews = () => {
  const [reviews, setReviews] = useState([]);

  useEffect(() => {
    const fetchData = () => {
      fetch("/reviews")
        .then((response) => response.json())
        .then((data) => {
          setReviews(data);
        })
        .catch((error) => {
          console.error("Error fetching data:", error);
        });
    };

    fetchData();
  }, []);

  return (
    <div>
      <h2 className="text-2xl font-bold mb-4">Reviews</h2>
      <div className="grid grid-cols-3 gap-4">
        {reviews.map((review) => (
          <div key={review.id} className="bg-white rounded-md shadow-md p-4">
            <h3 className="text-lg font-semibold">{review.title}</h3>
            <p className="text-gray-600">{review.description}</p>
            <p className="text-gray-500 mt-2">Rating: {review.rating}</p>
            <p className="text-gray-500">Posted by: {review.user}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Reviews;
