# Technical Challenge Python

## PRE-REQUISITES 📝
To take this challenge you will need to build a minimal REST API in Python using a framework of your choice. The API should detect transaction anomalies (i.e. outliers that deviate significantly from the expected norm) and have a single GET endpoint that returns a simple report with the list of detected anomalies.

## INSTRUCTIONS 📃

**Before the live session:** 👨‍💻
You are expected to work on this task on your own, without help or advice from others. If you need clarification please seek help from Aptoide by emailing the Recruitment team.

**During the live session (technical interview with Aptoide developers):** 🫱‍🫲🏾
Walk through your code with the assessor, answering questions on the code and programming/design choices as requested by the assessor.

## CODING ASSIGNMENT 💻
1. Build a Python REST API capable of responding to HTTP GET requests at a specific endpoint, e.g., `/anomalies_report`.

2. Use the following [transactions dataset](https://github.com/Aptoide/tech_challenge_python/blob/main/transactions_dataset.csv) containing information about various financial transactions, each represented by several features:
```yaml
Transaction_ID: Unique identifier for each transaction.
Date: The date and time when the transaction occurred.
Transaction_Amount: The monetary value of the transaction.
```

3. Implement a logic for detecting anomalies in the provided dataset and return the list of anomalies when the GET endpoint is accessed. The response is in a JSON format, and it should look something like this:
```json
{"anomalies": [{"Transaction_ID": "TX59", 
                "Date": "2024-01-01 15:50", 
                "Transaction_Amount": 2769.890232},...]} 
```

## EVALUATION CRITERIA ✅
- Correctness of the API implementation (with clear and well structured code).
- Exception and error handling (that might occur during API operation).
- Clarity of the README.md file (that explains how to run your API and make a request to the endpoint using a tool like cURL).

## SUBMISSION
Submit your project as a GitHub repository containing your code and the README.md and share the link with Aptoide Recruitment team.