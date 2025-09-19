username = "admin"
password_length = 12
# --- Start your solution below this line --- #
if username == "admin":
    if password_length >= 10:
        print("Login successful.")
    else:
        print("Admin password incorrect:")
else:
    if password_length >= 6:
        print("Login successful.")
    else:
        print("User password must be 6+ characters.")
