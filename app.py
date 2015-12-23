import datetime
import os
import socket
import sys
import time

from collections import OrderedDict

import BaseHTTPServer

HTTPD_HOSTNAME = '0.0.0.0'
HTTPD_PORT = os.environ.get('PORT', 8080)
HTTPD_CONFIG = (HTTPD_HOSTNAME, HTTPD_PORT, )

START_TIME = datetime.datetime.now()

def timesince(start=None, now=None):
  """
  Modified from https://gist.github.com/nzjrs/207624

  """
  if not now:
    now = datetime.datetime.now()

  if start:
    dt = now - start
    offset = dt.seconds + (dt.days * 60*60*24)

  if offset:
    delta_s = offset % 60
    offset /= 60
    delta_m = offset % 60
    offset /= 60
    delta_h = offset % 24
    offset /= 24
    delta_d = offset

  else:
    raise ValueError("Must supply start or offset (from now)")

  if delta_d > 1:
    if delta_d > 6:
      date = now + datetime.timedelta(days=-delta_d, hours=-delta_h, minutes=-delta_m)
      return date.strftime('%A, %Y %B %m, %H:%I')
    else:
      wday = now + datetime.timedelta(days=-delta_d)
      return wday.strftime('%A')
  if delta_d == 1:
    return "Yesterday"
  if delta_h > 0:
    return "%dh %dm ago" % (delta_h, delta_m)
  if delta_m > 0:
    return "%dm %ds ago" % (delta_m, delta_s)
  else:
    return "%ds ago" % delta_s

def get_environment_variables():
  d = OrderedDict()
  for key in sorted(os.environ.keys()):
    d[key] = os.environ.get(key)
  return d

def get_uptime():
  return timesince(START_TIME)

def get_ip_addr():
  return socket.gethostbyname(socket.gethostname())

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
    s.wfile.write('<!DOCTYPE html><html lang="en"><head>')
    s.wfile.write('<title>Debug Server</title>')
    # bootstrap
    s.wfile.write("""<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">""")
    s.wfile.write('</head><body><div class="container">')

    s.wfile.write('<div class="page-header"><h1>%s<small>&nbsp;&nbsp;Booted: %s</small></h1></div>' % (get_ip_addr(), get_uptime(), ))

    s.wfile.write('<dl>')

    for key,value in get_environment_variables().items():
      s.wfile.write('<dt><strong>%s</strong></dt>' % key)
      s.wfile.write('<dd><code>%s</code></dd><br/>' % (value if value else 'NULL'))

    s.wfile.write('</dl>')

    s.wfile.write('</div></body></html>')


if __name__ == '__main__':
  httpd = BaseHTTPServer.HTTPServer(HTTPD_CONFIG, SimpleEnvironmentHandler)

  print time.asctime(), "Server starting up at %s:%s" % HTTPD_CONFIG

  try:
    httpd.serve_forever()
  except KeyboardInterrupt:
    pass

  print "Server shutting down."

  httpd.server_close()
