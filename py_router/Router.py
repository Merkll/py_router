class Router:
  def __init__(self):
    self.__paths = {}
    self.__middlewares = []
    self.__pathMiddlewares = {}

  @property
  def paths(self):
    return self.__paths
  
  @property
  def middlewares(self):
    return self.__middlewares
  
  @property
  def pathMiddlewares(self):
    return self.__pathMiddlewares

  def addRoute(self, path, method, *handler):
    path = '/{path}/'.format(path = path.strip('/')) if path != '/' else path
    pathData = { method: handler } if not path in self.paths else { **self.paths[path], **{ method: handler } }
    self.__paths.update({ path: pathData})
    return self

  def get(self, path, *handler):
    self.addRoute(path, 'get', *handler)
    return self
  
  def post(self, path, *handler):
    self.addRoute(path, 'post', *handler)
    return self

  def patch(self, path, *handler):
    self.addRoute(path, 'patch', *handler)
    return self

  def put(self, path, *handler):
    self.addRoute(path, 'put', *handler)
    return self

  def all(self, path, *handler):
    self.addRoute(path, 'all', *handler)
    return self

  # for middleware attachemnt
  def use(self, path, handler = None):
    if not handler:
      self.middlewares.append(path)
    else:
      middleware = { path: handler }
      self.__pathMiddlewares.update(middleware)
