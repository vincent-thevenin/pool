<h1 align="center"> Pool </h1>
<p align="center">
    <a href="https://codeclimate.com/github/max-kov/pool">
        <img src="https://codeclimate.com/github/max-kov/pool/badges/gpa.svg"
             alt="CodeClimate">
    <a href="https://travis-ci.org/max-kov/pool">
        <img src="https://travis-ci.org/max-kov/pool.svg?branch=table_rework"
             alt="build status">
    </a>
</p>

<p align="center"><b> A pool game written entirely in python! </b></p>


![Alt text](/../screenshots/screen_recording_2.gif?raw=true "Game gif")


## Installing

Firstly, clone the github code. Run

```
git clone https://github.com/max-kov/pool
cd pool
```

in the linux terminal. To install the requirements with pip run

```
sudo pip install -r requirements.txt
```

You can now start the program using `python main.py`

## Running the tests

To run the tests we will require `pytest` module. To install it simply run

```
pip install pytest
```

To run the tests write `pytest` in the game folder. Pytest will recursively search for test files (which are initially located in tests folder).
You can also check test coverage by installing `pip install pytest-coverage` and executing
`pytest --cov=.` in the pool folder. That will analyse which files and which lines of code are being tested by the tests.
`.coveragerc` will prevent the module from analysing test files as well.

## Built With

* [Pygame](http://www.pygame.org/) - 2d graphics library
* [Numpy](http://www.numpy.org/) - Scientific computing library, used here for vector opertations
* [Travis CI](https://travis-ci.org/) and [CodeClimate](https://codeclimate.com/) - Testing and code analysis