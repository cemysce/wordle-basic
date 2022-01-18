#!/usr/bin/env python3

# Copyright (c) 2022, cemysce
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

import random
import sys

VALID_ANSWERS = [] # fill this in from JS code
VALID_GUESSES = set(VALID_ANSWERS) | {} # fill this in from JS code
TOTAL_GUESSES = 6

hard_mode = (len(sys.argv) >= 2 and sys.argv[1] == 'hard')
print(f'WORDLE{": Hard Mode" if hard_mode else ""}')
num_guesses_left = TOTAL_GUESSES
answer = random.choice(VALID_ANSWERS)
correct_chars = [None]*len(answer)
misplaced_chars = []
while num_guesses_left > 0:
    print(f'\n{num_guesses_left} guess(es) left')
    guess = input('Guess: ').lower()
    if guess == answer:
        print('Correct!')
        break
    if guess in VALID_GUESSES:
        if hard_mode and (   any(guess.count(m) < misplaced_chars.count(m) for m in misplaced_chars)
                          or any(guess[i] != c for i,c in enumerate(correct_chars) if c)):
            print('In hard mode, guesses must contain all misplaced characters and correct\n'
                  'characters (in correct positions) from previous guess.')
            continue
        print('Wrong!')
        correct_chars = [(guess[i] if guess[i] == answer[i] else None) for i in range(len(guess))]
        misplaced_chars.clear()
        for i in range(len(guess)):
            if guess[i] == answer[i]:
                s = f' {guess[i].upper()} '
            elif answer.count(guess[i]) > correct_chars.count(guess[i]):
                s = f'({guess[i].upper()})'
                misplaced_chars.append(guess[i])
            else:
                s = ' _ '
            print(f' {s}', end='')
        print()
        num_guesses_left -= 1
        continue
    print('Invalid word, try again.')
