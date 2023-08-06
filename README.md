# Hopcroft-Karp algorithm implementation

This is the repository containing the implementation of Hopcroft-Karp algorithm for bipartite graph and also an implementation for Naive algorithm for maximum matching

## Installation
Clone the repository
```bash
git clone https://github.com/nguyenbanhducA1K51/Hopcroft-Karp-implementation.git
```
cd to the directory and use the package manager [pip](https://pip.pypa.io/en/stable/) to install libary and package in file requirements.txt (recommend install in conda environment).

```bash
pip install -r requirements.txt
```

## Usage

This implementation simplify the bipartite graph by using the sequence 0->n-1 to represent n vertices of the graph. I also add a variable A which 0->A-1 represet one side, and A to n-1 for other side.More details can be find at file utils.py. To run this algorithm type command 
```bash
python3 hopcroft.py
```
The graph will be generated at file ./visualize/graph.png, and the matching is generated at file ./visualize/matching.png


