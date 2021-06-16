from setuptools import setup, find_packages
import re

readme = ''
with open('README.md') as f:
    readme = f.read()

version = ''
with open('cache/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)

if not version:
    raise RuntimeError('version is not set.')

setup(
    name='expiring-cache',
    author='ItsArtemiz',
    url='https://github.com/ItsArtemiz/expiring-cache',
    version=version,
    license='MIT',
    description='A simple Python dict with TTL support for auto-expiring caches with support for case-insensitive keys.',
    long_description=readme,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    python_requires='>3.7.0',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: MIT License',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Utilities'
    ]
)