import os

log_file = "build.log"

# Check if build.log exists
if not os.path.exists(log_file):
    print("No build log found.")
    exit(0)

# Read build log
with open(log_file, "r") as f:
    log = f.read()

print("\n========== AI BUILD ANALYSIS ==========\n")

# Build Success
if "BUILD SUCCESSFUL" in log:

    print("Status : SUCCESS")
    print("AI Recommendation : No issues detected.")

# Missing Semicolon
elif "';' expected" in log:

    print("Status : FAILED")
    print("Root Cause : Missing semicolon")
    print("Recommendation : Add ';' in App.java")

# Variable Not Found
elif "symbol: variable" in log:

    print("Status : FAILED")
    print("Root Cause : Variable not found")
    print("Recommendation : Declare the variable before using it.")

# Method/Class Not Found
elif "cannot find symbol" in log:

    print("Status : FAILED")
    print("Root Cause : Java class or method missing")
    print("Recommendation : Check class names and imports.")

# Missing Package
elif "package does not exist" in log:

    print("Status : FAILED")
    print("Root Cause : Missing package")
    print("Recommendation : Verify import statements.")

# Dependency Issue
elif "Could not resolve dependencies" in log:

    print("Status : FAILED")
    print("Root Cause : Dependency issue")
    print("Recommendation : Check build.gradle dependencies.")

# Permission Issue
elif "Permission denied" in log:

    print("Status : FAILED")
    print("Root Cause : Permission issue")
    print("Recommendation : Check file permissions.")

# Git Checkout Issue
elif "git" in log.lower() and "error" in log.lower():

    print("Status : FAILED")
    print("Root Cause : Git checkout issue")
    print("Recommendation : Verify Git URL and credentials.")

# Unknown Error
else:

    print("Status : UNKNOWN")
    print("Recommendation : Review Jenkins build log.")
