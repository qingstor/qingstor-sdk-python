from __future__ import unicode_literals

import hashlib

from time import strftime, gmtime

from ..compat import is_python2, is_python3, quote, unquote, urlparse, urlunparse


def current_time():
    time_format = "%a, %d %b %Y %H:%M:%S GMT"
    if is_python2:
        time_format = time_format.encode("utf-8")
    return strftime(time_format, gmtime())


def uni_quote(o):
    if is_python2:
        return quote(unicode(o).encode("utf-8"))
    elif is_python3:
        return quote(str(o))


def url_quote(o):
    scheme, netloc, path, params, query, fragment = urlparse(
        o, allow_fragments=False
    )
    path = quote(unquote(path))
    o = urlunparse((scheme, netloc, path, params, query, fragment))
    return o


def should_url_quote(key):
    should_url_quote_list = ["x-qs-fetch-source"]
    return key in should_url_quote_list


def should_quote(key):
    should_quote_list = ["x-qs-copy-source", "x-qs-move-source"]
    return key in should_quote_list


def md5_digest(input_str):
    m = hashlib.md5()
    m.update(input_str)
    return m.digest()
