from fastapi import FastAPI
from mangum import Mangum
from fastapi.middleware.cors import CORSMiddleware
from twitter import pre_filled_tweet
from marketResearch import gather_intelligence
from emailing import reach_out_email, reengagement_email, feedback_email

app = FastAPI()

# Handler for AWS lambda
handler = Mangum(app, lifespan="off")

# Allow api methods 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

## API Routes ##

# Generates tweet and returns it for the user
@app.get("/generate_tweet")
async def generate_tweet_api(prompt: str):
    tweet = pre_filled_tweet(prompt)
    return {"message": tweet}

# Generates a brief market research report and returns it for the user
@app.get("/gather_competitive_intel")
async def gather_competitive_intel(company: str):
    report = gather_intelligence(company)
    return {"message": report}

# Generates an email and returns it for the user
@app.get("/generate_email")
async def generate_email_sequences(recipient_name: str, recipient_title: str, recipient_company: str, sender_name: str, sender_company: str, sequence: str):
    match sequence:
        case "reach out":
            email = reach_out_email(recipient_name, recipient_title, recipient_company, sender_name, sender_company)
        case "re-engagement":
            email = reengagement_email(recipient_name, recipient_title, recipient_company, sender_name, sender_company)
        case "feedback":
            email = feedback_email(recipient_name, recipient_title, recipient_company, sender_name, sender_company)
    return {"message": email}