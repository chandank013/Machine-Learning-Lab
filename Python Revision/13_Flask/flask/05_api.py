### Put and Delete-HTTP Verbs
### Working With API's--Json

from flask import Flask, jsonify, request

app = Flask(__name__)

##Initial Data in my to do list
items = [
    {"id": 1, "name": "Item 1", "description": "This is item 1"},
    {"id": 2, "name": "Item 2", "description": "This is item 2"}
]

@app.route('/')
def home():
    return "Welcome To The Sample To DO List App"

## Get: Retrieve all the items

@app.route('/items',methods=['GET'])
def get_items():
    return jsonify(items)

## Get: Retireve a specific item by Id
@app.route('/items/<int:item_id>',methods=['GET'])
def get_item(item_id):
    item=next((item for item in items if item["id"]==item_id),None)
    if item is None:
        return jsonify({"error":"item not found"})
    return jsonify(item)

## Post :create a new task- API
@app.route('/items',methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"error":"item not found"})
    new_item={
        "id": items[-1]["id"] + 1 if items else 1,
        "name":request.json['name'],
        "description":request.json["description"]


    }
    items.append(new_item)
    return jsonify(new_item)

# Put: Update an existing item
@app.route('/items/<int:item_id>',methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item["id"] == item_id), None)
    if item is None:
        return jsonify({"error": "Item not found"})
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item)

# DELETE: Delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item["id"] != item_id]
    return jsonify({"result": "Item deleted"})




if __name__ == '__main__':
    app.run(debug=True)


'''
| **GET**     | Retrieve data from the server (read-only, no side-effects)             | Fetch a webpage, search query result       |
| **POST**    | Send data to the server to create a new resource                       | Submit form, register user                 |
| **PUT**     | Update an existing resource (or create if it doesn’t exist)            | Update user profile info in database       |
| **PATCH**   | Partially update an existing resource                                  | Change just the user's email               |
| **DELETE**  | Delete a resource from the server                                      | Remove a user account                      |
| **HEAD**    | Same as GET but only retrieves headers (no body/content)               | Check if a resource exists (metadata only) |
| **OPTIONS** | Get the allowed HTTP methods for a specific resource                   | Check allowed methods for an API endpoint  |
| **CONNECT** | Establish a tunnel to the server (mostly used for HTTPS proxy servers) | Secure connections, proxies                |
| **TRACE**   | Perform a message loop-back test along the path to the target resource | Debugging network routes  
'''


'''📌 What is Postman?
Postman is a popular API development and testing tool.
It allows developers to send HTTP requests to servers, view the responses, and test the behavior of APIs — without having to build a front-end or write client-side code.

It acts like a browser or client for sending requests, but much more powerful because you can control headers, request types (GET, POST, PUT, DELETE, etc.), authentication, body content, and see detailed responses.
'''