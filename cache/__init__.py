"""
ExpiringCache
~~~~~~~~~~~~~

A simple Python dict with TTL support for auto-expiring caches with support for case-insensitive keys.

:copyright: (c) 2021 Augadh Verma
:license: MIT, check LICENSE for more information.

"""

__title__ = 'cache'
__author__ = 'Augadh Verma'
__license__ = 'MIT'
__copyright__ = 'Copyright 2021 Augadh Verma'
__version__ = '1.0.0'

__path__ = __import__('pkgutil').extend_path(__path__, __name__)

from collections import namedtuple

from .expiringcache import ExpiringCache

VersionInfo = namedtuple('VersionInfo', 'major minor micro releaselevel serial')
version_info = VersionInfo(major=1, minor=0, micro=0, releaselevel='final', serial=0)

__all__ = (
    '__title__',
    '__author__',
    '__license__',
    '__copyright__',
    '__version__',
    'ExpiringCache',
    'version_info'
)