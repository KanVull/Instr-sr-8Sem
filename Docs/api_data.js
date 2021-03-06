define({ "api": [
  {
    "type": "delete",
    "url": "/ai-quotes",
    "title": "Delete quote",
    "name": "delete",
    "group": "Quote",
    "description": "<p>Delete quote by id from the xml files of quotes</p>",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "int",
            "optional": false,
            "field": "200",
            "description": "<p>Status code of request.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n    Quote with id 3 is deleted\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "int",
            "optional": false,
            "field": "400",
            "description": "<p>The <code>id</code> of the quote not exists.</p>"
          }
        ]
      }
    },
    "parameter": {
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"id\": 3\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "Code/main.py",
    "groupTitle": "Quote"
  },
  {
    "type": "get",
    "url": "/ai-quotes/:id",
    "title": "Request quote information by id",
    "name": "get",
    "group": "Quote",
    "description": "<p>Get quote by it's id</p>",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Int",
            "optional": false,
            "field": "id",
            "description": "<p>quote unique ID.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"id\": 1\n}",
          "type": "String"
        }
      ]
    },
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "json",
            "optional": false,
            "field": "quote",
            "description": "<p>The json contains id, author, quote text.</p>"
          },
          {
            "group": "Success 200",
            "type": "Int",
            "optional": false,
            "field": "200",
            "description": "<p>Status code of request.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 200 OK\n{\n\"id\": 1,\n\"author\": \"Elon Musk\",\n\"quote_text\": \"Mars is mine\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "int",
            "optional": false,
            "field": "404",
            "description": "<p>The <code>id</code> of the quote was not found.</p>"
          }
        ]
      }
    },
    "version": "0.0.0",
    "filename": "Code/main.py",
    "groupTitle": "Quote"
  },
  {
    "type": "post",
    "url": "/ai-quotes",
    "title": "Add new quote",
    "name": "post",
    "group": "Quote",
    "description": "<p>Add new quote (quote id, quote author, quote text) to the xml files of quotes</p>",
    "success": {
      "fields": {
        "Success 200": [
          {
            "group": "Success 200",
            "type": "int",
            "optional": false,
            "field": "201",
            "description": "<p>Status code of request.</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Success-Response:",
          "content": "HTTP/1.1 201 OK\n{\n    \"id\": 6,\n    \"auotor\": \"Elon Mask\",\n    \"quote_text\": \"Mars is mine\"\n}",
          "type": "json"
        }
      ]
    },
    "error": {
      "fields": {
        "Error 4xx": [
          {
            "group": "Error 4xx",
            "type": "int",
            "optional": false,
            "field": "400",
            "description": "<p>The <code>id</code> of the quote already exists.</p>"
          }
        ]
      }
    },
    "parameter": {
      "examples": [
        {
          "title": "Request-Example:",
          "content": "{\n    \"id\": 6,\n    \"auotor\": \"Elon Mask\",\n    \"quote_text\": \"Mars is mine\"\n}",
          "type": "json"
        }
      ]
    },
    "version": "0.0.0",
    "filename": "Code/main.py",
    "groupTitle": "Quote"
  }
] });
