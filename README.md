# Fetch Receipt Processor

## Overview
This is a web service that processes receipt data and calculates reward points based on predefined rules. The service is implemented in Python using Flask and includes two endpoints:

1. **Process Receipts** (`POST /receipts/process`): Submits a receipt for processing and returns a unique receipt ID.
2. **Get Points** (`GET /receipts/{id}/points`): Retrieves the reward points for a processed receipt using its ID.

---

## Running with Docker
**Build the Docker Image:**
'docker build -t receipt-processor'

**Run the Docker Container:**
'docker run -p 8080:8080 receipt-processor'

**Access the Service**
The API will be available at 'http://localhost:8080'


