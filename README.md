# mlocr

**mlocr** is a simple tool for recognizing chemical structure images and converting them to mol files, based on OSRA.

## Usage

### 1. Using Python
Clone the repository and navigate to the project folder:
```bash
git clone git@github.com:felixnextx/mlocr.git
cd mlocr
```

Install Flask:
```bash
pip install flask
```

Run the application:
```bash
python app.py
```
You should see output like this:
```bash
* Running on all addresses (0.0.0.0)
* Running on http://127.0.0.1:5001
```

### 2. Using Docker
Build the Docker image:
```bash
docker build -t mlocr:v1.0 .
```

Run the Docker container:
```bash
docker run -p 5000:5000 mlocr:v1.0
```

You can access the tool via Docker at http://localhost:5000.

### 3. API Usage
You can send a POST request to convert a base64-encoded image of a chemical structure to a mol file using the /base64img2mol endpoint.

Example using curl:
```bash
curl --location 'http://127.0.0.1:5000/base64img2mol' \
--header 'Content-Type: application/json' \
--data '{
    "img": "base64code"
}'
```
In the img field, replace "base64code" with your actual base64-encoded image of the chemical structure.
