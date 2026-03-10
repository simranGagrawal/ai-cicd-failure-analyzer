import re

log_file = "../logs/sample_pipeline.log"

def extract_errors(file):
    errors = []
    
    with open(file, "r") as f:
        for line in f:
            if "ERROR" in line or "ERR!" in line:
                errors.append(line.strip())

    return errors


def summarize_errors(errors):
    print("\nCI/CD Failure Analysis")
    print("----------------------")

    for error in errors:
        print("Detected Issue:", error)


if __name__ == "__main__":
    errors = extract_errors(log_file)
    summarize_errors(errors)
