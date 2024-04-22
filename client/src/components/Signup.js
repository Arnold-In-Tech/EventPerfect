import React, { useEffect, useState } from "react";
import { useFormik, Formik, Form, Field, ErrorMessage } from "formik";
import * as yup from "yup";
import { useNavigate, Link } from "react-router-dom";


export default function Login() {
    const navigate = useNavigate();
    const [checked, setChecked] = useState(true);

    function handleCheckChange(event) {
      event.target.checked = false;
      setChecked(!checked);
    }

    const formSchema = yup.object().shape({
      full_name: yup.string().required("Fullname is required"),
      affiliation: yup.string(),
      location: yup.string(),
      contact: yup.number(),
      username: yup.string().required("Username is required"),
      password: yup.string()
        .min(6, "Password must be at least 6 characters")
        .required("Password is required"),
      image_url: yup.string(),
      bio: yup.string()
        .max(250, "Bio must be at most 250 words"),
      user_role: yup.string().required("User role is required"),
    });
      
    const formik = useFormik({
      initialValues: {
        full_name: "",
        affiliation: "",
        location: "",
        contact: "",
        username: "",
        password : "",
        image_url : "",
        bio: "",
        user_role: "",
      },
      validationSchema: formSchema,
      onSubmit: (values) => {
        fetch("/signup", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(values, null, 2),
        }).then((res) => {
          if (res.status == 201) {
            alert("Sign-Up successful, Welcome")
            navigate("/create_event");
          }else{
            alert("Error " + res.status + ": " + res.statusText + "\nTry Again")
          }
        });
      },
    });

    
    return (
        <div className="max-w-md mx-auto mt-8">
            <h2 className="text-2xl font-semibold mb-4">Sign Up</h2>
            <form onSubmit={formik.handleSubmit} style={{ margin: "30px" }}>

                {/* full_name */}
                <div className="mb-4">
                    <label htmlFor="full_name" className="block font-medium mb-1">
                    Full Name
                    </label>
                    <input
                        id="full_name"
                        type="text"
                        name="full_name"
                        className="form-input w-full"
                        onChange={formik.handleChange}
                        value={formik.values.full_name}
                    />
                    <p style={{ color: "red" }}> {formik.errors.full_name}</p>
                </div>

                {/* affiliation */}
                <div className="mb-4">
                    <label htmlFor="affiliation" className="block font-medium mb-1">
                    Affiliation
                    </label>
                    <input
                        id="affiliation"
                        type="text"
                        name="affiliation"
                        className="form-input w-full"
                        onChange={formik.handleChange}
                        value={formik.values.affiliation}
                    />
                    <p style={{ color: "red" }}> {formik.errors.affiliation}</p>
                </div>

                {/* location */}
                <div className="mb-4">
                    <label htmlFor="location" className="block font-medium mb-1">
                    Location
                    </label>
                    <input
                        id="location"
                        type="text"
                        name="location"
                        className="form-input w-full"
                        onChange={formik.handleChange}
                        value={formik.values.location}
                    />
                    <p style={{ color: "red" }}> {formik.errors.location}</p>
                </div>

                {/* contact */}
                <div className="mb-4">
                    <label htmlFor="contact" className="block font-medium mb-1">
                    Contact
                    </label>
                    <input
                        id="contact"
                        type="text"
                        name="contact"
                        className="form-input w-full"
                        onChange={formik.handleChange}
                        value={formik.values.contact}
                    />
                    <p style={{ color: "red" }}> {formik.errors.contact}</p>
                </div>

                {/* image_url */}
                <div className="mb-4">
                    <label htmlFor="image_url" className="block font-medium mb-1">
                    Image URL
                    </label>
                    <input
                        id="image_url"
                        type="text"
                        name="image_url"
                        className="form-input w-full"
                        onChange={formik.handleChange}
                        value={formik.values.image_url}
                    />
                    <p style={{ color: "red" }}> {formik.errors.image_url}</p>
                </div>

                {/* bio */}
                <div className="mb-4">
                    <label htmlFor="bio" className="block font-medium mb-1">
                    User Bio
                    </label>
                    <input
                        id="bio"
                        type="text"
                        name="bio"
                        className="form-input w-full"
                        onChange={formik.handleChange}
                        value={formik.values.bio}
                    />
                    <p style={{ color: "red" }}> {formik.errors.bio}</p>
                </div>

                {/* user role */}
                <div className="mb-4">
                    <label htmlFor="user_role" className="block font-medium mb-1">
                    User Role - Organizer / Attendee
                    </label>
                    <input
                        id="user_role"
                        type="text"
                        name="user_role"
                        className="form-input w-full"
                        onChange={formik.handleChange}
                        value={formik.values.user_role}
                    />
                    <p style={{ color: "red" }}> {formik.errors.user_role}</p>
                </div>

                {/* username */}
                <div className="mb-4">
                    <label htmlFor="username" className="block font-medium mb-1">
                    Username
                    </label>
                    <input
                        id="username"
                        type="text"
                        name="username"
                        className="form-input w-full"
                        onChange={formik.handleChange}
                        value={formik.values.username}
                    />
                    <p style={{ color: "red" }}> {formik.errors.username}</p>
                </div>
                
                {/* password */}
                <div className="mb-4">
                    <label htmlFor="password" className="block font-medium mb-1">
                    Password
                    </label>
                    <input
                        id="password"
                        type="text"
                        name="password"
                        className="form-input w-full"
                        onChange={formik.handleChange}
                        value={formik.values.password}
                    />
                    <p style={{ color: "red" }}> {formik.errors.password}</p>                    
                </div>

                <button
                    type="submit"
                    className="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600"
                >
                Submit
                </button>
            
            </form>
        </div>
        );
    };

// # =====


