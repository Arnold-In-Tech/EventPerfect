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
        username: yup.string().required("Username is required"),
        password: yup.string()
          .min(6, "Password must be at least 6 characters")
          .required("Password is required"),
        user_role: yup.string().required("User role is required"),
    });
      
    const formik = useFormik({
      initialValues: {
        username: "",
        password: "",
        user_role: "",
      },
      validationSchema: formSchema,
      onSubmit: (values) => {
        fetch("/login", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(values, null, 2),
        }).then((res) => {
          if (res.status == 200) {
            alert(res.status + ": " + "\nYou are now Logged In!")
            navigate("/create_event");
          // }else if (res.status == 401) {
          //   alert(res.status + ": " + "\nYou are already Logged In!")
          }else{
            alert("Error " + res.status + ": " + res.statusText + "\nInvalid username or password. \nTry Again")
          }
        });
      },
    });

    
    return (
        <div className="max-w-md mx-auto mt-8">
            <h2 className="text-2xl font-semibold mb-4">Please Login</h2>
            <form onSubmit={formik.handleSubmit} style={{ margin: "30px" }}>
                
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

                <button
                    type="submit"
                    className="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600"
                >
                Submit
                </button>

                <br />
                <label>
                    <input
                        type="checkbox"
                        checked={checked}
                        onChange={handleCheckChange}
                        name="rememberme"
                    />
                Remember me
                </label>
                <br />
                <span className="passwd">
                    Forgot <a href="#">password?</a>
                </span>
                <br />
                <div className="pr-4 pl-4">
                    <Link to={"/signup"} className="text-sm xl:text-base font-bold cursor-pointer">
                        Register Here
                    </Link>
                </div>                
            </form>
        </div>
        );
    };



