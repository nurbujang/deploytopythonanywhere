from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello Ibu"

if __name__ == "__main__":
    app.run(debug = True)

# because I'm going to be do this on a different machine, I should set up a virtual environment to do that
# on linux: source ./venv/bin/activate
# pip freeze (there should be nothing in there)
# pip install flask
# now we can run the server 
# if u do ls, u should see thhis file there
# run this file, in output, u will get: http://127.0.0.1:5000 (open in browser)

# running: Hello Ibu
# Crtl C
# now we push this up to GH





