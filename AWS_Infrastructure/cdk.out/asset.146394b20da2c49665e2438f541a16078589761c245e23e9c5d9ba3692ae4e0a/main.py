# main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from dotenv import load_dotenv
import os

import openai

app = FastAPI()

load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")

class Item(BaseModel):
    key: str

class EmailInfo(BaseModel):
    name: str
    title: str
    company: str
    industry: str

class TweetInfo(BaseModel):
    prompt: str

class MarketInfo(BaseModel):
    company_prompt: str

# CORS middleware to allow requests from the React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

### FUNCTIONS ###

def generate_personalized_email(name, title, company, industry):
    email = f'Hi {name}, {company} is a great company that is making huge advances in {industry}. As the {title}, I think you could benefit from our services...'
    return email

def generate_tweet(tweet_prompt):
    tweet = f'[Insert AI-Generated Tweet here with this prompt]: {tweet_prompt}'
    return tweet

def initialize_market_research(company):
    result = f'[AI powered research for this company]: {company}'
    return result

### API ###

@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}




@app.get("/email")
async def get_data():
    data = {"message": "Email use case"}
    return data

@app.post("/generateEmail")
def generate_email(item: EmailInfo):
    data = generate_personalized_email(item.name, item.title, item.company, item.industry)
    return {'data': {data}}




@app.get("/socialmedia")
async def get_data():
    data = {"message": "Social Media use case"}
    return data

@app.post("/generateTweet")
def create_tweet(tweet: TweetInfo):
    data = generate_tweet(tweet.prompt)
    return {'data': {data}}



@app.get("/marketgpt")
async def get_data():
    data = {"message": "MarketGPT use case"}
    return data

@app.post("/marketresearch")
def get_market_research(company: MarketInfo):
    data = initialize_market_research(company.company_prompt)
    return {'data': {data}}




@app.get("/data")
async def get_data():
    data = {"message": "Data from FastAPI backend"}
    return data

@app.post('/api/data')
def receive_data(item: Item):
    return {'data': f'Data received: {item.key}'}

@app.get("/items/{item_id}")
async def read_item(item_id: int, query_param: str = None):
    return {"item_id": item_id, "query_param": query_param}