# Plotnn

## Description

Plot Neural Networks is a visualization python library inspired by [ANN Visualizer](https://github.com/Prodicode/ann-visualizer). This library is work with Keras model interface. It uses python's graphviz library to create a presentable graph of the neural network you are building.

## Install

```
pip install -e plotnn/
```

## Usage

```
from plotnn.visualize import model_visualize
#Build your model here
model_visualize(model, name="graph")
```
