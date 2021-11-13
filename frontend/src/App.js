import React, { Component } from 'react'

class App extends Component {
  state = {
    models: []
  };

  async componentDidMount(){
    try{
      const res = await fetch('http://127.0.0.1:8000/models/');
      const posts = await res.json();
      this.setState({
        models
      });
      
    }catch (e){
      console.log(e);
    }
  }
  render() {
    return(
      <div>
        {this.state.models.map(item =>(
          <div key={item.id}>
            <h1>{item.title}</h1>
            <span>{item.content}</span>
          </div>
        ))}
      </div>
    )
  }
  
}

export default App;

