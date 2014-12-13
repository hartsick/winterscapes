# -*- coding: utf-8 -*-

class TweetGenerator(object):
    def generate_tweet(self):
        pass

class WinterscapeGenerator(TweetGenerator):
    tweet_length = 140
    space = ' '
    snowman = '☃'
    ground = '_'
    trees = ['†','∆','ᗗ','ᗑ','ᗋ','†','⋀','▲','△','◭','◮','◬','◢','◣','⧋']
    houses = ['⌂','☖','☗']
    snowflakes = ['❄','❅', '❆', '⚹', '✵', '❉', '❋', '✺', '✹','✸','✳','✲','✱','⁂','☸','☀','✳','✱','✺']
    stars = ['⋄','✶','✷','✵','✴','✧','✦','⁕','༝','༚', '༶','•','‧','‸','⁂','☄','★','☆','✡','✯','✮','✰']
    people = ['☺','☻','☹','⚇','⚆','⚈','⚉']
    animals = ['♘','♞']

    def _set_size(self, rows=None,cols=None):
        pass

    def generate_tweet(self):
        return self.animals
