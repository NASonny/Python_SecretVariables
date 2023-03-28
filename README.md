
# Secret variable environment in Python 

This project as to show how to have secret variable environment in Python



## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`ID_KEY = YOUR ID`





## How to do it ? 

Really simple thats how you gonna create your setup

First you will need to make an .env with your value | Check the file in the repository to have a example

After that you will need to make a folder env so you don't gonna use the variables which is in your pc

```http
  python -m venv env
```
The command above will create a folder env for the environement 

After that you have the folder env and the .env need you will use this command below to use the values in the .env

```http
  pip install python-dotenv
```
Configuration from environment variables so you will be able to take the value of the secret

And to finish you will make the main.py and add this command there: 
```http
  from dotenv import load_dotenv
```
And just under the command above you use this : 
```http
  load_dotenv()
```

Now you have all the step to use a simple variable environment secret with a .env in python 


For any documented information you can check the documents in the repository: 
https://github.com/SonnyNA/Python_SecretVariables
## Usage/Examples

```python

#####################################################################################
##      ##       ##                   Initialization              ##      ##       ##
#####################################################################################

import os
from dotenv import load_dotenv 

#####################################################################################
##      ##       ##                   Main Part                   ##      ##       ##
#####################################################################################

load_dotenv()

autor_id=os.getenv('ID_AUTOR')

print(autor_id)
```



By SonnyNA