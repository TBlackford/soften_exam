from setuptools import setup, find_packages

setup(
    name='flaskr',
    packages=find_packages(),
    include_package_data=True,
    entry_points='''
        [flask.commands]
        initdb=flaskr.flaskr:initdb_command
    ''',
    install_requires=[
        'flask',
    ],
    setup_requires=[
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
    ],
)