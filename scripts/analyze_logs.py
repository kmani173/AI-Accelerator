import os

log_file = "build.log"

if not os.path.exists(log_file):
    print("No build log found.")
    exit(0)

with open(log_file) as f:
    log = f.read()

print("\n========== AI BUILD ANALYSIS ==========\n")

if "BUILD SUCCESSFUL" in log:

    print("Status : SUCCESS")
    print("AI Recommendation : No issues detected.")

elif "';' expected" in log:

    print("Status : FAILED")
    print("Root Cause : Missing semicolon")
    print("Recommendation : Add ';' in App.java")

elif "cannot find symbol" in log:

    print("Status : FAILED")
    print("Root Cause : Java class or method missing")
    print("Recommendation : Check class names and imports.")

elif "package does not exist" in log:

    print("Status : FAILED")
    print("Root Cause : Missing package")
    print("Recommendation : Verify import statements.")

elif "Could not resolve dependencies" in log:

    print("Status : FAILED")
    print("Root Cause : Dependency issue")
    print("Recommendation : Check build.gradle")

elif "Permission denied" in log:

    print("Status : FAILED")
    print("Root Cause : Permission issue")
    print("Recommendation : Check file permissions.")

elif "git" in log.lower() and "error" in log.lower():

    print("Status : FAILED")
    print("Root Cause : Git checkout issue")
    print("Recommendation : Verify Git URL and credentials.")

else:

    print("Status : UNKNOWN")
    print("Recommendation : Review build log.")
