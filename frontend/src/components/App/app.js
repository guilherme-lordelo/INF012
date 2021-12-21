import Lobby from '../Lobby';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import React, { useState } from 'react';
import Dashboard from '../Dashboard';
import Login from '../Login/Login';
import Preferences from '../Preferences';
import Veiculo from '../../Veiculo';
import Cliente from '../../Cliente';
import Fornecedor from '../../Fornecedor';
import Funcionario from '../../Funcionario';
import './App.css';
import useToken from './useToken';



function App() {

  const { token, setToken } = useToken();


  if(!token) {
    return <Login setToken={setToken} />
  }
  
    return (
      <div className="wrapper">
        <h1>Locadora de Veiculos</h1>
        <BrowserRouter>
          <Routes>
          <Route path="/" element= {<Lobby/>} />
            <Route path="/cliente" element= {<Cliente id= "1"/>} />
            <Route path="/veiculo" element= {<Veiculo id= "1"/>}/>
            <Route path="/funcionario" element= {<Funcionario id= "1"/>}/>
            <Route path="/fornecedor" element= {<Fornecedor id= "1"/>}/>
          </Routes>
        </BrowserRouter>
      </div>
    );
  }
  export default App;