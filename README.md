# wordle-basic

Quick and dirty [Wordle](https://www.powerlanguage.co.uk/wordle/) clones.

Credit for the game's name, gameplay logic, and visual design belongs to [Josh Wardle](https://www.powerlanguage.co.uk/).
The programs here were merely fun exercises for me, and may be useful to others.

The only bit of logic that was replicated from upstream Wordle's JavaScript code is the logic for computing the daily game number and its solution.
Everything else was written from scratch by me to replicate the gameplay logic as I understood it from playing the game.

* `basic/`
  * `wordle-basic.py` &ndash; My initial implementation, including hard mode support, in 39 lines of Python.
    * _The word lists in the code are blank and must be manually filled in however you want, or taken from the upstream game's code._
    * Optional arguments:
      * `hard` for hard mode
* `more-features/`
  * `wordle-bw.py` &ndash; A more featureful implementation, including downloading and analyzing upstream Wordle's word lists.
    * Optional arguments:
      * `hard` for hard mode
      * `fetch` to download Wordle's valid answers and valid guesses word lists
      * `stats` performs some very rudimentary analysis on words in valid answers list
  * `wordle-color.py` &ndash; Minor variation on `wordle-bw.py`, adding support for all 4 of upstream Wordle's color schemes.
    * _A couple of parameters must be edited in the code to switch between the color schemes (dark mode, high contrast mode)._
    * The idea for this came from [here](https://gist.github.com/huytd/6a1a6a7b34a0d0abcac00b47e3d01513),
      but I quickly realized I wanted to make a full-fledged replica instead.
  * `decode-solution.py` &ndash; A replication in Python of the logic Wordle uses to determine the daily game number and solution.
    * _This is only for reference. The program doesn't do anything useful on its own._
