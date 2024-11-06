import json
# TODO решите задачу
def task() -> float:
    with open ("input.json", 'r') as file:
        data = json.load(file)
        sum = 0
        for d in data:
            sum += d["score"] * d["weight"]
    return sum


print(f"{task():.3f}")
