import re

class PathMatch:
  def match(self, path, route):
    """
      Matches a route with a path . if a path is matched then a dictionary
      of the parameters is returned
    """
    # strips tailing / from paths to handle their presence or absense
    path = '/{path}/'.format(path = path.strip('/')) if path != '/' else path
    route = '/{route}/'.format(route = route.strip('/')) if route != '/' else route

    paramNames = re.findall(r':(.*?)/', path) # get names of parameters in path
    pathregex = re.sub(r':(.*?)/', '([^/]*?)/', path).strip('/') # substitute all parameters with matching regular exp
    matched = re.match(f'{pathregex}$', route.strip('/')) # matches the route

    if not matched:
      return None
    
    params = { v: matched.group(i + 1) for i, v in enumerate(paramNames) }
    return { 'path': path, 'params': params, 'route': route }

  def matchMulti(self, paths, route):
    """
      This searches a list of paths and finds a match against a route 
    """
    # print(paths, route)
    matched = list(map(lambda path : self.match(path, route), paths))
    matched = list(filter(None, matched))
    return matched[0] if len(matched) >= 1 else None
