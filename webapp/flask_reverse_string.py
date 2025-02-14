from flask import Flask, render_template, request
from reverse_string import reverse_string

app = Flask(__name__)

# Route for the form page
@app.route('/')
def entry_page():
    return render_template('entry.html', the_title="Reverse String App")

# Route for processing the form and showing the result
@app.route('/reverse', methods=['POST'])
def reverse():
    input_str = request.form['input_string']  # Get input from form
    reversed_str = reverse_string(input_str)  # Reverse the string

    return render_template(
        'results.html',
        the_title="Reversed String Result",
        the_input_string=input_str,
        the_results=reversed_str
    )

if __name__ == '__main__':
    app.run(debug=True)  # Enable debugging
