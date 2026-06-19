import os
import shutil
from pathlib import Path

# Mapping of file categories to their associated file extensions
CATEGORY_MAP = {
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv", ".epub"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".svg", ".webp", ".bmp", ".heic"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".m4a"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov", ".flv", ".wmv"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
    "Installers": [".exe", ".msi", ".dmg", ".pkg", ".deb", ".rpm"],
    "Code": [".py", ".js", ".html", ".css", ".json", ".xml", ".cpp", ".sh"]
}

def categorise_downloads():
    # Automatically locate the cross-platform system Downloads folder
    downloads_path = Path.home() / "Downloads"
    
    if not downloads_path.exists():
        print(f"Error: The directory {downloads_path} does not exist.")
        return

    print(f"Scanning: {downloads_path}\n")
    moved_count = 0

    # Iterate over items in the downloads directory
    for item in downloads_path.iterdir():
        # Skip directories to prevent moving existing categorization folders
        if item.is_dir() or item.name.startswith('.'):
            continue

        # Extract file extension in lowercase
        file_ext = item.suffix.lower()
        target_category = "Others"

        # Match extension to its respective category
        for category, extensions in CATEGORY_MAP.items():
            if file_ext in extensions:
                target_category = category
                break

        # Define destination path
        destination_dir = downloads_path / target_category
        destination_file = destination_dir / item.name

        try:
            # Create category directory if it doesn't exist
            destination_dir.mkdir(exist_ok=True)

            # Prevent overwriting files with identical names
            if destination_file.exists():
                stem = item.stem
                counter = 1
                while destination_file.exists():
                    destination_file = destination_dir / f"{stem}_{counter}{file_ext}"
                    counter += 1

            # Safely move file
            shutil.move(str(item), str(destination_file))
            print(f"Moved: '{item.name}' -> {target_category}/")
            moved_count += 1

        except (shutil.Error, PermissionError, OSError) as e:
            print(f"Failed to move '{item.name}': {e}")

    print(f"\nTask complete. Total files moved: {moved_count}")

if __name__ == "__main__":
    categorise_downloads()
