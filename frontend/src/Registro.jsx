import React, { useState } from "react";
import axios from "axios";
import "./Registro.css";
function Registro() {
  const [formData, setFormData] = useState({
    username: "",
    email: "",
    password: "",
  });

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.post("http://127.0.0.1:8000/register", formData);
      console.log("✅ Usuario registrado:", res.data);
      alert("Usuario registrado correctamente ✅");
    } catch (error) {
      console.error("❌ Error en el registro:", error);
      alert("Error en el registro ❌");
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        name="username"
        placeholder="Usuario"
        value={formData.username}
        onChange={handleChange}
      />
      <input
        type="email"
        name="email"
        placeholder="Correo"
        value={formData.email}
        onChange={handleChange}
      />
      <input
        type="password"
        name="password"
        placeholder="Contraseña"
        value={formData.password}
        onChange={handleChange}
      />
      <button type="submit">Registrar</button>
    </form>
  );
}

export default Registro;
