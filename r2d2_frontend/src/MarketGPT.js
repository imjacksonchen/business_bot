// src/Email.js
import React, { useState } from 'react';
import axios from 'axios';

function Email() {
  const [marketData, setMarketData] = useState('');
  const [inputPrompt, setInputPrompt] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  // Function to handle input changes
  const handleInputChange = (event) => {
    // Update the state with the current input value
    setInputPrompt(event.target.value);
  };

  const handleKeyPress = e => {
    if (e.key === "Enter") {
      generateMarketResearch();
    }
  };


  const generateMarketResearch = async () => {
    try {
      setIsLoading(true);
      const response = await axios.get(`https://tjw1whlolg.execute-api.us-east-2.amazonaws.com/prod/gather_competitive_intel?company=${inputPrompt}`);
      setMarketData(response.data);
      setIsLoading(false);
    } catch (error) {
      console.error('Error sending data:', error);
    }
  };

  const results = () => {
    return (
      <div class="card">
          <div class="card-header">
            Generated market research
          </div>
          <div class="card-body">
            <blockquote class="blockquote mb-0 col">

            <p>{marketData ? marketData.message : '' }</p>

            </blockquote>
          </div>
        </div>
    )
  }

  return (
    <div class="col-auto my-4 mx-auto">
      <header>
        <h2 class = "text-center">MarketGPT: Automated complex competitor research using chains of tasks</h2>

        <div>
          <label for="exampleFormControlInput1" class="form-label">Enter a company:</label>
          <input type="text" value={inputPrompt} onKeyDown={handleKeyPress} onChange={handleInputChange} class="form-control" style={{width: "300px"}} id="exampleFormControlInput1" placeholder="Tesla" />
        </div>

        <div class="my-4 mx-auto">
        <button type="submit" class="btn btn-primary" disabled={isLoading} onSubmit={generateMarketResearch}>Generate Market Research</button>
        </div>

        {marketData ? results() : ""}

      </header>
    </div>
  );
}

export default Email;
