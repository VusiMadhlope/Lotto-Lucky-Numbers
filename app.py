from flask import Flask, render_template, request, jsonify
from quick_pick import generate_quick_picks, number_of_boards, number_of_draws, compare_winning_numbers
import script #importing the Script.py file
from history import load_history, save_user_numbers 

app = Flask(__name__) #flask name instance is created and the "_name" tells Flask where to look for ther required templates and static files.


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/history")
def history_page():
    return render_template('history.html')

@app.route("/quick_pick.html")
def quick_pick_page():
    return render_template('quick_pick.html')


@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get('file')
    if not file:
        return jsonify({"error": "No file provided"}), 400

    # step: call into script
    draws = script.dataProcessing(file)
    return jsonify({"rows": len(draws)})

if __name__ == "__main__":
    app.run(debug=True)
    boards = number_of_boards()
    draws = number_of_draws()
    user_boards = generate_quick_picks(boards)

    print(f"You have played {boards} boards and {draws} draws.")
    print("Your boards are: ", user_boards)

    comparison = compare_winning_numbers(user_boards)
    print("Winning Numbers: ", comparison["winning numbers"])
    for r in comparison["results"]:
        print(f"Board: {r['board']} | Matches: {r['matches']} | Match Count: {r['match_count']} | WIN: {r['win']}")


@app.route("/api/quick_pick", methods=["POST"])
def api_quick_pick():
    data = request.json()
    boards = int(data.get('boards', 1))
    draws = int(data.get('draws', 1))

    if not(1 <= boards <= 5) or not (1 <= draws <= 5):
        return jsonify({"error: Boards and draws must be between 1 and 5"}), 400 
    
    all_draws = []

    for _ in range(draws):
        generated_boards = generate_quick_picks(boards)
        all_draws.append(generated_boards)

    return jsonify({
        "boards": boards,
        "draws": all_draws,
        "results": all_draws
        })

if __name__== "__main__":
    app.run(debug=True)