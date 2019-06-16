from .Router import Router
from types import SimpleNamespace

class RouteHandler:
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

  def executeMiddlewares(self, req, *handlers):
    middlewares = self.Router.middlewares
    middlewareDatas = []
    for middleware in middlewares:
      if callable(middleware):
        middlewareDatas.append(middleware(req, *handlers))
    return middlewareDatas

  def executeRouteHandlers(self, path, method, req, *handler):
    paths = self.Router.paths
    method = method or 'get'
    currentRoute = paths.get(path)
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
    method = req.get('method')
    return self.executeRouteHandlers(path, method, req, *handlers)

  def register(self, mode = None):
    self.__mode = mode
    return self.handleRequest
  
