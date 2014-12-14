# -*- coding: utf-8 -*-
import math
from random import choice, random

class TweetGenerator(object):
    TWEET_MAX_LENGTH = 140

    def generate_tweet(self):
        pass

    def set_tweet_dimensions(self, height=None, width=None, length=TWEET_MAX_LENGTH):
        size = {}
        if height:
            width = int(math.floor(length / height))
            length = int(width * height)
            size = {length: length, width: width, height: height}
        elif width:
            height = int(math.floor(length / width))
            length = int(width * height)

        size = {'length': length, 'width': width, 'height': height}

        return size


class WinterscapeGenerator(TweetGenerator):
    ground_chars = {
        'trees':    [4, ['∆','ᗗ','ᗑ','ᗋ','†','⋀','▲','△','◭','◮','◬','⧋']],
        'houses':   [3, ['⌂','☖','☗']],
        'ground':   [0, ['_']],
        'snowman':  [12, ['☃']],
        'happy_people': [2, ['☻','⚇','⚆','⚈','⚉']],
        'sad_people':   [1, ['☹']],
        'animals':  [8, ['♘','♞']]
        }
    sky_chars = {
        'space':    [0, [' ']],
        'snow':     [1, ['❅', '❆','❉','❋','✺','✹','✲','✱','☸','✺']],
        'flecks':   [5, ['⋄','‧']],
        'stars':    [2, ['✶','✷','✵','✴','✧','✦','⁕','༝','༚','•','‸','☄','☆','✮','✰','✸']]
    }

    def create_sky_row(self, length):
        row = []
        non_space_sky_chars = []

        # get all sky chars
        for char_cat in self.sky_chars.keys():
            non_space_sky_chars  += (self.sky_chars[char_cat][0] * self.sky_chars[char_cat][1])

        for index in range(length):
            # roll dice for blank
            dice = random()

            if dice < .92:
                char = choice(self.sky_chars['space'][1])
                row.append(char)
            else:
                char = choice(non_space_sky_chars)
                row.append(char)

        return row


    def create_ground_row(self, length):
        row = []
        non_ground_ground_chars = []

        # get all ground chars
        for char_cat in self.ground_chars.keys():
            non_ground_ground_chars += (self.ground_chars[char_cat][0] * self.ground_chars[char_cat][1])

        for index in range(length):

            # roll dice for blank
            dice = random()

            if dice < .83:
                char = choice(self.ground_chars['ground'][1])
                row.append(char)
            else:
                char = choice(non_ground_ground_chars)
                row.append(char)

        return row


    def flatten_tweet(self, tweet_array):
        tweet_string = '\n'.join([''.join(row) for row in tweet_array])

        return tweet_string


    def generate_tweet(self):
        dim = self.set_tweet_dimensions(width=25)
        row_length = dim['width']

        scape = []

        for sky_line in range(dim['height'] - 1):
            row = self.create_sky_row(length=row_length)
            scape.append(row)

        scape.append(self.create_ground_row(length=row_length))

        tweet_text = self.flatten_tweet(scape)

        print tweet_text
        return tweet_text
