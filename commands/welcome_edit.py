def welcome_edit(new_message: str):
    with open("config.py", "r") as f:
        lines = f.readlines()

    with open("config.py", "w") as f:
        for line in lines:
            if line.startswith("WELCOME_MESSAGE"):
                f.write(f'WELCOME_MESSAGE = "{new_message}"\n')
            else:
                f.write(line)

    return f"Welcome message updated to:\n{new_message}"
