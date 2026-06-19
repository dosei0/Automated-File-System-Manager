# Automated-File-System-Manager
A script that organises files in the Download folder of Windows, Linux and macOS,. It makes use of pathlib over os.path to demonstrate modern Python proficiency. Also made sure that there were zero external dependencies, this script only uses standard libraries meaning this script can run instantly on any machine without needing to run pip install, making it highly portable across a corporate network

## Scripts
For Windows: Open Task Scheduler, Create Basic Task, Set Trigger to prefered interval, Set Action to Start a Program and type python in program path and provide the file path as an argument.\
For macOS and Linux: Open a crontab using terminal command crontab -e and add the following code to run it every hour automatically:
```bash
0 * * * * /usr/bin/python3 /path/to/organise_downloads.py
```

## Technical Challenges Solved 
Cross-Platform Compatiblity: Used Path.home() to account for how operating systems handle user profiles differently.\
Risk Management: The script actively checks if directories exist, skips system hidden files, and explicitly blocks folders from moving into themselves.\
Collision Handling: Implementing a loop to rename files (e.g., file_1.pdf) instead of blindly overwriting data.\
Error Handling: Wrapping operations in try/except blocks for PermissionError or OSError as system environments are unpredictable (e.g., trying to move a file that a user still has open)
