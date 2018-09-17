import os

from jira import JIRA


class QueryJira:
    def __init__(self):
        with open(os.getenv('PRIVATE_PEM_KEY', 'pem_key_not_set'), 'r') as f:
            rsa_private = f.read()
        jira = JIRA(server=os.getenv('JIRA_BASE_URL', 'jira_url_not_set'),
                    oauth={
                        'access_token': os.getenv('ACCESS_TOKEN'),
                        'access_token_secret': os.getenv('ACCESS_TOKEN_SECRET'),
                        'consumer_key': os.getenv('CUSTOMER_KEY_JIRA'),
                        'key_cert': rsa_private}
                    )
        p = jira.projects()
        print(p)


QueryJira()
