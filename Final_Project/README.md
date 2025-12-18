# AI Pizza Ordering Assistant

This project is an interactive **AI-powered pizza ordering web app** built using **Python Flask** and the **OpenAI GPT API**. The app allows users to either manually select pizza options or chat with an AI to place an order in natural language. The AI interprets the order and returns a structured summary for user confirmation or edits.

## Features

- **AI Chatbox Interface**: The AI can understand pizza orders like:  
  - `"Can I get a large pizza with mushrooms and extra cheese?"`
  
- **Fine-Tuned GPT Model**: The AI is fine-tuned to interpret pizza-related queries into a structured JSON object, which can then be used to process the order.

- **Order Summary & Confirmation Interface**: After the AI interprets the order, the user is shown a structured order summary, which they can confirm or modify.

---

## Project Structure

The project is organized as follows:

### **run.py** 
This is the main entry point to start the Flask application. Running this file will initiate the web server.

### **routes.py**
Contains all the app routes for handling different views (e.g., home page, order page, confirmation page). It also includes the logic for integrating the AI-powered ordering system.

### **/templates** 
This directory contains all the **HTML** files used to render the web pages. The key files include:
  - `index.html`: The starting page where the user enters their name.
  - `order.html`: The page where users can select pizza options or interact with the AI.
  - `confirmation.html`: The page showing a summary of the order before confirming.

### **/static**
This folder contains all the **static files** such as:
  - **/css**: Contains all the **CSS** files for styling the website (e.g., `indexUI.css`, `confirmationUI.css`, etc.).
  - **/js**: Contains JavaScript files such as `app.js` for frontend functionality.

### **.env** 
This file stores **environment variables** such as the OpenAI **API key**, the **fine-tuned model name**, and the **Flask secret key** for security.

### **pizza.jsonl** 
Contains a series of examples that demonstrate how the fine-tuned GPT model should return a structured response in JSON format based on different pizza order queries.

---

## How to Run the Project

1. **Clone the repository**:
2. **Run run.py to initiate the webapp**:
