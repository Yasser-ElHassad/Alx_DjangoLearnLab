##Obtaining a Token:
    Send a POST request to /api-token-auth/ with your username and password to receive a token.

##Using the Token:
    Include the token in the Authorization header of your requests:

    Authorization: Token your_token_here

##Permissions:
    Only authenticated users can access the endpoints protected by IsAuthenticated permission.
