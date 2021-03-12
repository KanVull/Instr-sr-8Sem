from flask import Flask
from flask_restful import Api, Resource, reqparse
import xml.etree.ElementTree as ET
import random
import json

def load_xml():
    tree = ET.parse('quotes.xml')
    return tree

def get_quote_dict(id, xml_file):
    quote = xml_file.find(f"quote[@id='{id}']")
    if quote is not None:
        d = {
            'id': quote.attrib['id'],
            'author': quote[0].text,
            'quote': quote[1].text,
        }
        return json.dumps(d)
    else:    
        return f'Quote with id {id} is not found'    

def write_in_xml(quote):
    pass


app = Flask(__name__)
api = Api(app)

class Quote(Resource):
    def get(self, id=0):
        if id == 0:
            paragraphs = xml_file.findall('//quote')
            return get_quote_dict(random.randint(1, len(paragraphs)), xml_file), 200
        quote = get_quote_dict(id, xml_file)
        if quote is not None:    
            return quote, 200
        return f'Quote with id {id} not found', 404


    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int)
        parser.add_argument('author')
        parser.add_argument('quote')
        params = parser.parse_args()
        d = get_quote_dict(quote['id'], xml_file)
        if d is not None:
            return f'Quote with id {params["id"]} already exists', 400
        quote = {
            'id': params['id'],
            'author': params['author'],
            'quote': params['quote'],
        }
        ai_quotes.append(quote)
        return quote, 201


    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('id')
        parser.add_argument('author')
        parser.add_argument('quote')
        params = parser.parse_args()
        for quote in ai_quotes:
            if(params['id'] == quote['id']):
                quote['author'] = params['author']
                quote['quote'] = params['quote']
                return quote, 200
        quote = {
            'id': params['id'],
            'author': params['author'],
            'quote': params['quote'],
        }
        ai_quotes.append(quote)
        return quote, 201        


    def delete(self, id):
        global ai_quotes
        ai_quotes = [quote for quote in ai_quotes if qouote["id"] != id]
        return f'Quote with id {id} is deleted.', 200    


api.add_resource(Quote, "/ai-quotes", "/ai-quotes/", "/ai-quotes/<int:id>")
if __name__ == '__main__':
    xml_file = load_xml()      
    app.run(debug=True)