# Jira OAuth Setup

This is an to come up with quick boilerplate code for set up and accessing JIRA using OAuth.

**Project contains:**
 1. **requirements.txt** comments indicate what are needed when. Run it using
     _`pip install -r requirements.txt`_
 2. **export_vars.sh** comments indicate what env's are required in each .py file. Do
     _`source export_vars.sh`_
 3. **oauth_generator.py** contains python logic to do the OAuth dance.
     1. This assumes that you already generated the pem key and pub key
     2. The pub key is shared with JIRA server and a customer_key is obtained in return
     3. Must: install the requirements and configure env vars (step 1 and 2)
     4. Follow instructions in console
 4. **access_using_jira_package.py** contains python logic to interact with JIRA using `jira` package
     1. This assumes that you already generated the pem key and pub key
     2. The pub key is shared with JIRA server and a customer_key is obtained in return
     3. Must: install the requirements and configure env vars (step 1 and 2)
 5. **access_using_requests_package.py** contains python logic to interact with JIRA using `requests` package
     1. This assumes that you already generated the pem key and pub key
     2. The pub key is shared with JIRA server and a customer_key is obtained in return
     3. Must: install the requirements and configure env vars (step 1 and 2)
