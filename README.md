# expiring-cache
A simple Python dict with TTL support for auto-expiring caches with support for case-insensitive keys.

## Installation

```python
pip install expiring-cache
```

## Features

- TTL support for auto-caching
- Case-insensitive keys support

## Usage

Example 1:

```python
import time
from cache import ExpiringCache

cache = ExpiringCache(2) # Keys will exist for 2 seconds.

cache['ABC'] = 'Example value'
print(cache['ABC']) # Prints the 'Example Value'
time.sleep(2)
print(cache['ABC']) # Raises KeyError
```

Example 2: (shows case-insensitive feature)

```python
import time
from cache import ExpiringCache

cache = ExpiringCache(2)

cache['ABC'] = 'Example value'
print(cache['ABC'])
print(cache['abc'])
# Both print statements above print the exact same 'Example Value'

time.sleep(2)
print(cache['ABC'])
print(cache['abc'])
# Both the print statements above raise KeyError
```