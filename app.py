from flask import Flask, request, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

MONGO_URI = os.getenv('MONGO_URI', 'mongodb://database-service:27017/')
client = MongoClient(MONGO_URI)
db = client['comments_db']
collection = db['comments']

@app.route('/data/comments', methods=['GET'])
def get_comments():
    comments = list(collection.find({}, {'_id': 0}))
    return jsonify(comments)

@app.route('/data/comments', methods=['POST'])
def create_comment():
    data = request.json
    collection.insert_one(data)
    return jsonify(data), 201

@app.route('/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001)
