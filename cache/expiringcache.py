"""
MIT License

Copyright (c) 2021 Augadh Verma

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import time
from typing import Any, TypeVar

_KT = TypeVar('_KT')
_VT = TypeVar('_VT')

class ExpiringCache(dict):
    def __init__(self, seconds: int, *, case_insensitive: bool=False):
        """Makes a timed cache. Deletes cache after the time has expired.

        Returns the value as (value, time)

        Parameters
        ----------
        seconds : int
            The seconds to cache items for.
        case_insensitive : Optional[bool]
            Whether to use a case insensitive dict or not. By default `False`.
        """
        self.__ttl = seconds
        self.__case = case_insensitive
        super().__init__()

    def __verify_cache_integrity(self) -> None:
        current_time = time.monotonic()
        to_remove = [k for (k, (v,t)) in self.items() if current_time > (t + self.__ttl)]
        for k in to_remove:
            del self[k]

    def __check_case_sensitive(self, key: _KT) -> Any:
        if self.__case:
            if isinstance(key, str):
                return key.lower()
        return key

    def __contains__(self, key: _KT) -> bool:
        self.__verify_cache_integrity()
        key = self.__check_case_sensitive(key)
        return super().__contains__(key)

    def __getitem__(self, key: _KT) -> _VT:
        self.__verify_cache_integrity()
        key = self.__check_case_sensitive(key)
        return super().__getitem__(key)

    def __setitem__(self, k: _KT, v: _VT) -> None:
        k = self.__check_case_sensitive(k)
        return super().__setitem__(k, (v, time.monotonic()))