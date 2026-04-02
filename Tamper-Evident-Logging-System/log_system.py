import hashlib
import json
import time
import os


# function to generate SHA256 hash
def generate_hash(data):
    hash_object = hashlib.sha256(data.encode())
    return hash_object.hexdigest()


# function to load logs from file
def load_logs():

    if not os.path.exists("logs.json"):
        return []

    with open("logs.json", "r") as file:
        return json.load(file)


# function to save logs
def save_logs(logs):

    with open("logs.json", "w") as file:
        json.dump(logs, file, indent=4)


# function to add a log entry
def add_log():

    event = input("Enter event type: ")
    description = input("Enter description: ")

    logs = load_logs()

    timestamp = str(time.time())

    if len(logs) == 0:
        prev_hash = "0"
    else:
        prev_hash = logs[-1]["hash"]

    data = timestamp + event + description + prev_hash
    current_hash = generate_hash(data)

    log_entry = {
        "timestamp": timestamp,
        "event": event,
        "description": description,
        "prev_hash": prev_hash,
        "hash": current_hash
    }

    logs.append(log_entry)

    save_logs(logs)

    print("Log added successfully")


# function to verify log integrity
def verify_logs():

    logs = load_logs()

    if len(logs) == 0:
        print("No logs found")
        return

    for i in range(len(logs)):

        log = logs[i]

        data = log["timestamp"] + log["event"] + log["description"] + log["prev_hash"]
        recalculated_hash = generate_hash(data)

        if recalculated_hash != log["hash"]:
            print("Tampering detected in log", i + 1)
            return

        if i > 0:
            if log["prev_hash"] != logs[i - 1]["hash"]:
                print("Log chain broken at log", i + 1)
                return

    print("All logs are valid")


# function to display logs
def view_logs():

    logs = load_logs()

    if len(logs) == 0:
        print("No logs available")
        return

    for log in logs:
        print("\nTimestamp:", log["timestamp"])
        print("Event:", log["event"])
        print("Description:", log["description"])
        print("Hash:", log["hash"])


# main menu
while True:

    print("\nTamper Evident Logging System")
    print("1. Add Log")
    print("2. Verify Logs")
    print("3. View Logs")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_log()

    elif choice == "2":
        verify_logs()

    elif choice == "3":
        view_logs()

    elif choice == "4":
        print("Exiting program")
        break

    else:
        print("Invalid option")