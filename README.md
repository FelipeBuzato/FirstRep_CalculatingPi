# Calculating Pi

This is a Python code that calculates an approximation for the value of pi using Monte-Carlo method.

To read about Monte-Carlo method, access [Wikipedia](https://en.wikipedia.org/wiki/Monte_Carlo_method).

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the libraries _numpy_ and _stats_.

```bash
pip install numpy
pip install stats
```

## Approximation

Here we'll be using the function ```probability_distribution``` from _stats_ to generate _n_ tuples _(x,y)_ that will represent points in the cartesian plan s.t.  0<x<1 and 0<y<1.

Monte-Carlo method tells us that if we generate a very large number of random points, the proportion of points that fall into the area delimited by the circumference will be a good approximation for the ratio between the area of the circle (_R=1_) and the area of the square (_l=2_).


## Usage

After cloning this repository to your local machine and installing the apropriate libraries, run the code ```code.ipynb```

If you want to change the value of _N_, just alter it in the cell bellow and run the code.

```bash
# number of random points 
N = 1000
```

