from flask import Flask, render_template, request, jsonify
import aiml
import os

app = Flask(__name__)

kernel = aiml.Kernel()

if os.path.exists("brain.brn"):
    kernel.loadBrain("brain.brn")
else:
    kernel.learn("startup.xml")
    kernel.respond("LOAD AIML B")
    kernel.saveBrain("brain.brn")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    bot_response = kernel.respond(userText)
    return jsonify(bot_response)

if __name__ == "__main__":
    app.run(debug=True)