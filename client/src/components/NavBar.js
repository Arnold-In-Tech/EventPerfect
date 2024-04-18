import React from "react";
import { NavLink, Link } from "react-router-dom";

const NavBar = () => {
  return (
    <header className="min-w-[1000px]">
      <div className="flex bg-black text-primary h-[60px] mb-4">
        {/* Left */}
        <div className="flex items-center m-4 mr-[24]">
          <Link to={"/"}>
            <h2>
              <span className="text-secondary">
                <strong className="text-xl text-white">evento</strong>
              </span>
            </h2>
          </Link>
        </div>
        {/* Middle */}
        <div className="flex grow relative items-center space-x-12 ml-10 text-white">
          {/* Navigation links */}
          <NavLink to="/" activeClassName="text-amber-400">
            Dashboard
          </NavLink>
          <NavLink to="/events" activeClassName="text-amber-400">
            All Events
          </NavLink>
          <NavLink to="/create_event" activeClassName="text-amber-400">
            Create Events
          </NavLink>
          <NavLink to="/my_events" activeClassName="text-amber-400">
            My Events
          </NavLink>
          <NavLink to="/reviews" activeClassName="text-amber-400">
            Reviews
          </NavLink>
        </div>
        {/* Right */}
        <div className="flex items-center m-4 text-white">
          <div className="pr-4 pl-4">
            <p className="text-xs xl:text-sm ">Hello, sign in</p>
            <Link
              to={"/login"}
              className="text-sm xl:text-base font-bold cursor-pointer"
            >
              Account
            </Link>
          </div>
        </div>
      </div>
    </header>
  );
};

export default NavBar;
