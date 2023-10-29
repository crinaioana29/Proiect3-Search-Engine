import configparser


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
    config = configparser.RawConfigParser()
    config.read(path)
    return config.get(request_section, prop)
