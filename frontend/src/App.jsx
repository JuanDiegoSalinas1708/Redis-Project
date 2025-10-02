import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

import Home from "./Home.jsx";
import Registro from "./Registro.jsx";
import Login from "./Login.jsx";
import "./App.css";


export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/registrar" element={<Registro />} />
        <Route path="/login" element={<Login />} /> 
      
      </Routes>
    </Router>
  );
}
