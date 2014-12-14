# -*- coding: utf-8 -*-
import math
from random import choice, random, randrange

class TweetGenerator(object):
    TWEET_MAX_LENGTH = 140

    def generate_tweet(self):
        pass

    def set_tweet_dimensions(self, height=None, width=None, length=TWEET_MAX_LENGTH):
        size = {}
        if height:
            width = int(math.floor(length / height))
            width_with_newline = width + 1
            length = int(width_with_newline * height)
            size = {length: length, width: width, height: height}
        elif width:
            width_with_newline = width + 1
            height = int(math.floor(length / width_with_newline))
            length = int(width * height)

        size = {'length': length, 'width': width, 'height': height}

        return size


class WinterscapeGenerator(TweetGenerator):
    ground_chars = {
        'dtrees':   [20,['▲']],
        'trees':    [10, ['∆','ᗗ','ᗑ','⧋']],
        'houses':   [3, ['⌂','☖','☗']],
        'ground':   [0, ['_']],
        'snowman':  [0, ['☃']],
        'sad_people':   [1, ['☹']],
        'animals':  [2, ['♘','♞']]
        }
    sky_chars = {
        'space':    [0, ['　']],
        'snow':     [5, ['❅', '❆','❉','❋','✺','☸','✺']],
        'flecks':   [30,['⋄','‧','༚']],
        'stars':    [2, ['✧','✦','☄']]
    }

    def create_sky_row(self, length, row_num):
        row = []
        non_space_sky_chars = []

        # get all sky chars
        for char_cat in self.sky_chars.keys():
            non_space_sky_chars  += (self.sky_chars[char_cat][0] * self.sky_chars[char_cat][1])

        for index in range(length):
            # stagger space placement for each row
            if index % 2 == (row_num % 2):
                # roll dice for blank
                dice = random()

                if dice < .4:
                    char = choice(non_space_sky_chars)
                    row.append(char)
                else:
                    char = choice(self.sky_chars['space'][1])
                    row.append(char)
            else:
                char = choice(self.sky_chars['space'][1])
                row.append(char)

        return row


    def create_ground_row(self, length):
        # hack for now - increase size of ground
        length = length + 10

        row = []
        non_ground_ground_chars = []

        # get all ground chars
        for char_cat in self.ground_chars.keys():
            non_ground_ground_chars += (self.ground_chars[char_cat][0] * self.ground_chars[char_cat][1])

        for index in range(length):
            if index % 2 == 0:

                # roll dice for blank
                dice = random()

                if dice < .4:
                    char = choice(non_ground_ground_chars)
                    row.append(char)
                else:
                    char = choice(self.ground_chars['ground'][1])
                    row.append(char)
            else:
                char = choice(self.ground_chars['ground'][1])
                row.append(char)

        # randomly insert snowman at an even index
        start = 0
        end = length - 1
        rand_index = randrange(start, end, 2)
        row[rand_index] = choice(self.ground_chars['snowman'][1])

        return row


    def flatten_tweet(self, tweet_array):
        tweet_string = '\n'.join([''.join(row) for row in tweet_array])

        return tweet_string


    def generate_tweet(self):
        dim = self.set_tweet_dimensions(width=20)
        row_length = dim['width']

        scape = []

        for row_num in range(dim['height'] - 1):
            row = self.create_sky_row(length=row_length, row_num=row_num)
            scape.append(row)

        scape.append(self.create_ground_row(length=row_length))

        tweet_text = self.flatten_tweet(scape)

        print tweet_text
        return tweet_text
