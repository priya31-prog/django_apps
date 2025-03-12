// import logo from './logo.svg';
import './App.css';
// import { useEffect, useState } from 'react';
import AccountInfo from './components/AccountInfo';

function App() {

  return (
    <div className="App">
      <h1>Account Information</h1>
      <AccountInfo accountId='1'/>
   </div>
 )
}

export default App;
