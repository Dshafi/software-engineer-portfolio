def analyze_logs(file_path):
    errors = 0
    warnings = 0

    with open(file_path, "r") as file:
        for line in file:
            if "ERROR" in line:
                errors += 1
            elif "WARNING" in line:
                warnings += 1

    print("Log Analysis Report")
    print("-------------------")
    print(f"Total Errors: {errors}")
    print(f"Total Warnings: {warnings}")


if __name__ == "__main__":
    analyze_logs("log.txt")
