import requests
import sys


def extract_errors(file):
    errors = []

    with open(file, "r") as f:
        for line in f:
            if "ERROR" in line or "ERR!" in line:
                errors.append(line.strip())

    return errors


def analyze_with_ai(errors):

    prompt = f"""
You are an experienced DevOps engineer.

Analyze the following CI/CD pipeline errors and provide:

1. Root cause
2. Suggested fix

Errors:
{errors}
"""

    response = requests.post(
        "http://host.docker.internal:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    data = response.json()

    return data.get("response", "No response from AI")


if __name__ == "__main__":

    if len(sys.argv) < 2:
        print("Usage: python analyzer.py <log_file>")
        sys.exit(1)

    log_file = sys.argv[1]

    errors = extract_errors(log_file)

    print("\nDetected Errors:")
    print(errors)

    print("\nAI Analysis:")

    if errors:
        analysis = analyze_with_ai(errors)
        print(analysis)
    else:
        print("No errors detected in logs.")
