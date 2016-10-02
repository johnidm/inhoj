import setuptools
from inhoj.version import Version


setuptools.setup(name='inhoj',
                 version=Version('1.0.0').number,
                 description='Useful Python Code Snippets',
                 long_description=open('README.md').read().strip(),
                 author='Johni Douglas Marangon',
                 author_email='johni.douglas.marangon@gmail.com',
                 url='https://github.com/johnidm/inhoj',
                 py_modules=[],
                 install_requires=[],
                 license='MIT License',
                 zip_safe=False,
                 keywords=' ',
                 classifiers=['Packages'])
