import tableauserverclient as TSC
import os

class authorize:
    # define environment variables
    TOKEN_NAME = os.environ["TOKEN_NAME"]
    TOKEN_VALUE = os.environ["TOKEN_VALUE"]
    SITENAME = os.environ["SITENAME"]
    SERVER_URL = os.environ["SERVER_URL"]
    tableau_auth = TSC.PersonalAccessTokenAuth(TOKEN_NAME, TOKEN_VALUE, SITENAME)
    server = TSC.Server(SERVER_URL)