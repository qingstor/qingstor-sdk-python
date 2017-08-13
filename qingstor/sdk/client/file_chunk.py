import os

from ..constant import SEGMENT_SIZE

class FileChunk(object):

    def __init__(self,fd,part_size,callback):
        self.fd=fd
        self.part_size=part_size
        self.callback=callback

    def __iter__(self):
        return self

    def next(self):
        cur_part=[]
        for i in range(SEGMENT_SIZE,self.part_size,SEGMENT_SIZE):
            cur_segment=self.fd.read(SEGMENT_SIZE)
            if cur_segment==b"":
                break
            cur_part.append(cur_segment)
            self.callback()
        if cur_part==[]:
            raise StopIteration
        return b"".join(cur_part)

    def __next__(self):
        self.next()
