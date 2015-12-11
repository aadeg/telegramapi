'''
TelegramAPI
Copyright (C) 2015  Giove Andrea

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License along
with this program; if not, write to the Free Software Foundation, Inc.,
51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.
'''


class TelegramException(Exception):
    def __init__(self, info):
        self.info = info

    def __str__(self):
        return repr(self.info)


class ObjectDecodingException(TelegramException):
    MSG = "Exception trying to decode a %s object."

    def __init__(self, obj_type, j):
        TelegramException.__init__(self,
                                   ObjectDecodingException.MSG % self.obj_type)
        self.obj_type = obj_type
        self.json = j

    def __str__(self):
        return "Exception trying to decode a %s object." % (
            self.obj_type)
