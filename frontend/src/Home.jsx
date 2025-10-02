import React, { useState, useEffect } from "react";
import { useNavigate } from "react-router-dom";
import "./Home.css";

export default function Home() {
  const [darkMode, setDarkMode] = useState(false);
  const navigate = useNavigate();

  useEffect(() => {
    if (darkMode) document.body.classList.add("dark-mode");
    else document.body.classList.remove("dark-mode");
  }, [darkMode]);

  return (
    <div className="home-wrapper">
      {/* Barra superior */}
      <header className="top-nav">
        <div className="nav-left">
          <h2>BillCash</h2>
        </div>
        <div className="nav-right">
          <button className="btn-login" onClick={() => navigate("/login")}>
            Iniciar sesión
          </button>
          <button className="btn-signup" onClick={() => navigate("/registrar")}>
            Crear cuenta
          </button>
        </div>
      </header>

      {/* Hero */}
      <section className="hero-section">
        <div className="hero-text">
          <h1>Compra. Paga. Administra.</h1>
          <p>Tu billetera digital segura y fácil de usar</p>
          <div className="hero-buttons">
            <button className="btn-login" onClick={() => navigate("/login")}>
              Iniciar sesión
            </button>
            <button className="btn-signup" onClick={() => navigate("/registrar")}>
              Crear cuenta
            </button>
          </div>
        </div>
      </section>

      {/* Características */}
      <section className="features-section">
        <div className="feature-card">
          <h2>💳 Pagos rápidos</h2>
          <p>Envía y recibe dinero en segundos.</p>
        </div>
        <div className="feature-card">
          <h2>🔒 Seguridad</h2>
          <p>Protección de tus datos contra fraudes.</p>
        </div>
        <div className="feature-card">
          <h2>📊 Control total</h2>
          <p>Historial y reportes claros y accesibles.</p>
        </div>
      </section>

      {/* Footer */}
      <footer className="home-footer">
        <p>© {new Date().getFullYear()} BillCash. Todos los derechos reservados.</p>
      </footer>

      {/* Toggle modo oscuro */}
      <button
        className="dark-toggle"
        onClick={() => setDarkMode(!darkMode)}
        aria-label="Alternar modo oscuro"
      >
        {darkMode ? "Modo claro" : "Modo oscuro"}
      </button>
    </div>
  );
}
