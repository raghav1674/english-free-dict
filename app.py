import json
import os
from flask import Flask,request,jsonify
from utils.Trie import Trie


app = Flask(__name__)

# prepare the global search data
global_dict = Trie()
# https://raw.githubusercontent.com/matthewreagan/WebstersEnglishDictionary/master/dictionary.json
with open('data/dictionary.json') as dfp:
    dictionary = json.load(dfp)
    for each_word in dictionary:
        global_dict.insert(each_word.lower())

@app.route('/search',methods=['GET'])
def search():
    query = request.args.get('q')
    if global_dict.find(query):
        return jsonify({query:dictionary[query]})
    return jsonify({query:'word not found'})

@app.route('/suggestions',methods=['GET'])
def suggest():
    query = request.args.get('q')
    return jsonify({"suggestions":global_dict.autocomplete(query)})

PORT = os.getenv('PORT') or 6000

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=PORT)
