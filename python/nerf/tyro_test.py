"""
<!-- ******************************************
*  Author : Levin Jian  
*  Created On : Fri Sep 08 2023
*  File : tyro_test.py
******************************************* -->

"""

#"""Sum two numbers from argparse."""

import argparse



"""Sum two numbers by calling a function with tyro."""
import tyro
from dataclasses import dataclass

def add(a: int, b: int = 3) -> int:
    return a + b

# Populate the inputs of add(), call it, then return the output.
total = tyro.cli(add)

@dataclass
class Args:
    a: int
    e: int = 15

args = tyro.cli(Args)
print(args.a + args.e)

print(total)