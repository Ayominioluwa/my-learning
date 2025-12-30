def add_setting(settings, key_value_pair):
    key, value = key_value_pair
    key, value = key.lower(), value.lower()
    if key in settings.keys():
        return f"Invalid entry: setting '{key}' already exists!"
    else: 
        settings[key] = value
        return f"Setting '{key}' successfully added as '{value}!'"
def update_setting(settings, key_value_pair):
    key, value = key_value_pair
    key, value = key.lower(), value.lower()
    if key not in settings.keys():
        return "Invalid entry: cannot update a non-existent setting!"
    else:
        settings[key] = value
        return f"Setting '{key}' successfully updated to '{value}'!"
def delete_setting(settings, key):
    key =  key.lower()
    if not key in settings.keys():
        return "Cannot delete setting which does not exist!"
    else:
        del settings[key]
        return f"Settting '{key}' deleted successfully!"
def view_settings(settings):
    if not settings:
        return "NANI?"
    else:
        display_settings = ""
        for key, value in settings.items():
            display_settings += f"{key.capitalize()}: {value}\n "
        return f"User Settings:\n {display_settings}"