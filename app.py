from flask import Flask, render_template

app = Flask(__name__) #flask name instance is created and the "_name" tells Flask where to look for ther required templates and static files.

# Home Page/route
@app.route("/")
def home():
    return render_template('index.html')

#history page/route
@app.route("/history")
def history():
    return render_template('history.html')

if __name__ == "__main__":
    app.run(debug=True)