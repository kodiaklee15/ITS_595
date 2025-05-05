from openai import OpenAI
from flask import render_template, request, redirect, url_for, jsonify, Flask, session
from app import app
import os
from dotenv import load_dotenv
import json 

load_dotenv()

model_name = os.getenv("FINE_TUNED_MODEL")
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
app.secret_key = os.getenv("SECRET_KEY")



@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_name = request.form.get('name')
        if user_name:
            session['user_name'] = user_name  # Store name in session
            return redirect(url_for('order'))  # Redirect to order page
    return render_template('index.html')

@app.route('/order', methods=['GET', 'POST'])
def order():
    user_name = session.get('user_name', 'Guest')

    if request.method == 'POST':
        # Manually selected order details
        size = request.form['size']
        toppings = request.form.getlist('toppings')  # List of selected toppings
        quantity = request.form['quantity']
        sauce = request.form.get('sauce', 'tomato')  # Default to 'tomato' if not specified

        # Store the order data in the session
        session['order'] = {
            'size': size,
            'toppings': toppings,
            'quantity': quantity,
            'sauce': sauce
        }

        # Redirect to the confirmation page
        return redirect(url_for('confirmation'))

    return render_template('order.html', user_name=user_name)

@app.route('/ask_ai', methods=['POST'])
def ask_ai():
    data = request.get_json()
    user_message = request.get_json().get('message')

    if not user_message:
        return jsonify({'message': 'No message received. Please provide a description for the pizza order.'}), 400

    # Define the improved prompt to ensure a structured JSON response
    prompt = f"""
    You are a pizza ordering assistant. The user will describe their pizza order in natural language.
    Please return a **valid JSON** response that includes:
    - A field "response" which is a **natural language** confirmation for the user.
    - A field "order" which is the **pizza order details** with the following keys:
      - "size" (the size of the pizza)
      - "toppings" (a list of toppings for the pizza)
      - "quantity" (number of pizzas)
    - "sauce" (the type of sauce for the pizza, default to "tomato" if not specified)
    
    Example:
    {{
        "response": "Got it! A large pepperoni pizza with extra cheese has been added to your order.",
        "order": {{
            "size": "large",
            "toppings": ["pepperoni", "extra cheese"],
            "quantity": 1,
            "sauce": "tomato"
        }}
    }}

    The user’s order is: {user_message}
    """

    try:
        # Send the message to the fine-tuned model
        response = client.chat.completions.create(
            model=model_name,
            temperature=0,
            max_tokens=250,
            messages=[{"role": "user", "content": prompt}],
        )

        # Extract both parts of the response
        ai_reply = response.choices[0].message.content.strip()
        print(f"AI Reply: {ai_reply}")  # Debugging output to see the AI's response

        # Example: Splitting the JSON part and conversational part (assuming AI returns them in the correct format)

        try:
            # Attempt to parse the AI reply into structured JSON
            ai_response = json.loads(ai_reply)

            # Check if the AI returned the right keys in the JSON
            if "response" not in ai_response or "order" not in ai_response:
                return jsonify({
                    'reply': 'Sorry, I couldn’t process your order correctly. Could you clarify or rephrase it?',
                    'error': 'Invalid response structure from AI'
                })

            # Extract the natural language response and structured order
            user_reply = ai_response['response']
            order = ai_response['order']

            # Save the order data to the session
            session['order'] = order

            # Respond with the natural language reply and the structured order data
            return jsonify({
                'reply': user_reply,
                'order': order
            })

        except json.JSONDecodeError:
            # Handle case where AI doesn't return valid JSON
            return jsonify({
                'reply': 'Sorry, I couldn’t process your order correctly. Could you clarify or rephrase it?',
                'error': 'Invalid JSON response from AI'
            })

    except Exception as e:
        # Handle any errors with the AI request
        return jsonify({
            'message': f'Sorry, I couldn’t process your request at the moment. Error: {str(e)}'
        })
        
    
@app.route('/confirmation', methods=['GET', 'POST'])
def confirmation():
    # Retrieve order details from the session
    order = session.get('order')

    if not order:
        return redirect(url_for('order'))  # Redirect to order page if no order exists in session

    if request.method == 'POST':
        # User wants to modify their order, update the session
        size = request.form['size']
        toppings = request.form.getlist('toppings')
        quantity = request.form['quantity']
        sauce = request.form.get('sauce', 'tomato')

        # Update the session data with the modified order
        session['order'] = {
            'size': size,
            'toppings': toppings,
            'quantity': quantity,
            'sauce': sauce
        }

        return redirect(url_for('confirmation'))  # Redirect to confirmation page after modification

    return render_template('confirmation.html', size=order['size'], toppings=order['toppings'], quantity=order['quantity'], sauce=order['sauce'], user_name=session.get('user_name', 'Guest'))


@app.route('/order_confirmed', methods=['GET', 'POST'])
def order_confirmed():
    # Retrieve order details from the session
    order = session.get('order')

    # If no order is in session, redirect to the order page
    if not order:
        return redirect(url_for('order'))

    # Retrieve user name from session
    user_name = session.get('user_name', 'Guest')

    if request.method == 'POST':
        # Handle the final order confirmation logic here (e.g., storing the order in a database, etc.)
        # For now, just clear the session and show a final confirmation page.
        session.clear()  # Clear the session after confirmation
        return render_template('order_confirmed.html', user_name=user_name)  # Final confirmation page

    # Pass the order details to the confirmation page
    return render_template('order_confirmed.html', 
                           user_name=user_name,
                           size=order['size'], 
                           toppings=order['toppings'], 
                           quantity=order['quantity'], 
                           sauce=order['sauce'])

