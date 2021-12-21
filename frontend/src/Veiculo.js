import React, { Component } from "react";
import axios from "axios";
     



class Veiculo extends Component {
  constructor(props) {
      super(props);
    this.state = {
        someData: []
        }
      }
   
    componentDidMount() {

      axios
      .get("/api/veiculos/" + this.props.id)
      .then((res) =>(this.setState({ someData: res.data })) );

    }

    

  render() {
    
    var myGPSString = String(this.state.someData.gps);
    var myTracaoString = String(this.state.someData.tracao);
    return (
        
      <ul>
        <li>{this.state.someData.classificacao}</li>
        <li>{this.state.someData.placa}</li>
        <li>{this.state.someData.cor}</li>
        <li>{this.state.someData.chassi}</li>
        <li>{this.state.someData.foto}</li>
        <li>{myGPSString}</li>
        <li>{this.state.someData.cadeiras}</li>
        <li>{myTracaoString}</li>
        <li>{this.state.someData.ultimadatadisponivel}</li>
        <li>{this.state.someData.idade}</li>
      </ul>
      );
  }
}

export default Veiculo;