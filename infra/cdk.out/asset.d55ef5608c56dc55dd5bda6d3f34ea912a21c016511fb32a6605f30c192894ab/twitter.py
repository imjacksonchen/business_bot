import os

import openai

import urllib.parse

def generate_tweet(prompt):
    openai.api_key = os.getenv("OPEN_AI_API_KEY")
    response = openai.Completion.create(
        engine = "davinci-instruct-beta-v3",
        prompt = prompt,
        temperature = 1,
        max_tokens = 32
    )

    generated_tweet: str = response["choices"][0]["text"]
    generated_tweet = generated_tweet.strip()

    return generated_tweet

def pre_filled_tweet(topic):
    prompt = "Generate a business tweet of {}".format(topic)
    tweet = generate_tweet(prompt)
    encoding = urllib.parse.quote(tweet)
    link = "http://twitter.com/intent/tweet?text={}".format(encoding)
    return link