# R2D2 Prototype

This is a prototype of involve.ai's R2D2. This application is only for an assessment demonstration.

## Setup

**Frontend:** The frontend was set up with react. It utilizes the bootstrap library for CSS design. It has four pages: Home, MarketGPT, Automate Email Send, Automate Social Media Post. It contains five components:

- Home.js: A simple homepage for the user to land on when accessing the website.
s
- Navbar.js: A navigation bar for the user to switch between the use cases.

- MarketGPT.js: Page with an input response for a company and display the generated response.

- Email.js: Page with a few input reponses to generate an email in a specfic sequence of the email lifecycle.

- SocialMedia.js: Page with an input response for an item or service to generate a marketing tweet and display the link to post the tweet.

The frontend was intially set up by this command:

```javascript
npm create-react-app my-app
```

**Backend:** The backend was set up with Python to intake inputs and output responses. Working with the OpenAI and langchain API, it can take in a prompt and generate a response and be sent to the frontend for the user.

- business_bot_api.py: Contains three api calls that produce a response from a prompt.

- emailing.py: Contains the function that concatnates a prompt based on user input and calls the OpenAI api to generate an email

- marketResearch.py: Contains the function that concatnates a prompt based on user input and utilizes the langchain library to get up to date news on companies and information about their latest product/service.

- twitter.py: Contains the function that concatnates a prompt based on user input and calls the OpenAI api to generate a tweet and put it into a prefilled link for the user to post.

**Cloud Deployment:** The backend was deployed thorugh AWS' lambda and has a CICD pipeline set up with Codebuild and monitored by Cloudwatch. It was set up through the AWS CDK CLI. Eventually the building of the code and layer is automated through a yaml file. On Lambda, the four python files are the function code and the libraries are on one layer and the langchain library is on another layer (due to some error that the lambda function can't recognize the library when zipping the libraries along with langchain). CloudWatch is set up to monitor the CICD process and give us logs to look at.

**Frontend Deployment:** The frontend was deployed through a free cloud hosting service called Vercel. I connected thorugh the GitHub repository for it to build the frontend and have it live.

**Frontend and backend communication:** The frontend and backend communicates through API calls by utilizing the gateway API service through AWS.

**Local Testing/Hosting:** To run the application locally you will need to run the frontend with this command:

```javascript
npm start
```

To run the backend:

```python
uvicorn business_bot_api:app --reload
```

## Usage

The public live website is here: https://vercel.com/imjacksonchens-projects/business-bot 

Currently, the MarketGPT function is not working due to OpenAI mistakenly reducing the requests per minute to 3 during the beginning of the month. To make the function working again, I'll need to make another payment for the OpenAI API. Locally, it works as it keeps re-trying the API and eventually it'll get the generated response.

## Fututre Implementation

Currently, the application is a minimum viable product. It has a significant amounts of features and improvements that needs to implemented. This includes:

- Engineering prompts to produce the expected responses we want.

- Aggregating the MarketGPT tool with more information to improve the responses that are generated from langchain.

- Improving the user interface and experience with better design and intuitive user exploration flow.

- Implement more social media options (Instagram, Reddit, Facebook...).

- Implement tests so that the application is running correctly after every change and make sure it is running as expected before deploying.

- Implement constraints into the input on the frontend to reduce unexpected responses.

## Feedback

Feedback is welcomed to improve on the application.
