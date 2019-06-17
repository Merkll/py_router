from .Router import Router
from .pathRegexp import PathMatch
from types import SimpleNamespace

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class RouteHandler(metaclass = Singleton):
  def __init__(self):
    self.__router = Router()
    self.__mode = None
    self.__modeHandlers = {}

  @property
  def Router(self):
    return self.__router

  @property
  def Mode(self):
    return self.__mode

  @property
  def Paths(self):
    return self.Router.paths

  def executeMiddlewares(self, req, *handlers):
    middlewares = self.Router.middlewares
    middlewareDatas = []
    for middleware in middlewares:
      if callable(middleware):
        middlewareDatas.append(middleware(req, *handlers))
    return middlewareDatas

  def executeRouteHandlers(self, req, *handler):
    paths = self.Router.paths
    path = req.get('path')
    method = req.get('method') or 'get'
    currentRoute = paths.get(path) or {}
    routeHandler = currentRoute.get(method) or currentRoute.get('all') or []
    routeData = [] 
    for route in routeHandler:
      if (callable(route)):
        routeData.append(route(req, *handler))
    return routeData if len(routeData) > 0 else None

  def handleRequest(self, req, *handlers):
    self.executeMiddlewares(req, *handlers)
    if self.Mode and self.Mode in self.__modeHandlers:
      req = self.__modeHandlers[self.Mode].modifyRequest()
    path = req.get('path')
    matchedPath = PathMatch().matchMulti(self.Paths.keys(), path)
    if not matchedPath:
      return matchedPath
    req.update(matchedPath)
    return self.executeRouteHandlers(req, *handlers)

  def register(self, mode = None):
    self.__mode = mode
    return self.handleRequest