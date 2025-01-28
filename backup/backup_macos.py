import os
import shutil

def count_and_copy_files(source_directory, target_directory):
    """
    Counts the number of files and calculates the total disk space used,
    excluding the .local, .cache, and .DS_Store files, and mirrors the structure
    and files into a specified target directory.

    Args:
        source_directory (str): The path of the directory to analyze.
        target_directory (str): The path to the directory where files will be copied.

    Returns:
        tuple: A tuple containing the total number of files and the total size in bytes.
    """
    total_files = 0
    total_size = 0

    for root, dirs, files in os.walk(source_directory):
        # Skip .local, .cache, and any other system-specific directories
        dirs[:] = [d for d in dirs if d not in ['.local', '.cache']]

        # Create the corresponding directory in the target path
        relative_path = os.path.relpath(root, source_directory)
        target_path = os.path.join(target_directory, relative_path)
        os.makedirs(target_path, exist_ok=True)

        for file in files:
            # Skip .DS_Store and other system-specific files
            if file == ".DS_Store":
                continue

            source_file_path = os.path.join(root, file)
            target_file_path = os.path.join(target_path, file)

            if os.path.isfile(source_file_path):
                # Copy the file to the target directory
                shutil.copy2(source_file_path, target_file_path)

                # Update counts and size
                total_files += 1
                total_size += os.path.getsize(source_file_path)

    return total_files, total_size

def print_summary(total_files, total_size):
    """
    Prints a summary of the file count and total disk space used.

    Args:
        total_files (int): The total number of files.
        total_size (int): The total size in bytes.
    """
    print(f"Total files: {total_files}")
    print(f"Total disk space used: {total_size / (1024 * 1024):.2f} MB")

if __name__ == "__main__":
    source_directory = input("Enter the directory to analyze: ").strip()
    target_directory = input("Enter the target directory: ").strip()

    if not os.path.isdir(source_directory):
        print(f"Error: {source_directory} is not a valid directory.")
    elif not os.path.isdir(target_directory):
        print(f"Error: {target_directory} is not a valid directory.")
    else:
        total_files, total_size = count_and_copy_files(source_directory, target_directory)
        print_summary(total_files, total_size)
