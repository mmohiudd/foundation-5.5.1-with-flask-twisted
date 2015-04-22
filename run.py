import sys
from twisted.web.wsgi import WSGIResource
from twisted.web.server import Site
from twisted.internet import reactor
from twisted.python.log import startLogging
from application import app

resource = WSGIResource(reactor, reactor.getThreadPool(), app)
site = Site(resource)
reactor.listenTCP(5050, site)
startLogging(sys.stdout)
reactor.run()
