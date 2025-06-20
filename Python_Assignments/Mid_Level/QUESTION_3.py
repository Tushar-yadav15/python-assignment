#3. Build a small command-line app to track quiz scores, stored in a CSV file.

import csv
import json
import os
from typing import List, Tuple

def load_scores(path: str) -> List[Tuple[str, int]]:
    """Loads scores from a CSV or JSON file based on extension."""
    records = []
    try:
        if path.endswith(".json"):
            with open(path, "r") as file:
                records = [(item["name"], int(item["score"])) for item in json.load(file)]
        else:
            with open(path, "r") as file:
                reader = csv.reader(file)
                for row in reader:
                    if len(row) == 2:
                        name, score = row
                        records.append((name, int(score)))
    except FileNotFoundError:
        print(" No existing file found. Starting with an empty list.")
    except Exception as e:
        print(f" Error loading file: {e}")
    return records

def save_scores(path: str, records: List[Tuple[str, int]]) -> None:
    """Saves scores to a CSV or JSON file."""
    try:
        if path.endswith(".json"):
            with open(path, "w") as file:
                json.dump([{"name": name, "score": score} for name, score in records], file)
        else:
            with open(path, "w", newline='') as file:
                writer = csv.writer(file)
                for name, score in records:
                    writer.writerow([name, score])
    except Exception as e:
        print(f" Error saving file: {e}")

def add_score(records: List[Tuple[str, int]], name: str, score: int) -> None:
    """Adds a new (name, score) to the list."""
    records.append((name, score))

def top_n(records: List[Tuple[str, int]], n: int) -> List[Tuple[str, int]]:
    """Returns top N scores, sorted in descending order."""
    return sorted(records, key=lambda x: x[1], reverse=True)[:n]

def delete_all_scores(records: List[Tuple[str, int]]) -> None:
    """Clears the score list after confirmation."""
    confirm = input("Are you sure you want to delete all scores? (yes/no): ").lower()
    if confirm == "yes":
        records.clear()
        print(" All scores deleted.")
    else:
        print(" Deletion cancelled.")

def print_menu():
    print("\n Menu:\n1. Show Top N Scores\n2. Add New Score\n3. Delete All Scores (Optional)\n4. Exit")

def main():
    path = "scores.csv"  
    records = load_scores(path)

    while True:
        print_menu()
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            try:
                n = int(input("Enter N (number of top scores to show): "))
                top_scores = top_n(records, n)
                print("\n Top Scores:")
                for i, (name, score) in enumerate(top_scores, 1):
                    print(f"{i}. {name} - {score}")
            except ValueError:
                print(" Please enter a valid number.")
        elif choice == "2":
            name = input("Enter name: ").strip()
            try:
                score = int(input("Enter score: "))
                add_score(records, name, score)
                save_scores(path, records)
                print(" Score added and saved.")
            except ValueError:
                print(" Invalid score. Please enter a number.")
        elif choice == "3":
            delete_all_scores(records)
            save_scores(path, records)
        elif choice == "4":
            print(" Exiting program. Goodbye!")
            break
        else:
            print(" Invalid option. Please select from the menu.")

if __name__ == "__main__":
    main()