## Secure Blockchain Visualizer

An interactive blockchain demonstration built using Python (Flask) to visualize block creation, hashing, mining, and chain dependency.

This project illustrates how blocks are linked using hashes and how modifying one block affects the entire blockchain.

## Features
- Interactive blockchain UI
- Block mining (Proof-of-Work simulation)
- SHA-256 hash generation
- Timestamp per block
- Previous hash linking
- Invalid chain highlighting
- Genesis block creation

## Tech Stack
- Python
- Flask
- HTML / CSS
- JavaScript
- CryptoJS (SHA256)

## Run Locally

### Get the code

```bash
git clone https://github.com/mahalakshmitetala/blockchain-demo.git
```

### Install dependencies

```bash
cd blockchain-demo
pip install flask
```

### Run the app

```bash
python app.py
```

## How It Works
- Each block stores previous block hash
- Changing block data breaks the chain
- Mining recalculates nonce and hash
- Valid chain appears in green
- Invalid chain appears in red

## Author
MahalakshmiTetala_323103210216
