import json
import multiprocessing
import subprocess

def run_creater(entry):
    command = [
        'python',           # Replace with your Python executable if needed
        'creater.py',
        entry['name'],
        entry['domain'],
        entry['url'],
        entry['path'],
        entry['imgPath'],
        entry['description']
    ]

    try:
        subprocess.run(command, check=True)
        print(f"Successfully ran creater.py for {entry['name']}")
    except subprocess.CalledProcessError as e:
        print(f"Error running creater.py for {entry['name']}: {e}")

if __name__ == "__main__":
    # Load the information from info.json
    with open('info.json', 'r') as json_file:
        data = json.load(json_file)

    # Create a process for each entry in the JSON
    processes = []
    for entry in data:
        process = multiprocessing.Process(target=run_creater, args=(entry,))
        processes.append(process)
        process.start()

    # Wait for all processes to finish
    for process in processes:
        process.join()
