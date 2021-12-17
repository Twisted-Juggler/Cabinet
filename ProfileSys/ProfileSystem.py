import os

# -- Profile System -- #

""" The profile system saves the last written path
to be reused. It works by writing to a text
file (Profile.txt) and uses the written path until
changed. When a different path is used, it
rewrites the file, this way it uses the most
recent one used."""


def write_profiles(origin, destination):
    cwd = os.path.dirname(os.path.realpath(__file__))
    file = open(cwd + "\\Profile.txt", 'w+')
    file.write(origin + ',')
    file.write(destination)


class Profiles:
    def __init__(self):
        cwd = os.path.dirname(os.path.realpath(__file__))
        file = open(cwd + "\\Profile.txt", 'r')
        self.content = file.read().split(',')
