from setuptools import setup

long_description = """
    Plot Neural Networks is a visualization python library inspired by [ANN Visualizer](https://github.com/Prodicode/ann-visualizer). This library is work with Keras model interface. It uses python's graphviz library to create a presentable graph of the neural network you are building.

    Usage:


from plotnn.visualize import model_visualize
#Build your model here
model_visualize(model, name="graph")



Documentation:
 model - The Keras Sequential model
 filename - Where to save the graph. (.gv file format)
"""

install_requires=[
    'networkx',
    'graphviz',
    'keras'
]

setup(
  name = 'plotnn',
  packages = ['plotnn'],
  version = '0.1',
  license="BSD",
  description = 'A python library for visualizing Neural Networks',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Romain Egele',
  author_email = 'romainegele@gmail.com',
  url = 'https://github.com/deephyper/plotnn',
  download_url = '',
  keywords = ['plotnn', 'ai', 'visualizer', 'learning', 'artificial', 'intelligence'],
  classifiers = [
    # How mature is this project? Common values are
    #   3 - Alpha
    #   4 - Beta
    #   5 - Production/Stable
    'Development Status :: 3 - Alpha',

    # Indicate who your project is intended for
    'Intended Audience :: Developers',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Topic :: Scientific/Engineering :: Visualization',

    # Pick your license as you wish (should match "license" above)
     'License :: OSI Approved :: BSD License',

    # Specify the Python versions you support here. In particular, ensure
    # that you indicate whether you support Python 2, Python 3 or both.
    'Programming Language :: Python :: 3.6',
    ],
    install_requires=install_requires,
)
