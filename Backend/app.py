from flask import flask, render_template, request, jsonify  #imports key Flask modules
import pandas as pd #imports pandas for handling csv

app = flask(__name__)  #initializes a flask web application. _name_ is what helps flask knwoe where to look for template files.

#   route for homepage / index
@app.route('/')  #this routes to homepage. This "/" sets the root URL (homepage) which when renders shows index.html
def index():
    return render_template('index.html')

#   route for handling form submission, file upload and processing
#   This "upload route" uploads the expected file from the form
@app.route('/upload', methods=['POST'])  #this route handles form submission. It only accepts POST requests
def upload_files():
    file = request.files['file']
    if file.filename.endswith('.csv'):  # checks if file is a csv and if so uses pandas to read it into a dataframe
        df = pd.read_csv(file)

        # Example processing: process data (phase 2 functions go here later)
        #dictionary below
        result = {
            "rows": len(df),
            "columns": list(df.columns)
        }

        return jsonify(result)
    return jsonify({"error": "Invalid File Format. Please upload a CSV file."})

# Run the app. Deubug=True means Flask will reload the server automactically on code changes, shows the errs in browser
if __name__ == '__main__':
    app.run(debug=True)  #runs the app in debug mode, which provides detailed error messages and auto-reloads on code changes