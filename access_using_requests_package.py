import os

import requests
from requests_oauthlib import OAuth1


def get_jira_projects():
    oauth = get_oauth_session()
    session = requests.Session()
    session.auth = oauth
    session.headers.update({'X-Atlassian-Token': 'nocheck'})
    base_url = os.getenv('JIRA_BASE_URL', 'jira_url_not_set')
    url = base_url + '/rest/api/2/project'
    response = session.get(url)
    response.raise_for_status()
    print(response.text)


def get_oauth_session():
    with open(os.getenv('PRIVATE_PEM_KEY', 'pem_key_not_set'), 'r') as f:
        rsa_private = f.read()

    client_key = os.getenv('CUSTOMER_KEY_JIRA')
    resource_owner_key = os.getenv('ACCESS_TOKEN')
    resource_owner_secret = os.getenv('ACCESS_TOKEN_SECRET')

    return OAuth1(
        client_key=client_key,
        rsa_key=rsa_private,
        signature_method='RSA-SHA1',
        resource_owner_key=resource_owner_key,
        resource_owner_secret=resource_owner_secret
    )


get_jira_projects()
