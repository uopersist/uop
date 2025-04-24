import asyncio
from functools import reduce
import inspect

async def ca(fn, *args, **kwargs):
    if inspect.iscoroutinefunction(fn):
        return await fn(*args, **kwargs)
    else:
        return fn(*args, **kwargs)

class SimpleToggle:
    def __init__(self, val=False):
        self._is_set = bool(val)

    def toggle(self):
        self._is_set = not self._is_set

    @property
    def is_set(self):
        return self._is_set


class short_circuit():
    def __init__(self, fn, fail_test, failed_value):
        self.fn = fn
        self._failed = False
        self.test_fn = fail_test
        self.fail_val = failed_value

    async def __call__(self, val):
        res = await self.fn(val)
        if self.test_fn(res):
            return self.fail_val
        return res


async def a_set_and(fn, vals):
    if vals:
        res = await fn(vals[0])
        for v in vals[1:]:
            if not res:
                return set()
            next = await fn(v)
            res = res & next
        return res
    return set()

def set_and(fn, vals):
    if vals:
        res = fn(vals[0])
        for v in vals[1:]:
            if not res:
                return set()
            next = fn(v)
            res = res & next
        return res
    return set()


async def a_set_or(fn, values):
    sets = await asyncio.gather(*[fn(v) for v in values])
    return reduce(lambda a, b: a | set(b), sets, set())

def set_or(fn, values):
    sets = [fn(v) for v in values]
    return reduce(lambda a, b: a | set(b), sets, set())
