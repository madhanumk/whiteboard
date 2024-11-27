from decouple import config

# Load the project variable from the .env file
project = config('PROJECT', default='dev')

# Determine which settings to import based on the project variable
if project == 'LOCAL':
    print("Running development...", 'green')
    from .local import *
else:
    print("Running production...", 'green')
    from .dev import *
