# 🕵️ Reverse Engineering Challenge – Go Client API Discovery

Welcome to the technical challenge! 🚀
In this exercise, you will analyze a compiled Go client application and reverse-engineer how it communicates with a remote API.

Your goal is to discover the API contract (endpoint, protocol, and data format) used by the Go application and then reproduce the same request using Python.

## 📋 Challenge Description

Your tasks are to:

### 1 - Analyze the Go binary
Choose one of the binaries provided in this repository according with your OS and architecture (e.g. `client_linux_amd64`). **Please let us know if you need to use a different binary.**
Analyze the binary and determine:
- The API base URL
- The endpoint path
- The HTTP method
- The data serialization format (e.g. JSON, Protobuf, etc.)
- The request and response structure
- Any required headers

You may use any reasonable tools or techniques, such as:
- Static analysis (strings, file, go tool, etc.)
- Dynamic analysis (running the binary, inspecting traffic)
- Network inspection tools
- Reverse-engineering tools
- Artificial Intelligence tools 🤖

### 2 - Reproduce the request using Python
Create a Python script that:
- Sends exactly the same request as the Go client
- Uses the same serialization format
- Correctly parses the response
- Prints the same success message as the Go client


## Expected Behavior

Execute your Python script and it should print the same success message as the Go client, by calling the API directly.
```
Congrats!! You sent a valid request!
```


## ✅ Requirements

- Use Python 3.9+.
- Write clean, simple, well-structured, and documented script that is runnable with:
```
python3 client.py
```
- Ensure that errors (e.g. the API is not reachable...) are handled gracefully.
  

## 🚀 Deliverables

Create GitHub repository (and share the link with the Aptoide Recruitment team) containing:
- Your *source code*,
  - ```client.py```
- A **README.md** with:
  - How you analyzed the Go binary
  - How you discovered:
    - The endpoint
    - The request format
  - How to run your script
  - Any assumptions or trade-offs you made

## 🎯 Evaluation Criteria

- Reverse-engineering skills - Ability to infer protocol and behavior
- Systems understanding - HTTP, serialization, tooling
- Code quality	- Clean, readable Python
- Accuracy -	Request matches Go client behavior
- Documentation -	Clear explanation of reasoning
- Pragmatism - Realistic approach, **not overengineering**

Good luck, and happy coding! 💻✨
