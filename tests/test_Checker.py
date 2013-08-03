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

__author__ = "Nestor Arocha"
__copyright__ = "Copyright 2008-2013, Nestor Arocha"
__email__ = "nesaro@gmail.com"

import unittest

class TestMongoChecker(unittest.TestCase):
    """Mongo checker"""
    def testCheck(self):
        """Test checker instantiation and call"""
        bad = {"a":1,"b":3}
        letter = {"a":1,"b":"asd"}
        from pydsl.Checker import MongoChecker
        from pydsl.contrib.mongogrammar import spec, fullspec
        checker = MongoChecker(spec)
        self.assertTrue(checker.check(spec))
        self.assertFalse(checker.check(bad))
        fullchecker = MongoChecker(fullspec)
        self.assertTrue(fullchecker.check(spec))
        self.assertTrue(fullchecker.check(bad))
        self.assertFalse(fullchecker.check(letter))
        #self.assertRaises(TypeError,fullchecker.check, "")

class TestBNFChecker(unittest.TestCase):
    """BNF Checker"""
    def testCheck(self):
        """Test checker instantiation and call"""
        from pydsl.Checker import BNFChecker
        from pydsl.contrib.bnfgrammar import productionset0
        grammardef = productionset0
        checker = BNFChecker(grammardef)
        self.assertTrue(checker.check("SR"))
        self.assertFalse(checker.check("SL"))

class TestRegularExpressionChecker(unittest.TestCase):
    """BNF Checker"""
    def testCheck(self):
        """Test checker instantiation and call"""
        from pydsl.Checker import RegularExpressionChecker
        checker = RegularExpressionChecker("abc")
        self.assertTrue(checker.check("abc"))
        self.assertFalse(checker.check("abd"))

class TestPLYChecker(unittest.TestCase):
    def testCheck(self):
        """Test checker instantiation and call"""
        from pydsl.Checker import PLYChecker
        from pydsl.contrib.grammar import example_ply
        from pydsl.Grammar.Definition import PLYGrammar
        grammardef = PLYGrammar(example_ply)
        checker = PLYChecker(grammardef)
        self.assertTrue(checker.check("O"))
        self.assertFalse(checker.check("FALSE"))


class TestJsonSchemaChecker(unittest.TestCase):
    def testCheck(self):
        """Test checker instantiation and call"""
        from pydsl.Grammar.Definition import JsonSchema
        from pydsl.Checker import JsonSchemaChecker
        schema = {
            "type" : "string",
            "items" : {
                "type" : ["string", "object"],
                "properties" : {
                    "foo" : {"enum" : [1, 3]},
                    #"bar" : { #See https://github.com/Julian/jsonschema/issues/89
                    #    "type" : "array",
                    #    "properties" : {
                    #        "bar" : {"required" : True},
                    #        "baz" : {"minItems" : 2},
                    #    }
                    #}
                }
            }
        }
        grammardef = JsonSchema(schema)
        checker = JsonSchemaChecker(grammardef)
        self.assertTrue(checker.check("a"))
        self.assertFalse(checker.check([1, {"foo" : 2, "bar" : {"baz" : [1]}}, "quux"]))


class TestEncodingChecker(unittest.TestCase):
    def testCheck(self):
        from pydsl.Checker import EncodingChecker
        from pydsl.Alphabet.Definition import Encoding
        a = Encoding('ascii')
        checker = EncodingChecker(a)
        self.assertTrue(checker.check('asdf'))
        self.assertFalse(checker.check('£'))

class TestAlphabetListDefinitionChecker(unittest.TestCase):
    def testCheck(self):
        from pydsl.Checker import AlphabetListChecker
        from pydsl.Alphabet.Definition import AlphabetListDefinition
        a = AlphabetListDefinition(['integer'])
        checker = AlphabetListChecker(a)
        self.assertTrue(checker.check('1234'))
        self.assertFalse(checker.check('abc'))
