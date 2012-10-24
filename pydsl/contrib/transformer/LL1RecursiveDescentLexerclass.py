#!/usr/bin/python
# -*- coding: utf-8 -*-

#Copyright (c) 2008-2012 Nestor Arocha Rodriguez

"""LL(1) Recursive Descent Lexer
second recipe of the book "Language implementation patterns

grammar NestedNameList;
list : '[' elements ']' ; // match bracketed list
elements : element (',' element)* ; // match comma-separated list
element : NAME | list ; // element is name or nested list
NAME : ('a'..'z' |'A'..'Z' )+ ; // NAME is sequence of >=1 letter
"""

#tokenlist = ["NAME", "COMMA", "LBRACK", "RBRACK","EOF_TYPE"]

from pydsl.Grammar.Lexer import Lexer as _Lexer

class _ListLexer(_Lexer):
    def nextToken(self):
        import re
        from pydsl.Grammar.Lexer import finalchar
        while self.current != finalchar:
            if self.current == "/":
                self.comment(tl)
                continue
            elif self.current == " ":
                self.consume()
                continue
            elif self.current == ",":
                return self.comma()
            elif self.current == "[":
                return self.lbrack()
            elif self.current == "]":
                return self.rbrack()
            elif re.match("[a-zA-Z]", self.current):
                return self.name()
            else:
                raise Exception
        return ("EOF_TYPE", "")

    def comma(self):
        current = self.current
        self.match(",")
        return ("COMMA", current)

    def lbrack(self):
        current = self.current
        self.match("[")
        return ("LBRACK", current)

    def rbrack(self):
        current = self.current
        self.match("]")
        return ("RBRACK", current)

    def name(self):
        import re
        string = ""
        from pydsl.Grammar.Lexer import finalchar
        while self.current != finalchar and re.match("[a-zA-Z]", self.current):
            string += self.current
            self.consume()
        return ("NAME", string)


def function(inputdic, inputgrammar, outputdic):
    a = _ListLexer(inputdic["input"])
    result = []
    result.append(a.nextToken())
    while result[-1][0] != "EOF_TYPE":
        result.append(a.nextToken())
    return {"output":result}


iclass = "PythonTransformer"
inputdic = {"input":"cstring"}
outputdic = {"output":"cstring"}

