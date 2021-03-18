from flask import Flask
from flask_restful import Api, Resource, reqparse
import xml.etree.ElementTree as ET
import random
import json

xml_file = ''

def load_xml():
    tree = ET.parse('quotes.xml')
    return tree

def get_quote_dict(id):
    quote = xml_file.find(f"quote[@id='{id}']")
    if quote is not None:
        d = {
            'id': quote.attrib['id'],
            'author': quote[0].text,
            'quote': quote[1].text,
        }
        return json.dumps(d)
    else:    
        return None 

def write_in_xml(quote):
    q = ET.Element('quote')
    q.set('id', str(quote['id']))
    author = ET.SubElement(q, 'author')
    author.text = quote['author']
    quote_text = ET.SubElement(q, 'quote_text')
    quote_text.text = quote['quote']
    root = xml_file.getroot()
    root.append(q)
    xml_file.write('quotes.xml')
    return True

class Quote(Resource):

    """
        @api {get} /ai-quotes/:id Request quote information by id
        @apiName get
        @apiGroup Quote

        @apiDescription
            Get quote by it's id

        @apiParam {Int} id quote unique ID.

        @apiSuccess {json} quote The json contains id, author, quote text.
        @apiSuccess {Int} 200 Status code of request.
        
        @apiError {int} 404 The <code>id</code> of the quote was not found.

        @apiParamExample {String} Request-Example:
            {
                "id": 1
            }

        @apiSuccessExample {json} Success-Response:
            HTTP/1.1 200 OK
            {
            "id": 1,
            "author": "Elon Musk",
            "quote_text": "Mars is mine"
            }
    """
    def get(self, id=0):
        if id == 0:
            paragraphs = xml_file.findall('//quote')
            return get_quote_dict(random.randint(1, len(paragraphs))), 200
        quote = get_quote_dict(id)
        if quote is not None:    
            return quote, 200
        return f'Quote with id {id} not found', 404

    """
        @api {post} /ai-quotes Add new quote
        @apiName post
        @apiGroup Quote

        @apiDescription 
            Add new quote (quote id, quote author, quote text) to the xml files of quotes

        @apiSuccess {int} 201 Status code of request.
        
        @apiError {int} 400 The <code>id</code> of the quote already exists.

        @apiParamExample {json} Request-Example:
            {
                "id": 6,
                "auotor": "Elon Mask",
                "quote_text": "Mars is mine"
            }

        @apiSuccessExample {json} Success-Response:
            HTTP/1.1 201 OK
            {
                "id": 6,
                "auotor": "Elon Mask",
                "quote_text": "Mars is mine"
            }
    """
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int)
        parser.add_argument('author')
        parser.add_argument('quote_text')
        params = parser.parse_args()
        d = get_quote_dict(params['id'])
        if d is not None:
            return f'Quote with id {params["id"]} already exists', 400
        quote = {
            'id': params['id'],
            'author': params['author'],
            'quote': params['quote_text'],
        }
        write_in_xml(quote)
        return quote, 201    

    """
        @api {delete} /ai-quotes Delete quote
        @apiName delete
        @apiGroup Quote

        @apiDescription 
            Delete quote by id from the xml files of quotes

        @apiSuccess {int} 200 Status code of request.
        
        @apiError {int} 400 The <code>id</code> of the quote not exists.

        @apiParamExample {json} Request-Example:
            {
                "id": 3
            }

        @apiSuccessExample {json} Success-Response:
            HTTP/1.1 200 OK
            {
                Quote with id 3 is deleted
            }
    """
    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type=int)
        params = parser.parse_args()
        d = get_quote_dict(params['id'])
        if d is None:
            return f'Quote with id {params["id"]} not exists', 400
        root = xml_file.getroot()
        quote = xml_file.find(f'quote[@id="{params["id"]}"]')
        root.remove(quote)
        xml_file.write('quotes.xml')
        return f'Quote with id {params["id"]} is deleted.', 200    


app = Flask(__name__)
api = Api(app)

api.add_resource(Quote, "/", "/ai-quotes", "/ai-quotes/", "/ai-quotes/<int:id>")
if __name__ == '__main__':
    xml_file = load_xml()      
    app.run(debug=False, host='localhost', port='8888', ssl_context='adhoc')