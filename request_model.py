from load_properties import load_properties


class RequestModel:

    def __init__(self, path, request_section):
        """
        Initialize a RequestModel instance.
        Args:
            path (str): The path to the configuration file.
            request_section (str): The section in the configuration file
                that contains request-related properties.
        Attributes:
            hostname (str): The hostname from the configuration.
            headers (str): The user-agent headers from the configuration.
            params (str): The request parameters from the configuration.
        """
        self.hostname = load_properties(path=path,
                                        request_section=request_section,
                                        prop='request.hostname')
        self.headers = load_properties(path=path,
                                       request_section=request_section,
                                       prop='request.user-agent')
        self.params = load_properties(path=path,
                                      request_section=request_section,
                                      prop='request.params')
