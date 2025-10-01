# 🐍 Python Developer Challenge – Aptoide Scraper API

Welcome to the coding challenge! 🚀 
Your task is to build a Python-based API that scrapes package data from the Aptoide app store (https://en.aptoide.com/) and exposes it through a REST endpoint.

## 📋 Challenge Description

You are required to:  
1 - Develop an API (using FastAPI or Flask, your choice) that exposes an endpoint:
```
GET /aptoide?package_name=<package_id>
```

2 - This endpoint should:
  - Accept a package name as a query parameter (e.g. com.facebook.katana).
  - Scrape or fetch package details from Aptoide.
  - Return all relevant metadata about the app in JSON format.

## 🧾 Example

Request:
```
GET /aptoide?package_name=com.facebook.katana
```

Response (JSON):
```
{
  "name": "Facebook",
  "size": "152.5 MB",
  "downloads": "2B",
  "version": "532.0.0.55.71",
  "release_date": "2025-09-30 17:06:59",
  "min_screen": "SMALL",
  "supported_cpu": "arm64-v8a",
  "package_id": "com.facebook.katana",
  "sha1_signature": "8A:3C:4B:26:2D:72:1A:CD:49:A4:BF:97:D5:21:31:99:C8:6F:A2:B9",
  "developer_cn": "Facebook Corporation",
  "organization": "Facebook Mobile",
  "local": "Palo Alto",
  "country": "US",
  "state_city": "CA"
}
```

## ✅ Requirements

- Use Python 3.9+.
- Use a modern API framework (FastAPI preferred).
- Write clean, well-structured, and documented code.
- Ensure that errors (e.g. missing package, invalid input) are handled gracefully.
- Include instructions to run the project locally.

## 🚀 Deliverables

Create GitHub repository (and share the link with the Aptoide Recruitment team) containing:
- Your *source code*,
- A README.md with:
    - Setup instructions.
    - Example requests/responses.
    - Any assumptions or design decisions.

## 🎯 Evaluation Criteria

- Functionality & scalability
- Code readability & structure.
- API design principles.
- Error handling.
- Testing approach.

Good luck, and happy coding! 💻✨
