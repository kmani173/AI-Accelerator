import os

log_file = "build.log"

if not os.path.exists(log_file):
    print("No build log found.")
    exit(0)

with open(log_file, "r") as file:
    log = file.read()

print("\n========== AI BUILD ANALYSIS ==========\n")

if "BUILD SUCCESSFUL" in log:
    print("Status : SUCCESS")
    print("AI Recommendation : No issues detected.")
elif "Compilation failed" in log:
    print("Status : FAILED")
    print("Root Cause : Java Compilation Error")
    print("Recommendation : Check Java source code.")
elif "Could not resolve dependencies" in log:
    print("Status : FAILED")
    print("Root Cause : Dependency Error")
    print("Recommendation : Verify build.gradle dependencies.")
elif "git" in log.lower() and "error" in log.lower():
    print("Status : FAILED")
    print("Root Cause : Git Checkout Issue")
    print("Recommendation : Verify repository URL and credentials.")
else:
    print("Status : UNKNOWN")
    print("Recommendation : Review Jenkins build log.")
