// src/SocialMedia.js
import React, { useState } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';

function Email() {
  const [tweetData, setTweetData] = useState('');
  const [inputPrompt, setInputPrompt] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  // Function to handle input changes
  const handlePromptChange = (event) => {
    // Update the state with the current input value
    setInputPrompt(event.target.value);
  };

  // Function to handle key press for Enter
  const handleKeyPress = e => {
    if (e.key === "Enter") {
      generateTweet();
    }
  };

  // Function to make a call to the backend to generate a tweet
  const generateTweet = async () => {
    try {
      setIsLoading(true);
      const response = await axios.get(`https://tjw1whlolg.execute-api.us-east-2.amazonaws.com/prod/generate_tweet?prompt=${inputPrompt}`);
      setTweetData(response.data);
      setIsLoading(false);
    } catch (error) {
      console.error('Error sending data:', error);
    }
  };

  // Results function to display the generated response
  const results = () => (
    <div class="card">
      <div class="card-header">
        Generated Tweet
      </div>
      <div class="card-body">
        <blockquote class="blockquote mb-0 col">

          {tweetData ? <Link target="_blank" to={tweetData.message}>Link to post tweet</Link> : ''}

        </blockquote>
      </div>
    </div>
  );

  return (
    <div class="col-auto my-4 mx-auto">
      <header>
        <h2 class="text-center">Social Media Posting: Automate social media post creations and posting</h2>

        <div class="mx-auto p-2">
          <div>
            <label for="exampleFormControlInput1" class="form-label">Enter a topic:</label>
            <input type="text" value={inputPrompt} onChange={handlePromptChange} onKeyDown={handleKeyPress} class="form-control" style={{ width: "300px" }} id="exampleFormControlInput1" placeholder="Coffee" />
          </div>

          <div class="my-4">
            <button type="submit" class="btn btn-primary" disabled={isLoading} onSubmit={generateTweet}>Generate Tweet</button>
          </div>
        </div>

        {tweetData ? results() : ""}

      </header>
    </div>
  );
}

export default Email;
