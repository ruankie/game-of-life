![alt text](https://github.com/ruankie/game-of-life/raw/main/images/game-of-life.png "game-of-life")

# Description
This version of the Game of Life was created with the `pygame` library in `Python`. It is based on [A Plus Coding's YouTube video](https://www.youtube.com/watch?v=GKe1aGQlKDY&list=PLryDJVmh-ww1OZnkZkzlaewDrhHy2Rli2).

## Background
The Game of Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves. It is Turing complete and can simulate a universal constructor or any other Turing machine [[1]](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).

## Rules
The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live or dead. Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur [[1]](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life):

> 1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
> 2. Any live cell with two or three live neighbours lives on to the next generation.
> 3. Any live cell with more than three live neighbours dies, as if by overpopulation.
> 4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

These four simple rules govern the dynamics of the game. Although they are simple, they can lead to some quite complex and beautiful patterns.


# How to Install
1. Clone this repository.
2. Install pygame and other dependencies by running `pip install -r requirements.txt` from your terminal.
3. Run `python main.py` from your terminal to open Game of Life.

# How to Play
* Click to toggle between live and dead cells.
* Click the `RUN` button to run the game.
* Click the `PAUSE` button to pause the game.
* Click the `RESUME` button to resume the game after being paused.
* Click the `RESET` button to reset the game with randomised cells.


# References
> * [1] Wikipedia, *Conway's Game of Life*, https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
> * [2] A Plus Coding, *Conways Game of Life in python*, YouTube, https://www.youtube.com/watch?v=GKe1aGQlKDY&list=PLryDJVmh-ww1OZnkZkzlaewDrhHy2Rli2

***

*In honour of John Horton Conway who died of complications from COVID-19 on 11 April 2020 at age 82.*

***