from backend import app

@app.route('/')
def home():
    return 'Hello across-stack!'