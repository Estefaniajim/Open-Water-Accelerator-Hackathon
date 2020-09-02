import React from 'react';
import { Route } from 'react-router-dom';
import Home from './components/Home.js';
import Signup from './components/Signup.js';
import Address from './components/Address.js';
import Payment from './components/Payment.js';
import Browse from './components/Browse.js';
import Restaurant from './components/Restaurant.js';
import Info from './components/Info.js';
import Food from './components/Food.js';
import Cart from './components/Cart.js';
import './App.css';

class App extends React.Component {
  render() {
    
    return(
      <div>
      <Route exact path="/" component={Home}/>
      <Route exact path="/signup" component={Signup}/>
      <Route exact path="/address" component={Address}/>
      <Route exact path="/payment" component={Payment}/>
      <Route exact path="/browse" component={Browse}/>
      <Route exact path="/restaurants" component={Restaurant}/>
      <Route exact path="/restaurant" component={Info}/>
      <Route exact path="/food" component={Food}/>
      <Route exact path="/cart" component={Cart}/>
     
      </div>
    ) 
    
  }
}
export default App;
