import sys
import os
import time
import datetime
from collections import OrderedDict

import BaseHTTPServer

HTTPD_HOSTNAME = '0.0.0.0'
HTTPD_PORT = os.environ.get('PORT', 8080)
HTTPD_CONFIG = (HTTPD_HOSTNAME, HTTPD_PORT, )

START_TIME = datetime.datetime.now()

def get_environment_variables():
  d = OrderedDict()
  for key in sorted(os.environ.keys()):
    d[key] = os.environ.get(key)
  return d

def get_uptime():
  return datetime.datetime.now() - START_TIME

class SimpleEnvironmentHandler(BaseHTTPServer.BaseHTTPRequestHandler):
  """
  Simple server to print out environment variables defined during invocation.

  """
  def do_HEAD(s):
    s.send_response(200)
    s.send_header("Content-type", "text/html")
    s.end_headers()

  def do_GET(s):
    s.send_response(200)
    s.send_header("Content-type", "text/html")
    s.end_headers()
    s.wfile.write("<html><head><title>Debug Server</title></head><body>")

    s.wfile.write("<p>Uptime: %s</p>" % get_uptime())

    s.wfile.write("<dl>")

    for key,value in get_environment_variables().items():
      s.wfile.write("<dt><strong>%s</strong></dt>" % key)
      s.wfile.write("<dd><code>%s</code></dd><br/>" % value)

    s.wfile.write("</dl>")

    s.wfile.write("</body></html>")


if __name__ == '__main__':
  httpd = BaseHTTPServer.HTTPServer(HTTPD_CONFIG, SimpleEnvironmentHandler)

  print time.asctime(), "Server starting up at %s:%s" % HTTPD_CONFIG

  try:
    httpd.serve_forever()
  except KeyboardInterrupt:
    pass

  print "Server shutting down."

  httpd.server_close()
