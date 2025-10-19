import os

def read_all_py_files(directory_path):
    """Reads all .py files in a directory and saves their names and contents to code.txt."""
    try:
        if not os.path.isdir(directory_path):
            raise FileNotFoundError(f"Directory not found: {directory_path}")

        print(f"📂 Reading Python files from: {directory_path}\n")

        all_text = []

        for file_name in os.listdir(directory_path):
            if file_name.endswith(".py"):
                file_path = os.path.join(directory_path, file_name)
                print(f"📄 Reading file: {file_name}")

                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read().strip()

                # Append formatted content to list
                all_text.append(f"\n\n==============================\n📄 File: {file_name}\n==============================\n{content}")

        # Save all collected code into code.txt
        output_path = os.path.join(directory_path, "code.txt")
        with open(output_path, "w", encoding="utf-8") as out_file:
            out_file.write("\n".join(all_text))

        print(f"\n✅ All .py files saved successfully to: {output_path}")

    except Exception as e:
        print(f"❌ Error while reading files: {e}")


# Example usage
if __name__ == "__main__":
    directory = "Matching"  # or full path
    read_all_py_files(directory)
