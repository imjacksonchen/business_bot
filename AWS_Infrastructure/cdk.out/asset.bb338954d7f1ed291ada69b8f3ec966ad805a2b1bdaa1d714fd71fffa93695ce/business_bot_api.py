from fastapi import FastAPI
from mangum import Mangum
from twitter import pre_filled_tweet
from marketResearch import gather_intelligence
from emailing import reach_out_email, reengagement_email, feedback_email

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello"}

@app.get("/generate_tweet")
async def generate_tweet_api(prompt: str):
    tweet = pre_filled_tweet(prompt)
    return {"message": f"generated tweet: {tweet}"}

@app.get("/gather_competitive_intel")
async def gather_competitive_intel(company: str):
    report = gather_intelligence(company)
    return {"message": report}

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

handler = Mangum(app)