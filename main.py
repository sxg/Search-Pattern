import yaml
import os


def main():
    # Open the search pattern YAML file.
    with open("searchPatterns.yaml", "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    # Create directory if it doesn't exist.
    output_dir = "Search Patterns"

    # Empty the output directory if it exists
    if os.path.exists(output_dir):
        for file in os.listdir(output_dir):
            file_path = os.path.join(output_dir, file)
            if os.path.isfile(file_path):
                os.remove(file_path)
    else:
        os.makedirs(output_dir)

    # Load studies.
    studies = data["studies"]
    for study_name, steps in studies.items():
        # Create a file path for this study.
        file_path = os.path.join(output_dir, f"{study_name}.txt")

        # Flatten and print the search pattern steps.
        flat_steps = _flatten(steps)

        # Write to file.
        with open(file_path, "w", encoding="utf-8") as output_file:
            for step in flat_steps:
                output_file.write(f"{step}\n")


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
