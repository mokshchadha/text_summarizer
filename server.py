from flask import Flask, request, jsonify
from bart_cnn import summarize_text

app = Flask(__name__)

 

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    text = data['text']
    summary = summarize_text(text)
    return jsonify({'summary': summary, 'text':data['text']})

if __name__ == '__main__':
    app.run(debug=True)