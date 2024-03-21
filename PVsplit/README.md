# PVSplit

This repository contains the implementation of `PVSplit`, a tool used to analyse galaxy dynamics.

## Requirements

To install all of the tools you would need to run this program on your machine, ensure that you are using version
3.x of Python and run:

```sh
make install
```

## Usage

If you wish to run the program locally on your Operating System, ensure that you
change the path in `main.py` and execute the file using while in the **pvsplit** directory:

```sh
python3 main.py
```

If you wish to run the program using a Docker container, build the docker image using the Dockerfile
by running:

```sh
docker build .
```

An example of the structure of the output directory is also provided for reference in the repository under **example_directory**.