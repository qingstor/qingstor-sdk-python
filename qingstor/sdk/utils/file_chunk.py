import os

from math import ceil

from ..constant import PART_SIZE, SEGMENT_SIZE

# Only support read for now
HOOKS = ["read"]


class FileChunk:

    def __init__(self, fd, part_size=PART_SIZE, hooks=None):
        self.fd = fd
        self.part_size = part_size

        # Check if this file object is seekable
        self.seekable = True
        try:
            self.fd.seek(0)
        except IOError:
            self.seekable = False

        # Cal segments
        self.segments = int(ceil(self.part_size * 1.0 / SEGMENT_SIZE))

        # Handle hooks
        self.hooks = {}
        self.register_hook(hooks)

    @property
    def size(self):
        self.seek(0, os.SEEK_END)
        size = self.fd.tell()
        self.seek(0, os.SEEK_SET)
        return size

    @property
    def parts(self):
        return int(ceil(self.size * 1.0 / self.part_size))

    def register_hook(self, hooks):
        if isinstance(hooks, dict):
            for event in HOOKS:
                self.hooks[event] = []
                callbacks = hooks.get(event, [])
                for callback_function in callbacks:
                    if callable(callback_function):
                        self.hooks[event].append(callback_function)
                    else:
                        raise Exception(
                            "%s is not callable" % callback_function
                        )

    def seek(self, offset, whence=os.SEEK_SET):
        if not self.seekable:
            raise Exception("This file is not seekable")
        self.fd.seek(offset * self.part_size, whence)

    def read(self):
        for (event, callbacks) in self.hooks.items():
            for callback_function in callbacks:
                callback_function()
        return self.fd.read(SEGMENT_SIZE)

    def read_part(self):
        cache = []
        for i in range(self.segments):
            cur = self.read()
            if cur == b"":
                break
            cache.append(cur)
        return b"".join(cache)

    def next(self):
        data = self.read_part()
        if data == b"":
            raise StopIteration
        return data

    def __next__(self):
        return self.next()

    def __iter__(self):
        return self
