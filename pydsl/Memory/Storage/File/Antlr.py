#!/usr/bin/python
# -*- coding: utf-8 -*-
#This file is part of pydsl.
#
#pydsl is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.
#
#pydsl is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.
#
#You should have received a copy of the GNU General Public License
#along with pydsl.  If not, see <http://www.gnu.org/licenses/>.


"""ANLTr grammar format functions"""

__author__ = "Nestor Arocha Rodriguez"
__copyright__ = "Copyright 2008-2012, Nestor Arocha Rodriguez"
__email__ = "nesaro@gmail.com"

import logging
LOG = logging.getLogger(__name__)

#manual lexer

reservedwords = ["grammar","options","language","output","ASTLabelType",":",";","|","*"]

comments = ["/**/"]

class ANLTRGrammarLexer(Lexer):
    def comma(self):
        current = self.current
        self.match(",")
        return ("COMMA", current)

    def colon(self):
        current = self.current
        self.match(":")
        return ("COLON", current)

    def vbar(self):
        current = self.current
        self.match("|")
        return ("VBAR", current)


#manual parser
#convert to instance
