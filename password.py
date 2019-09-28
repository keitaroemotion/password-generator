#!/usr/bin/env python

import random

class Password:
    def int_to_word(self, password_length=13):
        num = random.randint(1, 200000)
        if password_length == 0:
            return ""
        text = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ%&$#012345678"
        size = len(text)
        return list(text)[num % size] + self.int_to_word(password_length - 1)

    def create(self):
        return self.int_to_word()

print(Password().create())
