import React from "react";
import { NavLink, Link } from "react-router-dom";

const NavBar = () => {
  return (
    <header className="min-w-[1000px]">
      <div className="flex bg-primary text-white h-[60px]">
        {/* Left */}
        <div className="flex items-center m-4 mr-[24]">
          <Link to={"/"}>
            <h2>
              <span className="text-amber-400">
                <strong className="text-xl">evento</strong>
              </span>
            </h2>
          </Link>
        </div>
        {/* Middle */}
        <div className="flex grow relative items-center space-x-7">
          {/* Navigation links */}
          <NavLink to="/dashboard" activeClassName="text-amber-400">
            Dashboard
          </NavLink>
          <NavLink to="/events" activeClassName="text-amber-400">
            All Events
          </NavLink>
          <NavLink to="/reviews" activeClassName="text-amber-400">
            Reviews
          </NavLink>
        </div>
        {/* Right */}
        <div className="flex items-center m-4">
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
