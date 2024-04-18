import React from 'react';
import { Link } from 'react-router-dom';
import { FaFacebook } from "react-icons/fa6";
import { FaInstagram } from "react-icons/fa";
import { FaXTwitter } from "react-icons/fa6";
import { FaLinkedin } from "react-icons/fa";

const Footer = () => {
  return (
    <footer className="flex flex-wrap bg-primary p-4 mt-4 md:items-top justify-center">
      <div className="w-full md:w-1/4 mb-10 mt-10">
        <h4 className="relative mb-8 font-bold text-lg text-fourth">evento</h4>
        <ul className="list-none font-light">
          <li><a href="#" className="block text-sm  text-fourth no-underline transition duration-400">About us</a></li>
          <li><a href="#" className="block text-sm  text-fourth no-underline transition duration-400">Contact us</a></li>
          <li><a href="#" className="block text-sm  text-fourth no-underline transition duration-400">Support</a></li>
          <li><a href="#" className="block text-sm  text-fourth no-underline transition duration-400">Careers</a></li>
        </ul>
      </div>
      <div className="w-full md:w-1/4 mb-10 mt-10">
        <h4 className="relative mb-8 font-bold text-md  text-fourth">Quick Links</h4>
        <ul className="list-none font-light">
          <li><a href="#" className="block text-sm  text-fourth no-underline transition duration-400"> Vendor Management</a></li>
          <li><a href="#" className="block text-sm  text-fourth no-underline transition duration-400">Event Timeline</a></li>
          <li><a href="#" className="block text-sm  text-fourth no-underline transition duration-400">Venue Selection</a></li>
          <li><a href="#" className="block text-sm  text-fourth no-underline transition duration-400">Event Decor</a></li>
          <li><a href="#" className="block text-sm  text-fourth no-underline transition duration-400">FAQs</a></li>
          <li><a href="#" className="block text-sm  text-fourth no-underline transition duration-400">Help?</a></li>
        </ul>
      </div>
      <div className="w-full md:w-1/4 mb-10 mt-10">
        <h4 className="relative mb-8 font-bold text-md   text-fourth">Legal terms</h4>
        <ul className="list-none font-light">
          <li><a href="#" className="block text-sm  text-fourth no-underline transition duration-400">Terms and Conditions</a></li>
          <li><a href="#" className="block text-sm  text-fourth no-underline transition duration-400">Privacy Policy</a></li>
          <li><a href="#" className="block text-sm  text-fourth no-underline transition duration-400">Intellectual Property (IP)</a></li>
          <li><a href="#" className="block text-sm  text-fourth no-underline transition duration-400">End User License Agreement (EULA)</a></li>
          <li><a href="#" className="block text-sm  text-fourth no-underline transition duration-400">Terms of Service</a></li>
        </ul>
      </div>
      <div className="w-full md:w-1/4 mb-10 mt-10">
        <h4 className="relative mb-8 font-bold text-md   text-fourth">Follow us</h4>
        <div className="links flex space-x-3 text-fourth font-light">
            <a href="#" className='text-xl'> <FaFacebook /> </a>
            <a href="#" className='text-xl'> <FaInstagram /> </a>
            <a href="#" className='text-xl'> <FaXTwitter /> </a>
            <a href="#" className='text-xl'> <FaLinkedin /> </a>
        </div>
      </div>
      <div className="w-full mt-4 mb-8 text-center items-center text-fourth font-light">
        <p>&copy; 2024 <span className="text-secondary text-xl space-x-2 font-black">evento</span> All rights reserved.</p>
      </div>
    </footer>
  );
};

export default Footer;

