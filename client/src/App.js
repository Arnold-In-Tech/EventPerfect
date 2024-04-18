import { Route, Routes } from "react-router-dom";
import NavBar from "./components/NavBar";
import Footer from "./components/Footer";
import Dashboard from "./components/Dashboard";
import AllEvents from "./components/AllEvents";
import Reviews from "./components/Reviews";
import Login from "./components/Login";
import Create_event from "./components/Create_event";
import My_events from "./components/My_events";

function App() {
  return (
    <>
      <NavBar />
      <Routes>
        <Route path="/" element={<Dashboard />} />
        <Route path="/events" element={<AllEvents />} />
        <Route path="/create_event" element={<Create_event />} />
        <Route path="/my_events" element={<My_events />} />
        <Route path="/reviews" element={<Reviews />} />
        <Route path="/login" element={<Login />} />
      </Routes>
      <Footer />
    </>
  );
}

export default App;
