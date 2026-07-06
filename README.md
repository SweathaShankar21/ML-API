# Tiny ML API 

A minimal, production-ready model-serving backend built with **FastAPI**, **Pydantic**, and **scikit-learn**. 

This project takes machine learning logic out of offline notebooks and hosts it live on the web as a microservice, allowing external web and mobile applications to request real-time predictions.

##  Features
- **Strict Data Validation**: Uses Pydantic schemas to validate incoming payloads and block bad data types before they can crash the model.
- **Automated Testing Suite**: Built-in unit tests with Pytest to guarantee endpoint stability during updates.
- **Production-Ready Structure**: Clean separation of application endpoints and testing logic.

##  Repository Structure
```text
ML-API/
├── app.py             # Main FastAPI server and endpoint routing
├── requirements.txt   # Application dependencies
└── test_app.py        # Automated testing suite (Pytest)
```

##  Local Setup

1. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the local development server:**
   ```bash
   uvicorn app:app --reload
   ```
   The local server will spin up at `http://127.0.0.1:8000`. You can access the interactive documentation UI at `http://127.0.0`.

## Running Tests
To run the automated validation and endpoint health checks, execute:
```bash
pytest test_app.py
```
