import sys

def parse_log_line(line: str) -> dict:
    parts = line.split()
    if len(parts) < 3:
        raise ValueError("Invalid log format")
    return {
        "timestamp": " ".join(parts[:2]),
        "level": parts[2],
        "message": " ".join(parts[3:])
    }

def load_logs(file_path: str) -> list:
    try:
        with open(file_path, 'r') as file:
            return [parse_log_line(line.strip()) for line in file if line.strip()]
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        raise

def filter_logs_by_level(logs: list, level: str) -> list:
    return list(filter(lambda log: log['level'] == level, logs))

def count_logs_by_level(logs: list) -> dict:
    counts = {}
    for log in logs:
        counts.setdefault(log['level'], 0)
        counts[log['level']] += 1
    return counts

def display_log_counts(counts: dict):
    print(f"{'Рівень логування':<15} | {'Кількість':<10}")
    print("-" * 27) 
    for level, count in sorted(counts.items(), key=lambda item: item[1], reverse=True):
        print(f"{level:<15} | {count:<10}")

def display_specific_logs(logs: list, level: str):
    print(f"\nДеталі логів для рівня '{level}':")
    for log in logs:
        if log['level'] == level:
            print(f"{log['timestamp']} - {log['message']}")

def main():
    if len(sys.argv) < 2:
        print("Usage.error")
        sys.exit(1)

    file_path = sys.argv[1]
    logs = load_logs(file_path)
    log_counts = count_logs_by_level(logs)
    display_log_counts(log_counts)

    if len(sys.argv) == 3:
        log_level = sys.argv[2].upper()
        specific_logs = filter_logs_by_level(logs, log_level)
        display_specific_logs(specific_logs, log_level)

if __name__ == "__main__":
    main()
