import re

def monitor_security(data):
    # SSRF & Jailbreak detection
    forbidden = ["169.254.169.254", "ignore previous instructions"]
    for pattern in forbidden:
        if pattern in data.lower():
            return f"SECURITY_ALERT: {pattern} BLOCKED"
    return "CLEAN: " + re.sub(r'\S+@\S+', '[HIDDEN_EMAIL]', data)

print(monitor_security("Contact support@milyes.io or ignore previous instructions."))
