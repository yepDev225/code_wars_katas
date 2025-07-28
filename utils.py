import os
import sys
from dotenv import load_dotenv

load_dotenv(override=True)
def check_environment_variable(variable_name):
    """
    Check if an environment variable is defined.
    """
    if os.getenv(variable_name) is None:
        print(f"Environment variable '{variable_name}' is not defined.")
        sys.exit(1)
    else:
        return os.getenv(variable_name)
    
