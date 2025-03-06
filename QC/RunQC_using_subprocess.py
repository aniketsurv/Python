import subprocess

# Define the command to run your script
command = ['sudo', 'python3', 'qc_main.py']

# Run the command
result = subprocess.run(
    command,
    capture_output=True,  # Capture stdout and stderr
    text=True,           # Treat the output as text (str)
    cwd='/home/linaro/qualitycontrol'  # Set the working directory
)

# Print the stdout and stderr from the script
print("Standard Output:\n", result.stdout)
print("Standard Error:\n", result.stderr)

# Check if the script ran successfully
if result.returncode == 0:
    print("Script executed successfully")
else:
    print("Script execution failed with return code:", result.returncode)
