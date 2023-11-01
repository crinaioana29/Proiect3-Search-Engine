import configparser
import os


def load_properties(path, request_section, prop):
    """
    Load a property from a configuration file.

    Args:
        path (str): The path to the configuration file.
        request_section (str): The section in the configuration file that contains
            the property you want to retrieve.
        prop (str): The name of the property you want to retrieve.

    Returns:
        str: The value of the specified property.
    """
    # Get the directory of the currently executing script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the absolute path to the configuration file
    config_file_path = os.path.join(script_dir, path)

    # Initialize the configuration parser and read the file
    config = configparser.RawConfigParser()
    config.read(config_file_path)

    # Now you can use config.get() to retrieve values
    return config.get(request_section, prop)