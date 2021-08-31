#!/usr/bin/env python
# coding=utf-8

import inkex

from inkex.elements import TextElement

class Greet(inkex.GenerateExtension):

    def generate(self):
        textElement = TextElement()
        textElement.text = 'Hello World'
        return textElement

if __name__ == '__main__':
    Greet().run()
