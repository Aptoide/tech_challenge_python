# Technical Challenge Python

## CODING ASSIGNMENT 💻
Build a Python script capable of performing HTTP requests with the correct parameters defined below:
1. **Search** and display to the console the list of apps obtained from the API call using the following URL:
   ```
   https://ws75.aptoide.com/api/7/apps/get/store_name=apps/q=bWF4U2RrPTE5Jm1heFNjcmVlbj1ub3JtYWwmbWF4R2xlcz0yLjA/group_name=games/limit=10/offset=0/mature=false
   ```
   **EXTRA:** Can you print to the console the decoded value of "q" parameter assuming that on the URL above it is a base64 encoded query string that summarises device specifications?

2. **Display** to the console the app description extracted from the app details (e.g. use the app ```com.fun.lastwar.gp```). Use the following URL:
   ```
   https://ws75.aptoide.com/api/7/app/get/store_name=apps/q=bWF4U2RrPTE5Jm1heFNjcmVlbj1ub3JtYWwmbWF4R2xlcz0yLjA/package_name=com.fun.lastwar.gp/language=pt_PT/
   ```
 
3. **Download** the app file (APK) by requesting the following URL:
   ```
   https://aptoide-mmp.aptoide.com/api/v1/download/b2VtaWQ9VGVjaENoYWxsZW5nZVB5dGhvbiZwYWNrYWdlX25hbWU9Y29tLmZ1bi5sYXN0d2FyLmdwJnJlZGlyZWN0X3VybD1odHRwczovL3Bvb2wuYXBrLmFwdG9pZGUuY29tL2FwcHMvY29tLWZ1bi1sYXN0d2FyLWdwLTk5OTk5LTY2NjEyOTMwLWE3MThmOWZlMjE5OGM1Y2EyYzIwMmUwNDYzZTVkZDk1LmFwaw==?resolution=1080x1776
   ```
   OPPSSS... It seems someone forgot to add a mandatory parameter. **Can you fix the previous URL by including the missing parameter with a dummy value** (e.g. testchallenge)?


## EVALUATION CRITERIA ✅
- The correct execution of the 3 previous steps.
- Correctness of the script implementation (with clear and well structured code).
- Clarity and simplicity of the README.md file (that explains how to run your script).

## SUBMISSION
Submit your project as a GitHub repository containing your code and the README.md and share the link with the Aptoide Recruitment team.