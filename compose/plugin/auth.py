from tyk.decorators import *
from gateway import TykGateway as tyk

import os
import sys
bundle_dir = os.path.abspath(os.path.dirname(__file__))
for lib_dir in [ 'vendor/lib/python3.7/site-packages/' ]:
  vendor_dir = os.path.join(bundle_dir, lib_dir)
  sys.path.append(vendor_dir)

import jwt

@Hook
def TokenAuth(request, session, metadata, spec):
  logLevel = "info"
  tyk.log("TokenAuth START", logLevel)
  # get the token out of the Auth header
  hydraToken = request.get_header('Authorization')
  tyk.log("TokenAuth: hydraToken from client header " + hydraToken, logLevel)
  # lookup the token in redis
  jot = tyk.get_data(hydraToken).decode()
  if len(jot):
    # token in redis
    tyk.log("TokenAuth: hydraToken found in redis " + jot, logLevel)
    # add the token to a header to pass upstream
    request.add_header("JWT-Header", jot)
    # extract client_id from the token and push it to the analytics
    decoded = jwt.decode(jot, options={"verify_signature": False})
    metadata["token"] = decoded["client_id"]
  else:
    # token not in redis
    tyk.log("TokenAuth: hydraToken NOT found in redis " + hydraToken, logLevel)
  tyk.log("TokenAuth: END", logLevel)
  return request, session, metadata

