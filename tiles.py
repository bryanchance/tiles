# Copyright (c) 2017 Martin Sustrik  All rights reserved.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"),
# to deal in the Software without restriction, including without limitation
# the rights to use, copy, modify, merge, publish, distribute, sublicense,
# and/or sell copies of the Software, and to permit persons to whom
# the Software is furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL
# THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from inspect import currentframe
from itertools import dropwhile

def __trim(t):
    lns = [ln.rstrip() for ln in t.split("\n")]
    lns = [ln for ln in dropwhile(lambda ln: len(ln) == 0, lns)]
    lns = [ln for ln in dropwhile(lambda ln: len(ln) == 0, reversed(lns))]
    lns = filter(bool, lns)
    left = 0 if not lns else \
           min([len(ln) - len(ln.lstrip()) for ln in lns])
    return [ln[left:] for ln in reversed(lns)]

def __append(t1, t2):
    t1 += [""] * (len(t2) - len(t1))
    w = max([len(s) for s in t1 or [""]])
    for i in range(len(t2)):
        t1[i] = t1[i].ljust(w) + t2[i]

def tile(s):
    lns = s.split("\n")
    res = []
    for ln in lns:
        curr = []; end = 0
        while True:
            start = ln.find("@{", end)
            __append(curr, [ln[end : (len(ln) if start == -1 else start)]])
            if start == -1:
                break
            end = ln.find("}", start) + 1
            if end == 0:
                raise Exception("unifinished @{} expression")
            __append(curr, __trim(str(eval(ln[start + 2 : end - 1],
                currentframe().f_back.f_globals,
                currentframe().f_back.f_locals))))
        res += curr
    return "\n".join(res)

