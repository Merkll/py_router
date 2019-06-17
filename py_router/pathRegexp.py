import re

class PathMatch:
  def match(self, path, route):
    """
      Matches a route with a path . if a path is matched then a dictionary
      of the parameters is returned
    """
    # strips tailing / from paths to handle their presence or absense
    path = '/{path}/'.format(path = path.strip('/'))
    route = '/{route}/'.format(route = route.strip('/'))

    paramNames = re.findall(r':(.*?)/', path) # get names of parameters in path
    pathregex = re.sub(r':(.*?)/', '(.*?)/', path) # substitute all parameters with matching regular exp
    pathregex = '/{pathregex}/'.format(pathregex = pathregex.strip('/'))
    matched = re.match(pathregex, route) # matches the route
    print(pathregex, route)

    if not matched:
      return None
    
    params = { v: matched.group(i + 1) for i, v in enumerate(paramNames) }
    return { 'path': path, 'params': params, 'route': route }

  def matchMulti(self, paths, route):
    """
      This searches a list of paths and finds a match against a route 
    """
    print(paths, route)
    matched = list(filter(lambda path : self.match(path, route), paths))
    return matched


print(PathMatch().match('/users/:user/', '/users/45/about'))
# print(PathMatch().matchMulti(['/users/:user/:about/', '/users/:user/' ], '/users/45/about'))

  
