from flask import Flask, render_template, request
from reddit_data import get_from_reddit

# Flask app
app = Flask(__name__)
app.config.from_pyfile("config.py")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        query = request.form.get("query")
        data = get_from_reddit(query)
        if data:
            return render_template("index.html", data=data, msg="Found something.")
        return render_template("index.html", msg="Item not found, sorry.")
    return render_template("index.html", msg="Go on, search for something.")


if __name__ == "__main__":
    app.run()
