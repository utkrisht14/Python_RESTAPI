from flask import Flask, request

app = Flask(__name__)

stores = [
    {
        "name": "My Store",
        "items": [
            {
                "name": "Chair",
                "Price": 15.99
            }
        ]
    }
]

@app.get("/")  # Now this handles the root URL
def home():
    return {"message": "Welcome to the Store API. Visit /store for store data."}

@app.get("/store")  # http://127.0.0.1:5000/store
def get_stores():
    return {"stores": stores}

@app.post("/store")
def create_store():
    request_data = request.get_json()
    new_store = {"name": request_data["name"], "items":[]}
    stores.append(new_store)
    return new_store, 201

@app.post("/store/<string:name>/item")
def create_item(name):
    request_data = request.get_json()
    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_data["name"], "price":request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message": "Store not found"}, 404


@app.get("/store/<string:name>")
def get_store(name):
    for store in stores:
        if store["name"] == name:
            return store
    return {"message": "Store not found."}, 404

@app.get("/store/<string:name>/item")
def get_item_in_score(name):
    for store in stores:
        if store["name"] == name:
            return {"items": store["items"]}
    return {"message": "Store not found."}, 404 

if __name__ == "__main__":
    app.run()
