import json

# from jose import jwt, JWTError
from jwcrypto import jwk, jwt

from web.config import config


class JWTError(Exception):
    ''' An error occurred while validating the JWT. '''


def read_jwk_set(filename):
    ''' Read JWKs (JSON web keys) from a file and return a JWKSet. '''
    with open(filename) as f:
        jwk_set = jwk.JWKSet.from_json(f.read())

    return jwk_set


# Environment config
aws_region = config['aws']['region']
user_pool_id = config['aws']['cognito']['user_pool_id']
client_id = config['aws']['cognito']['client_id']

# Decode JWK set on start up
jwk_set = read_jwk_set('jwks.json')

# Set expected issuer
issuer = 'https://cognito-idp.{region}.amazonaws.com/{user_pool_id}'.format(
    region=aws_region, user_pool_id=user_pool_id)


def decode_jwt(token):
    ''' Decode and validate an incoming JWT against the JWK set. '''
    jwt_decoded = jwt.JWT(jwt=token, key=jwk_set)
    claims = json.loads(jwt_decoded.claims)

    # Verify claims
    if 'iss' not in claims or claims['iss'] != issuer:
        raise JWTError('Invalid issuer')

    if 'client_id' not in claims or claims['client_id'] != client_id:
        raise JWTError('Invalid client ID')

    if 'token_use' not in claims or claims['token_use'] != 'access':
        raise JWTError("Token use should be 'access'")

    # If no exception was raised, token is valid
    return claims
