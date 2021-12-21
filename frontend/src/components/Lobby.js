import React from 'react';
import { BrowserRouter, Route, Routes, Link } from 'react-router-dom';

export default function Lobby() {
  return(
    <div>
        <div><Link to="/cliente">Cliente</Link></div>
        <div><Link to="/veiculo">Veiculo</Link></div>
        <div><Link to="/funcionario">Funcionario</Link></div>
        <div><Link to="/fornecedor">Fornecedor</Link></div>
    </div>
  );
}