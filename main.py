import yaml


def main():
    "Open the search pattern YAML file."
    with open("searchPatterns.yaml", "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    "Load studies."
    studies = data["studies"]
    for study_name, steps in studies.items():
        print(f"Study: {study_name}")

        "Flatten and print the search pattern steps."
        flat_steps = _flatten(steps)
        for step in flat_steps:
            print(step)
        print()


def _flatten(items):
    """Recursively flatten nested lists."""
    result = []
    for item in items:
        if isinstance(item, list):
            result.extend(_flatten(item))
        else:
            result.append(item)
    return result


if __name__ == "__main__":
    main()
