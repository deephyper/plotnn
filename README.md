# Plotnn

## Description

Plot Neural Networks is a visualization python library inspired by [ANN Visualizer](https://github.com/Prodicode/ann-visualizer). This library is working with Keras model interface. It uses python's graphviz library to create a presentable graph of the neural network you are building. Working for sequential and non-sequential models.

For example if you have this keras model as input:

![example keras model](https://image.ibb.co/fxcPzf/graph-test.png)

You will have this visualisation:

![example visualisation](https://image.ibb.co/cWJxKf/visual.png)

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
