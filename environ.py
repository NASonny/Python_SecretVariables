import os #Import os to allow recovery of the secret in the .env

from dotenv import load_dotenv 

load_dotenv() # set the load_dotenv to take the value from the .env

autor_id=os.getenv('ID_AUTOR') # This is what you want to get so if you need the secret password you right in the os.getenv('PASSWORD') so switch the name variable

print(autor_id) # verified print to know if the value is correct or None