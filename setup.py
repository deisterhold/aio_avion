from setuptools import setup, find_packages

setup(
    name='aio_avion',
    version='0.0.1',
    license='MIT',
    url='https://github.com/deisterhold/aioavion',
    author='Daniel Eisterhold',
    author_email='deisterhold@gmial.com',
    description='Python module to control Avi-on lights through the Wi-Fi bridge.',
    packages=find_packages(),
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