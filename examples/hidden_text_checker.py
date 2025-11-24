print("Simple AI Cybersecurity Hidden Text Checker")

# Ask the user for a file to check
file_path = input("Enter the file path to scan: ")

try:
    with open(file_path, "r", encoding="utf-8") as f:
        data = f.read()
except FileNotFoundError:
    print("File not found. Please check the file name and try again.")
    exit()

print("\nScanning file...")

# --- Simple AI-like logic ---
suspicious = False

# Rule 1: detect Base64-like strings
if "==" in data or "==" in data:
    print("⚠️ Possible Base64 encoded text found.")
    suspicious = True

# Rule 2: detect very long words (common in hidden data)
for word in data.split():
    if len(word) > 30:
        print("⚠️ Found a very long string:", word[:30] + "...")
        suspicious = True
        break

# Rule 3: detect non-readable characters
if any(ord(c) > 126 for c in data):
    print("⚠️ File contains unusual characters.")
    suspicious = True

# Final "AI decision"
if suspicious:
    print("\nAI Decision: ❗ Suspicious content detected.")
else:
    print("\nAI Decision: ✓ File looks normal.")
