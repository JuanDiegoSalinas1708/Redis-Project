import React, { useState } from "react";
import axios from "axios";

const Login = () => {
  const [formData, setFormData] = useState({
    correo: "",
    password: "",
  });

  const [mensaje, setMensaje] = useState("");

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      // Enviar datos como form-data (porque el backend usa Form(...))
      const formDataToSend = new FormData();
      formDataToSend.append("correo", formData.correo);
      formDataToSend.append("password", formData.password);

      const response = await axios.post("http://127.0.0.1:8000/login", formDataToSend, {
        headers: { "Content-Type": "multipart/form-data" },
      });

      console.log("✅ Login exitoso:", response.data);

      // Guardar el token en localStorage
      localStorage.setItem("token", response.data.token);

      setMensaje("Login exitoso ✅");
    } catch (error) {
      console.error("❌ Error en el login:", error);
      setMensaje("Credenciales inválidas ❌");
    }
  };

  return (
    <div style={{ maxWidth: "400px", margin: "auto" }}>
      <h2>Iniciar Sesión</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Correo:</label>
          <input
            type="email"
            name="correo"
            value={formData.correo}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label>Contraseña:</label>
          <input
            type="password"
            name="password"
            value={formData.password}
            onChange={handleChange}
            required
          />
        </div>
        <button type="submit">Ingresar</button>
      </form>

      {mensaje && <p>{mensaje}</p>}
    </div>
  );
};

export default Login;
