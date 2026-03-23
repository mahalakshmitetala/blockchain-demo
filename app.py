from flask import Flask, render_template, jsonify, request
import hashlib
import json
import time
import random
import datetime

app = Flask(__name__)

# Block class
class Block:
    def __init__(self, index, timestamp, data, previous_hash=''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = random.randint(1, 1000)
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = (
            str(self.index)
            + self.previous_hash
            + self.timestamp
            + json.dumps(self.data)
            + str(self.nonce)
        )
        return hashlib.sha256(value.encode()).hexdigest()

    def mine_block(self, difficulty):
        target = "0" * difficulty

        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()


# Blockchain class
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 2

    def create_genesis_block(self):
        return Block(
            0,
            str(datetime.datetime.now()),
            "Genesis Block",
            "0"
        )

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_block):
        new_block.previous_hash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_hash()
        self.chain.append(new_block)


blockchain = Blockchain()

# Create 5 blocks
for i in range(1, 6):
    blockchain.add_block(
        Block(
            i,
            str(datetime.datetime.now()),
            f"Block {i} Data"
        )
    )


@app.route("/")
def index():
    return render_template("index.html", chain=blockchain.chain)


# UPDATED MINE ROUTE WITH TIMESTAMP FEATURE
@app.route("/mine/<int:index>", methods=["POST"])
def mine(index):

    block = blockchain.chain[index]

    # get updated data
    data = request.json.get("data")
    block.data = data

    # 🔹 UPDATE TIMESTAMP WHEN BLOCK IS MINED
    block.timestamp = str(datetime.datetime.now())

    # recalc + mine
    block.hash = block.calculate_hash()
    block.mine_block(blockchain.difficulty)

    return jsonify({
        "hash": block.hash,
        "nonce": block.nonce,
        "timestamp": block.timestamp
    })


if __name__ == "__main__":
    app.run(debug=True)