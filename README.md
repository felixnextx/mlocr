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
* Running on http://192.168.1.156:5001
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
