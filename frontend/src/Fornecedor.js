import React, { Component } from "react";
import axios from "axios";
     



class Fornecedor extends Component {
  constructor(props) {
      super(props);
        this.state = {
        someData: [],
        }
      }
   
      componentDidMount() {
        axios
          .get("/api/fornecedores/"  + this.props.id)
          .then((res) =>(this.setState({ someData: res.data })) );
      }

    

  render() {
  

    return (
      <ul>
      <li>{this.state.someData.nome}</li>
      <li>{this.state.someData.cnpj}</li>
      <li>{this.state.someData.telefone}</li>
      <li>{this.state.someData.email}</li>
      <li>{this.state.someData.senha}</li>
  </ul>
      );
  }
}

export default Fornecedor;