from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_word():
	return { "chave1": "hello world" }

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)