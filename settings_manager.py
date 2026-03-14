def add_setting(settings:dict,new_setting:tuple):
    key,value = new_setting
    key = key.lower()
    value = str(value).lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"
    
def update_setting(settings:dict,new_setting:tuple):
    key,value = new_setting
    key = key.lower()
    value = str(value).lower()

    if key not in settings:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
    else:
        settings[key] = value
    return f"Setting '{key}' updated to '{value}' successfully!"

def delete_setting(settings: dict, key: str):
    key = key.lower()
    if key in settings:
        settings.pop(key)
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"


def view_settings(settings:dict):
    if not settings:
        return "No settings available."
    else:
        result = "Current User Settings:\n"
        for key,value in settings.items():
            result += f"{key.capitalize()}: {value}\n"
        return result