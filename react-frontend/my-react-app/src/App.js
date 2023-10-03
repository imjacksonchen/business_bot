// src/App.js
import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Navbar from './Navbar';
import Home from './Home';
import Email from './Email';
import SocialMedia from './SocialMedia';
import MarketGPT from './MarketGPT';

function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/email" element={< Email />} />
          <Route path="/socialmedia" element={< SocialMedia />} />
          <Route path="/marketgpt" element={< MarketGPT />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
