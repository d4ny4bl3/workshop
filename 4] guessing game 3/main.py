from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def guessing_game():
    return render_template("index.html", min=0, max=1000, guess=500, condition=False)


@app.route("/", methods=["POST"])
def guessing_game_post():
    min_number = int(request.form["min"])
    max_number = int(request.form["max"])
    user_input = request.form["user_input"]
    guess = int(request.form["guess"])
    condition = False

    if user_input == "Too small":
        min_number = guess
    elif user_input == "Too big":
        max_number = guess
    elif user_input == "You win":
        condition = True
        return render_template("index.html", guess=guess, condition=condition)

    guess = int(((max_number - min_number) / 2) + min_number)

    return render_template("index.html", min=min_number, max=max_number, guess=guess, condition=condition)


if __name__ == "__main__":
    app.run(debug=True)
