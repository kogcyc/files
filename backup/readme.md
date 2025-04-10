 <p><span align="left">
  <img src="backup_logo.png" width="200" alt="backup_logo" />
</span>

# backup user files on Unix-y OSes #

This Python script recursively analyzes a given source directory, counts all files (excluding `.local` and `.cache` directories), calculates the total disk space used, and copies the directory structure and files to a specified target directory.

## Usage

```bash
    python3 backup_ubuntu.py
```

## Features

- Recursively walks through a directory
- Excludes `.local` and `.cache` directories
- Counts files and computes total disk space used
- Mirrors the source directory's structure and contents into a target directory
- Displays a summary of the operation

## MacOS version

The MacOS version skips .DS_Store files as well as .local and .cache. .DS_Store files are hidden metadata files automatically created by Finder in every folder. They store view preferences (icon positions, sorting order, etc.) and are not necessary for backup.

## Usage

```bash
    python3 backup_macos.py 
```
