from __future__ import annotations
import sys
import csv
from typing import *
from dataclasses import dataclass
import unittest
import math
sys.setrecursionlimit(10_000)

# Put your data definitions first!
@dataclass(frozen=True)
class Row
  country: str
  year: int
  electricity_and_heat_co2_emissions: float|None
  electricity_and_heat_co2_emissions_per_capita: float|None
  energy_co2_emission: float|None
  energy_co2_emissions_per_capita	total_co2_emissions_excluding_lucf: float|None
  total_co2_emissions_excluding_lucf_per_capita: float|None
  
class Node
  value = Row
  next = Node | None
     
# ...

# Then your functions.

read_csv_lines(filename: str) -> Optional[Node]
  

# ...
