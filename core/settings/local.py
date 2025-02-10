from core.settings.base import *

DEBUG = True
ALLOWED_HOSTS = ["*"]
if DEBUG:
    import socket

    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.0.1", "10.0.2.2"]

INTERNAL_IPS = [
    "127.0.0.1",
    "localhost",
]
