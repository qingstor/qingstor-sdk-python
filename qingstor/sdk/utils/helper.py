from __future__ import unicode_literals

from time import strftime, gmtime

from ..compat import is_python2, is_python3, quote


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


def should_quote(key):
    keys_map = [
        "date", "user-agent", "content-md5", "content-type",
        "x-qs-encryption-customer-key", "x-qs-encryption-customer-key-md5",
        "x-qs-copy-source-encryption-customer-key",
        "x-qs-copy-source-encryption-customer-key-md5"
    ]
    return key not in keys_map
