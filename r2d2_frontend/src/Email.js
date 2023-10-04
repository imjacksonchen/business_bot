// src/Email.js
import React, { useState } from 'react';
import axios from 'axios';

function Email() {
    const [resultData, setResultData] = useState('');
    const [senderName, setSenderName] = useState('');
    const [senderCompany, setSenderCompany] = useState('');
    const [recipientName, setRecipientName] = useState('');
    const [recipientCompany, setRecipientCompany] = useState('');
    const [recipientTitle, setRecipientTitle] = useState('');
    const [sequence, setSequence] = useState('');
    const [isLoading, setIsLoading] = useState(false);

    // Next 6 functions to handle input changes
    const handleSenderNameChange = (event) => {
        // Update the state with the current input value
        setSenderName(event.target.value);
    };

    const handleSenderCompanyChange = (event) => {
        setSenderCompany(event.target.value);
    };

    const handleRecipientNameChange = (event) => {
        setRecipientName(event.target.value);
    };

    const handleRecipientCompanyChange = (event) => {
        setRecipientCompany(event.target.value);
    };

    const handleRecipientTitlChange = (event) => {
        setRecipientTitle(event.target.value);
    };

    const handleSequenceChange = (event) => {
        setSequence(event.target.value);
    };

    // Function to call the backend to generate an email based off the sequence
    const generateEmail = async () => {
        try {
            setIsLoading(true);
            // call to backend to generate a response
            const response = await axios.get(`https://tjw1whlolg.execute-api.us-east-2.amazonaws.com/prod/generate_email?recipient_name=${recipientName}&recipient_title=${recipientTitle}&recipient_company=${recipientCompany}&sender_name=${senderName}&sender_company=${senderCompany}&sequence=${sequence}`);
            setResultData(response.data);
            setIsLoading(false);
        } catch (error) {
            console.error('Error sending data:', error);
        }
    };

    // Results function to display the generated response
    const results = () => (
        <div class="card">
            <div class="card-header">
                Generated email
            </div>
            <div class="card-body">
                <blockquote class="blockquote mb-0 col">

                    <p>{resultData ? resultData.message : ''}</p>

                </blockquote>
            </div>
        </div>
    )

    return (
        <div class="col-auto my-4 mx-auto">
            <h2 class="text-center">Personalized Email Outreach: Auto-generate personalized email sequences</h2>

            <div class="my-4">
                <label for="exampleFormControlInput1" class="form-label">Enter your name:</label>
                <input type="text" value={senderName} onChange={handleSenderNameChange} class="form-control" style={{width: "300px"}} id="exampleFormControlInput1" placeholder="Andy Smith" />
            </div>

            <div class="my-4">
                <label for="exampleFormControlInput1" class="form-label">Enter your company:</label>
                <input type="text" value={senderCompany} onChange={handleSenderCompanyChange} class="form-control" style={{width: "300px"}} id="exampleFormControlInput1" placeholder="Pepsi" />
            </div>

            <div class="my-4">
                <label for="exampleFormControlInput1" class="form-label">Enter recipient's name:</label>
                <input type="text" value={recipientName} onChange={handleRecipientNameChange} class="form-control" style={{width: "300px"}} id="exampleFormControlInput1" placeholder="John Doe" />
            </div>

            <div class="my-4">
                <label for="exampleFormControlInput1" class="form-label">Enter recipient's company:</label>
                <input type="text" value={recipientCompany} onChange={handleRecipientCompanyChange} class="form-control" style={{width: "300px"}} id="exampleFormControlInput1" placeholder="Coca-Cola" />
            </div>

            <div class="my-4">
                <label for="exampleFormControlInput1" class="form-label">Enter recipient's job title:</label>
                <input type="text" value={recipientTitle} onChange={handleRecipientTitlChange} class="form-control" style={{width: "300px"}} id="exampleFormControlInput1" placeholder="CEO" />
            </div>


            <label class="form-label">Select Sequence:</label>

            <div>
                <select class="form-select" onChange={handleSequenceChange} aria-label="Default select example">
                    <option value="reach out" >Reach Out</option>
                    <option value="re-engagement">Re-engagement</option>
                    <option value="feedback">Feedback</option>
                </select>
            </div>

            <div class="my-4 mx-auto">
                <button type="button" class="btn btn-primary" disabled={isLoading} onClick={generateEmail}>Generate personalized email</button>
            </div>

            {resultData ? results() : ""}

        </div>
    );
}

export default Email;
