#!/usr/bin/env python3

# Copyright (c) 2022, cemysce
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

import itertools
import json
import random
import re
import requests
import sys

from collections import Counter

WORDLE_LISTS_FILE = 'wordle_lists.json'
WORD_LENGTH = 5
TOTAL_GUESSES_ALLOWED = 6

def usage():
    return (f'Usage: {sys.argv[0]} [fetch|stats|hard]\n'
             '\n'
            f'  fetch         Fetch word lists to "{WORDLE_LISTS_FILE}".\n'
             '  stats         Print stats about words in answer list.\n'
             '  hard          Play in hard mode.\n'
             '  (no args)     Play in normal mode.')

def fetch():
    def get_text_or_abort(url):
        rs = requests.get(url)
        if not rs.ok:
            return f'Failed to get URL "{url}", with status {rs.status_code}!'
        return rs.text

    URL = 'https://www.powerlanguage.co.uk/wordle'

    html = get_text_or_abort(URL)
    matches = re.findall(r'<script src="(main\.[0-9a-f]+\.js)">', html)
    if len(matches) != 1:
        return f'Failed to determine URL for JavaScript source!'

    js = get_text_or_abort(f'{URL}/{matches[0]}')
    word_lists = [sorted(word.strip('"') for word in word_list.split(','))
                  for word_list in re.findall(r'=\[("[a-z]{'+str(WORD_LENGTH)+'}"(?:,"[a-z]{'+str(WORD_LENGTH)+'}")*)\]', js)]
    if len(word_lists) != 2:
        return f'Failed to locate word lists within JavaScript source!'
    if len(word_lists[0]) < len(word_lists[1]):
        valid_answers = word_lists[0]
        also_valid_guesses = word_lists[1]
    elif len(word_lists[0]) > len(word_lists[1]):
        valid_answers = word_lists[1]
        also_valid_guesses = word_lists[0]
    else:
        return f'Both word lists are same size, cannot tell them apart!'
    with open(WORDLE_LISTS_FILE, 'w') as f:
        json.dump({'valid_answers': valid_answers, 'also_valid_guesses': also_valid_guesses}, f)

def stats():
    with open(WORDLE_LISTS_FILE) as f:
        word_lists = json.load(f)
    VALID_ANSWERS = word_lists['valid_answers']
    overall_total_num_letters = len(VALID_ANSWERS) * WORD_LENGTH
    overall_letter_count_print_width = len(str(overall_total_num_letters))
    print(f'Overall Stats:')
    for letter_count in Counter(itertools.chain(*VALID_ANSWERS)).most_common():
        print(f'{letter_count[1]:{overall_letter_count_print_width}}/{overall_total_num_letters} {letter_count[0]}')
    per_letter_total_num_letters = len(VALID_ANSWERS)
    per_letter_count_print_width = len(str(len(VALID_ANSWERS)))
    for i in range(WORD_LENGTH):
        print(f'\nLetter {i+1} Stats:')
        for letter_count in Counter(a[i] for a in VALID_ANSWERS).most_common():
            print(f'{letter_count[1]:{per_letter_count_print_width}}/{per_letter_total_num_letters} {letter_count[0]}')

def play(hard_mode=False):
    with open(WORDLE_LISTS_FILE) as f:
        word_lists = json.load(f)
    VALID_ANSWERS = word_lists['valid_answers']
    VALID_GUESSES = set(VALID_ANSWERS) | set(word_lists['also_valid_guesses'])

    print(f'WORDLE{": Hard Mode" if hard_mode else ""}')
    num_guesses_left = TOTAL_GUESSES_ALLOWED
    answer = random.choice(VALID_ANSWERS)
    correct_letters = [None]*len(answer)
    misplaced_letters = []
    while num_guesses_left > 0:
        print(f'\n{num_guesses_left} guess(es) left')
        guess = input('Guess: ').lower()
        if guess == answer:
            print('Correct!')
            return
        if guess in VALID_GUESSES:
            if hard_mode and (   any(guess.count(m) < misplaced_letters.count(m) for m in misplaced_letters)
                              or any(guess[i] != c for i,c in enumerate(correct_letters) if c)):
                print('In hard mode, guesses must contain all misplaced letters and correct letters\n'
                      '(in correct positions) from previous guess.')
                continue
            print('Wrong!')
            correct_letters = [(guess[i] if guess[i] == answer[i] else None) for i in range(len(guess))]
            misplaced_letters.clear()
            for i in range(len(guess)):
                if guess[i] == answer[i]:
                    s = f' {guess[i].upper()} '
                elif answer.count(guess[i]) > misplaced_letters.count(guess[i]) + correct_letters.count(guess[i]):
                    s = f'({guess[i].upper()})'
                    misplaced_letters.append(guess[i])
                else:
                    s = ' _ '
                print(f' {s}', end='')
            print()
            num_guesses_left -= 1
            continue
        print('Invalid word, try again.')
    print()
    return f'Out of guesses! It was "{answer}".'

if len(sys.argv) > 2:
    sys.exit(usage())
if len(sys.argv) == 2:
    mode = sys.argv[1]
    if mode == 'fetch':
        sys.exit(fetch())
    if mode == 'stats':
        sys.exit(stats())
    if mode == 'hard':
        sys.exit(play(True))
    sys.exit(usage())
sys.exit(play())
