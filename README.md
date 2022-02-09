# wordle-basic

Quick and dirty Wordle clones.

* `basic/`
  * `wordle-basic.py` &ndash; My initial implementation, including hard mode support (run with `hard` as argument), in 39 lines of Python.
    * _The word lists in the code are blank and must be manually filled in however you want, or taken from the upstream game's code._
* `more-features/`
  * `wordle-bw.py` &ndash; A more featureful implementation (`fetch` argument downloads upstream Wordle's word list, `stats` performs some very rudimentary analysis on the words).
  * `wordle-color.py` &ndash; Minor variation on `wordle-bw.py` that adds color support (all 4 of upstream Wordle's color schemes supported, but must toggle in code).
  * `decode-solution.py` &ndash; A replication in Python of the logic Wordle uses to determine the daily game number and solution.
    * _This is only for reference. The program doesn't do anything useful on its own._
