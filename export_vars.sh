#!/usr/bin/env bash
### env needed to run oauth_generator.py ###
# corresponding pair of public key shared with JIRA server for OAuth
export PRIVATE_PEM_KEY='replace_me'
# customer key given while doing OAuth configuration in JIRA Server
export CUSTOMER_KEY_JIRA='replace_me'
# base url which is like 'https://<jira_server>'
export JIRA_BASE_URL='replace_me'


### env needed to run access_using_jira_package.py ###
# NOTE: All the env above are also needed
export ACCESS_TOKEN='replace_me'
export ACCESS_TOKEN_SECRET='replace_me'