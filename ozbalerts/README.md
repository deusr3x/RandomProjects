# Ozbargin Live Alerts

## Summary
This project follows the Ozbargin website (www.ozbargin.com.au).  It sends a request to their live API once per minute to check for any new deals.
If the title of the deal contains a keyword, a notification will be sent via Slack.

## Setup
For Slack alerting, you will need to create a bot here https://api.slack.com/ and get a token.  Create an environment variable called SLACKTOKEN and set it to this value.
`export SLACKTOKEN=<TOKEN>`

Copy the subscription sample file `cp subscriptions_sample.yml subscriptions.yml` 
Then edit `subscriptions.yml` to suit your own needs.  The sample file has instructions.

Install the python requirements with `pip install -r requirements.txt`

Run with `python ozblalerts.py`

When an item appears with one of the keywords in the title, an alert will be sent to the slack user.