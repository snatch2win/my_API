# http://127.0.0.1:5000/coin
# http://127.0.0.1:5000/coin/
# http://127.0.0.1:5000/coin/6

# curl-X PUT -H "Content-Type: application/json" -d '{"key1:"value}' "YOU_URI"
# curl-X PUT -H "Content-Type: application/json" -d '{"key1:"value}' "http://127.0.0.1:5000/coin/4"

from flask import Flask
from flask_restful import Api, Resource, reqparse
import random

my_list = [
    {
        "id": 1,
        "Coin": "Bitcoin",
        "Abbreviation": "BTC",
        "# in listing": "#1",
    },
    {
        "id": 2,
        "Coin": "Ethereum",
        "Abbreviation": "ETH",
        "# in listing": "#2",
    },
    {
        "id": 3,
        "Coin": "Tether",
        "Abbreviation": "USDT",
        "# in listing": "#3",
    },
    {
        "id": 4,
        "Coin": "USD Coin",
        "Abbreviation": "USDC",
        "# in listing": "#4",
    },
    {
        "id": 5,
        "Coin": "XRP (Ripple)",
        "Abbreviation": "XRP",
        "# in listing": "#7",
    },
    {
        "id": 6,
        "Coin": "Solana",
        "Abbreviation": "SOL",
        "# in listing": "#9",
    },
    {
        "id": 7,
        "Coin": "Dogecoin",
        "Abbreviation": "DOGE",
        "# in listing": "#10",
    },
    {
        "id": 8,
        "Coin": "Polkadot",
        "Abbreviation": "DOT",
        "# in listing": "#11",
    },
    {
        "id": 9,
        "Coin": "Litecoin",
        "Abbreviation": "LTC",
        "# in listing": "#20",
    },
    {
        "id": 10,
        "Coin": "Bitcoin Cash",
        "Abbreviation": "BCH",
        "# in listing": "#26",
    },
    {
        "id": 11,
        "Coin": "Monero",
        "Abbreviation": "XMR",
        "# in listing": "#27",
    },
    {
        "id": 12,
        "Coin": "Dash",
        "Abbreviation": "DASH",
        "# in listing": "#72",
    },
]

class CoinResource(Resource):
    def get(self, id=0):
        if id == 0:
            return random.choice(my_list), 200
        for val in my_list:
            if(val["id"] == id):
                return val, 200
        return "Error, no such id/coin", 404

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("Coin")
        parser.add_argument("Abbreviation")
        parser.add_argument("# in listing")
        params = parser.parse_args()
        for val in my_list:
            if (id == val["id"]):
                val["Coin"] = params["Coin"]
                val["Abbreviation"] = params["Abbreviation"]
                val["# in listing"] = params["# in listing"]
                return val, 200
        val = {
            "id": id,
            "Coin": params["Coin"],
            "Abbreviation": params["Abbreviation"],
            "# in listing": params["# in listing"],
        }
        my_list.append(val)
        return val, 201

    def post(self, id):
        parser = reqparse.RequestParser(location='form')
        parser.add_argument("Coin")
        parser.add_argument("Abbreviation")
        parser.add_argument("# in listing")
        params = parser.parse_args()
        for val in my_list:
            if (id == val["id"]):
                return f"This text with id={id} already exists", 400
        val = {
            "id": id,
            "Coin": params["Coin"],
            "Abbreviation": params["Abbreviation"],
            "# in listing": params["# in listing"],
        }
        my_list.append(val)
        return val, 201

    def delete(self, id):
        global my_list
        my_list = [val for val in my_list if val["id"] != id]
        return f"Record with id={id} was deleted!", 200


if __name__ == '__main__':
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(CoinResource, "/coin", "/coin/", "/coin/<int:id>")
    app.run(debug=True)



































































































