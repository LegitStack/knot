# Knot

_a little wholeness_

Knot is an AGI research project. If Knot discovers the underlying algorithmic structure able to adapt itself to any environment it will have achieved it's goal aimed at by

The Contributors.


## Getting Started

The app runs in a docker image. The UI is a Flask web app.


### Deployment:

Option A. install knot on local machine:
```
cd <repositories>
git clone https://github.com/LegitStack/knot.git
cd knot
python setup.py develop
knot build
knot run
start http:\\localhost:5001 && start http:\\localhost:5000
knot start  # <--- inside jupyter at localhost:5001
```

Option B. don't install knot on local machine (just in docker):
```
cd <repositories>
git clone https://github.com/LegitStack/knot.git
cd knot
docker_build.bat
docker_run.bat
start http:\\localhost:5001 && start http:\\localhost:5000
knot start  # <--- inside jupyter at localhost:5001
```


### Getting Started Details

If you `python setup.py <install | develop>` you can build and run the docker image from the command line using `knot build` and `knot run`

If you do not install knot on your local machine you can build and run the docker image using the `docker_build` and `docker_run` files for windows (`.bat`) or linux (`.sh`).

Once the docker file is running open a browser to [localhost:5001](localhost:5001) to see a jupyter lab terminal into the docker container.

From the jupyter lab terminal you can run `knot start` to start the application. The application will be available at [localhost:5000](localhost:5000)



### Requirements

  - docker


## Background

This project makes two assumptions:

1. A generally intelligent mind can be made up of a repeating substructure.
2. That smallest unit can be discovered using current day ML and AI technologies.

That repeating substructure could be considered the smallest unit of intelligence, a microcosm of the entire structure of the intelligent mind, possessing each major impetus or faculty the generally intelligent mind possess.

This 'smallest unit of intelligence' is referred to in this project as a 'knot'.

### Evidence for

There is much evidence for a structure like this in biology. The cortex in mammals has a repeating circuit of neurons varied throughout the cortex mainly by the type of data that each region is exposed to. This adaptive substructure, repeated throughout the entire cortex seems to be the reason mammals have higher orders of general intelligence.

This underlying assumption does not presuppose this is the only way to build generally intelligent memory structures, but given this patterns ubiquity in nature, and even in engineered systems, it seems a natural place to start - that is, a natural way to confine the search space of intelligent mechanisms.

## Methodology

Here we attempt to generate environments in which to place generated agents who are tested for general fitness. Aspects of the memory structures that learn to manage the broadest range of environments well are then allowed to propagate.

In short, we have constrained the search space, generated a framework by which we can generate and evaluate agents, and implemented a genetic algorithm.

### Search Space Constriction
_(under Constriction)_

1. discuss what we know about the shape of the knot
2. ...

### Framework
_(under Constriction)_

1. Agents are treated as generic input-output black boxes, in a perpetual feedback loop with the environment.
2. Goal setting and evaluation.
3. Genetic Algorithm.


### Environments

At present, each environment in Knot's benchmark suite is fully observable. The agent essentially moves through the state space of the fully observable environment's configurations.

Environments are semantically encoded. And even their behaviors are semantically encoded. This is done for fidelity purposes. We're not in the business of building automatically generated semantics, we're in the business of building general intelligence off those semantics.

In this way we compare apples to apples, as the generally intelligent brain sits inside a body that, through the course of evolution, has learned to semantically encode incoming data into the brain through it's various sensing organs such that it is already in a format the brain can more easily comprehend.

#### Semantic Encoding

Semantically encoded data means that similar representations of input (and output) data are similar in their meaning (or effects).

Take, as an anti-example, the word 'screen.' Screen can mean to hide something, or it can mean to show a film. These are almost opposite meanings, but the same representation. Only within a larger context can one know what is meant to be conveyed. Semantically encoded inputs mean similar things if the representations look similar. For example, 'similar' has a similar representation to the word 'simile' and their meanings are similar as well.

#### Environment Requirements

Environments, therefore, have 2 major constraints:

1. It must be fully observable. (This means, also, that the agent is the only agent perturbing the environment).
2. It must be at least partially semantically encoded; both in it's state representations and it's available transitions (agent behaviors).

Once generally intelligent agents are developed with these constraints, (aimed at drastically reducing the required complexity of their mind's substructure), they can be lifted and training continued to develop the knot further.

---

##### inspired by:

Inspired by https://discourse.numenta.org/t/ml-and-deep-learning-to-automatically-create-agi/6501/5, knot is an attempt to deduce the repeating structure (or network) of a distributed, generally intelligent, naturally learning memory structure and it's associated algorithm by constraining the search space of what that structure must look like as best we can then searching that space with machine learning or specialized AI algorithms.
