# Q1. Create two virtual environments, install few packages into first one. How do you create similar environment into second one?

''' Commands for Terminal''' # One-by-One

# Create Two Virtual Environments
'''
virtualenv env1
virtualenv env2

'''

# Activate env1
'''
.\env1\Scripts\activate.ps1

'''
# Install some packages into env1
'''
pip install pandas
pip install pyjokes

'''

# Fill in requirements.txt
'''
pip freeze > requirments.txt

'''

# Deactivate env1
'''
deactivate

'''

# Activate env2
'''
.\env2\Scripts\activate.ps1

'''

# Create a similar environment from env1 to env2
'''
pip install -r .\requirments.txt

'''

# '''# Done #'''