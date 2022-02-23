from setuptools import find_packages, setup


setup(
    name            = 'labyrinth',
    version         = '0.1.0',
    packages        = find_packages(),
    python_requires = '>=3.7',
    entry_points    = { 'console_scripts' : 
                            [ 'labyrinth = labyrinth.__main__:main',
                            ]
    }
)