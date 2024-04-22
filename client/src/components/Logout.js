import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

export default function Logout() {
    const navigate = useNavigate();

    function handleLogout() {
        fetch("/logout", {
        method: "DELETE",
        }).then(() => {
            alert("You have Logged Out, Goodbye!")
            navigate("/");
        });
    }
    
    return (
        <header>
        <button onClick={handleLogout}>Logout</button>
        </header>
    );
    }
          