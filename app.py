from flask import Flask, render_template, request
app = Flask(__name__)

kinoko=3
takenoko=5
message=['kinoo is wondarfull']
@app.route('/')
def top():
    return render_template('index.html', **vars())

@app.route('/vote', methods=['POST'])
def answer():
    kinoko_per=kinoko/(kinoko+takenoko)*100
    takenoko_per=takenoko/(kinoko+takenoko)*100
    return render_template('vote.html', **vars())

if __name__ == '__main__':
    app.run(debug=True)
