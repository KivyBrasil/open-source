from setuptools import setup

setup(
    name='kv',
    version='1.0.0',
    py_modules=['kv'],
    install_requires=['Click',],
    entry_points='''
        [console_scripts]
        kv=kv:main
    '''
)