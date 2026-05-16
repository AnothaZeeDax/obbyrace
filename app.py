from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    # Set your actual username here
    website_owner = "TitanicPrime"

    # Add your developers' names or aliases to this list
    # The HTML will automatically generate a sleek card for each developer added here
    developers = ["Amos_bad", "ZeeDax", "Dumphy", "Gakas", "rixze", "Jolly_lazydev1", "-Space-", "Afan kamaran"]

    return render_template('index.html', owner=website_owner, devs=developers)


if __name__ == '__main__':
    # Runs the local development server on http://127.0.0.1:5000/
    app.run(debug=True)