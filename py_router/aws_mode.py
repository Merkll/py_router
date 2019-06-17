import json

def jsonLoad(string):
  data = string
  try:
    data = json.loads(string)
  except:
    pass
  finally:
    return data or {}

class AwsLambdaMode:
  def modifyRequest(self, req):
    req = json.loads(req)  if not isinstance(req, dict) else req
    path = req.get('path')
    method = req.get('httpMethod')
    body = jsonLoad(req.get('body'))
    query = jsonLoad(req.get('queryStringParameters'))
    params = jsonLoad(req.get('pathParameters'))
    req.update({ 'path': path, 'method': method, 'body': body, 'query': query, 'params': params })
    return req
