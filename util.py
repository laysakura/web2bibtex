# -*- coding: utf-8 -*-

def coroutine(func):
    """コルーチンの要素をラップするデコレータ．最初にnext()しないで良いようになる．

    http://www.dabeaz.com/coroutines/Coroutines.pdf からほぼ引用

    Usage:
    @consumer
    def hoge():
        ...
        foo = yield
    """
    def _wrapper(*args,**kw):
        cr = func(*args, **kw)
        next(cr)
        return cr
    _wrapper.__name__ = func.__name__
    _wrapper.__dict__ = func.__dict__
    _wrapper.__doc__  = func.__doc__
    return _wrapper
