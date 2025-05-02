from flask import Flask, render_template, request, redirect, url_for, session
from reverse_string import reverse_string

app = Flask(__name__)
app.secret_key = 'dev_key_25'  

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            session['logged_in'] = True  
            return redirect(url_for('entry_page'))  # Redirect to the entry page on successful login
    return render_template('login.html', error=error)

# Route for the form page
@app.route('/')
def entry_page():
    if not session.get('logged_in'):
        return redirect(url_for('login'))  # Protect this route
    return render_template('entry.html', the_title="Reverse String App")

# Route for processing the form and showing the result
@app.route('/reverse', methods=['POST'])
def reverse():
    if not session.get('logged_in'):
        return redirect(url_for('login'))  # Protect this route too
    
    input_str = request.form['input_string']  # Get input from form
    reversed_str = reverse_string(input_str)  # Reverse the string

    return render_template(
        'results.html',
        the_title="Reversed String Result",
        the_input_string=input_str,
        the_results=reversed_str
    )

# Add logout route
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)  # Enable debugging