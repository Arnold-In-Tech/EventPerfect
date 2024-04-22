import React from 'react';
import { Link } from 'react-router-dom';

function LandingPage() {
    return (
      <div className="relative h-screen flex items-center justify-center" style={{ backgroundImage: 'url(https://images.unsplash.com/photo-1587825140708-dfaf72ae4b04?q=80&w=1470&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D)', opacity: 0.9 }}>
        <div className="bg-white rounded-md shadow-md p-8 max-w-lg" style={{ opacity: 0.9 }}>
          <h1 className="text-3xl font-bold mb-4">Welcome to your ultimate event experience. Discover, engage, and enjoy!</h1>
          <p className="text-black">Our platform empowers organizers and attendees alike, offering streamlined management and immersive experiences.</p>
          <Link to="/events">
            <button className="bg-black hover:bg-gray-500 text-white font-bold py-2 px-4 mt-4 rounded-md">Get Started</button>
          </Link>
        </div>
      </div>
    );
  }
  
  export default LandingPage;
