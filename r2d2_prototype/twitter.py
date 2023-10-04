import os

import openai

import urllib.parse

""""
I chose Twitter as my use case of 
automating social media because 
I have worked with it before.

It is not fully possible to automate 
social media posting on Twitter. It 
would require the user to send an 
access token and key to allow a third
party application to handle the posting.

Therefore, I decided to go with the next
best thing, which is to provide a pre-filled
link of the tweet and be able to post it in
one click.
"""

# Function to generate a tweet based on the prompt
def generate_tweet(prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Completion.create(
        engine = "davinci-instruct-beta-v3",
        prompt = prompt,
        temperature = 1,
        max_tokens = 32
    )

    generated_tweet: str = response["choices"][0]["text"]
    generated_tweet = generated_tweet.strip()

    return generated_tweet

# Function concatnates the tweet and a link to allow a easy posting
def pre_filled_tweet(topic):
    prompt = "Generate a business tweet of {}".format(topic)
    tweet = generate_tweet(prompt)
    encoding = urllib.parse.quote(tweet)
    link = "http://twitter.com/intent/tweet?text={}".format(encoding)
    return link