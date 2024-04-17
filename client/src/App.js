import { Route, Routes } from "react-router-dom";
// import LoginUser from './components/SignIn';
import Home from "./components/Home";
import NavBar from "./components/NavBar";
import Footer from "./components/Footer";

function App() {
  return (
    <>
    <NavBar/>
      <Routes>
        <Route path="/" element={<Home />} />
        {/* <Route path="/Login" element={<LoginUser />} /> */}
      </Routes>
      <Footer />
    </>
  );
}

export default App;