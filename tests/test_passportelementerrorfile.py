#!/usr/bin/env python
#
# A library that provides a Python interface to the Telegram Bot API
# Copyright (C) 2015-2021
# Leandro Toledo de Souza <devs@python-telegram-bot.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser Public License for more details.
#
# You should have received a copy of the GNU Lesser Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].
import inspect

import pytest

from telegram import PassportElementErrorFile, PassportElementErrorSelfie


@pytest.fixture(scope='class')
def passport_element_error_file():
    return PassportElementErrorFile(
        TestPassportElementErrorFile.type_,
        TestPassportElementErrorFile.file_hash,
        TestPassportElementErrorFile.message,
    )


class TestPassportElementErrorFile:
    source = 'file'
    type_ = 'test_type'
    file_hash = 'file_hash'
    message = 'Error message'

    def test_extra_slots(self, passport_element_error_file):
        members = inspect.getmembers(
            passport_element_error_file.__class__,
            predicate=lambda b: not inspect.isroutine(b) and (inspect.ismemberdescriptor(b)),
        )
        for member in members:
            val = getattr(passport_element_error_file, member[0], 'err')
            assert False if val == 'err' else True, f"got extra slot '{member[0]}'"

    def test_expected_values(self, passport_element_error_file):
        assert passport_element_error_file.source == self.source
        assert passport_element_error_file.type == self.type_
        assert passport_element_error_file.file_hash == self.file_hash
        assert passport_element_error_file.message == self.message

    def test_to_dict(self, passport_element_error_file):
        passport_element_error_file_dict = passport_element_error_file.to_dict()

        assert isinstance(passport_element_error_file_dict, dict)
        assert passport_element_error_file_dict['source'] == passport_element_error_file.source
        assert passport_element_error_file_dict['type'] == passport_element_error_file.type
        assert (
            passport_element_error_file_dict['file_hash'] == passport_element_error_file.file_hash
        )
        assert passport_element_error_file_dict['message'] == passport_element_error_file.message

    def test_equality(self):
        a = PassportElementErrorFile(self.type_, self.file_hash, self.message)
        b = PassportElementErrorFile(self.type_, self.file_hash, self.message)
        c = PassportElementErrorFile(self.type_, '', '')
        d = PassportElementErrorFile('', self.file_hash, '')
        e = PassportElementErrorFile('', '', self.message)
        f = PassportElementErrorSelfie(self.type_, self.file_hash, self.message)

        assert a == b
        assert hash(a) == hash(b)
        assert a is not b

        assert a != c
        assert hash(a) != hash(c)

        assert a != d
        assert hash(a) != hash(d)

        assert a != e
        assert hash(a) != hash(e)

        assert a != f
        assert hash(a) != hash(f)
