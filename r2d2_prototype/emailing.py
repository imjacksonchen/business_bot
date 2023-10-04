import os

import openai

# Function to generate a an email based on the prompt
def generate_email(prompt):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Completion.create(
        engine = "davinci-instruct-beta-v3",
        prompt = prompt,
        temperature = 1,
        max_tokens = 300 # Limit tokens so that I don't spend all my credits on accident
    )

    # Parse out the generated response
    generated_email: str = response["choices"][0]["text"]
    # Remove any newline characters in the beginning of message
    generated_email = generated_email.lstrip()

    return generated_email

### Prompts for each sequence ###

def reach_out_email(recipient_name, recipient_title, recipient_company, sender_name, sender_company):
    reach_out_prompt = f"Generate a personalized message for business outreach for {recipient_name}, {recipient_title}, {recipient_company}. My name is {sender_name}, {sender_company}. With no fill ins and under 300 words."
    return generate_email(reach_out_prompt)
    
def reengagement_email(recipient_name, recipient_title, recipient_company, sender_name, sender_company):
    reengagement_prompt = f"Generate a personalized message for re-engaging {recipient_name}, {recipient_title}, {recipient_company} about a business outreach. My name is {sender_name}, {sender_company}. With no fill ins and under 300 words."
    return generate_email(reengagement_prompt)

def feedback_email(recipient_name, recipient_title, recipient_company, sender_name, sender_company):
    feedback_prompt = f"Generate a personalized message for {recipient_name}, {recipient_title}, {recipient_company} asking for feedback on our customer service. My name is {sender_name}, {sender_company}. With no fill ins and under 300 words."
    return generate_email(feedback_prompt)