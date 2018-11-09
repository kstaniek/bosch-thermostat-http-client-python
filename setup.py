from setuptools import setup, find_packages


long_description = open('README.md').read()

setup(
    name='buderus-client-python',
    version='0.0.1',
    license='Apache License 2.0',
    url='https://github.com/moustic999/buderus-client-python',
    author='Ludovic Laurent',
    author_email='moustic999@msn.com',
    description='Python module to talk to Buderus KM200.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['buderus-client-python'],
    zip_safe=True,
    platforms='any',
    install_requires=list(val.strip() for val in open('requirements.txt')),
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)