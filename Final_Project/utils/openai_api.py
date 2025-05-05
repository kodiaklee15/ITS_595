import openai
import os
import re
from dotenv import load_dotenv

load_dotenv()

def get_openai_response(user_input):
    try:
        response = openai.chat.completions.create(
            model="ft:gpt-4o-2024-08-06:personal::BS8utEkb",  
            messages=[
                {
                    "role": "system",
                    "content": """
                    You are a pizza ordering assistant. Extract details in this format:
                    - Size: small/medium/large
                    - Toppings: comma-separated (e.g., pepperoni, mushrooms)
                    - Quantity: number
                    Respond with 'ORDER size:{size}, toppings:{toppings}, quantity:{quantity} DONE'.
                    For modifications, say 'ORDER UPDATE quantity:{new_quantity} DONE'.
                    """
                },
                {"role": "user", "content": user_input}
            ],
            temperature=0.2,
            max_tokens=200
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"OpenAI API error: {e}")
        return "Sorry, I couldn't process your request. Please try again."


MODEL_NAME = "ft:gpt-4o-2024-08-06:personal::BS8utEkb"  # Replace with your fine-tuned name once it's ready



