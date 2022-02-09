#!/usr/bin/env python3.8

# Copyright (c) 2022, cemysce
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.

import datetime

day_offset = round((datetime.date.today() - datetime.date(2021, 6, 19)).total_seconds()/864e2)
print(day_offset)
# load word list as-is (i.e. unsorted) into valid_answers_unsorted, then:
#   solution = valid_answers_unsorted[day_offset % len(valid_answers_unsorted)]
