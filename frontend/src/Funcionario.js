import React, { Component } from "react";
import axios from "axios";
     



class Funcionario extends Component {
  constructor(props) {
      super(props);
        this.state = {
        someData: []
        }
      }
   
      componentDidMount() {
        axios
          .get("/api/funcionarios/"  + this.props.id)
          .then((res) =>(this.setState({ someData: res.data })) );
      }

    

  render() {
    

    return (
      <ul>
      <li>{this.state.someData.nome}</li>
      <li>{this.state.someData.cpf}</li>
      <li>{this.state.someData.rg}</li>
      <li>{this.state.someData.cnh}</li>
      <li>{this.state.someData.email}</li>
      <li>{this.state.someData.senha}</li>
  </ul>
      );
  }
}

export default Funcionario;