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

expected_header = expected_header = [
    "country",
    "year",
    "electricity_and_heat_co2_emissions",
    "electricity_and_heat_co2_emissions_per_capita",
    "energy_co2_emissions",
    "energy_co2_emissions_per_capita",
    "total_co2_emissions_excluding_lucf",
    "total_co2_emissions_excluding_lucf_per_capita"
]
def parse_float(s: str) -> Optional[float]:
    if s == "":
        return None
    return float(s)


def parse_row(fields: list[str]) -> Row:
    return Row(
        fields[0],
        int(fields[1]),
        parse_float(fields[2]),
        parse_float(fields[3]),
        parse_float(fields[4]),
        parse_float(fields[5]),
        parse_float(fields[6]),
        parse_float(fields[7]),
    )
  
def read_csv_lines(filename: str) -> Optional[Node]:
  with open(filename, newline="") as csvfile:
          reader = csv.reader(csvfile)
          header = next(reader)
  if header != expected_header:
    raise ValueError("Invalid header row")
            
 rows = list(reader)
        return build_list(rows)


def build_list(rows: list[list[str]]) -> Optional[Node]:
    if rows == []:
        return None
    return Node(parse_row(rows[0]), build_list(rows[1:]))

  
# return Row( country: str
#   year: int
#   electricity_and_heat_co2_emissions: float|None
#   electricity_and_heat_co2_emissions_per_capita: float|None
#   energy_co2_emission: float|None
#   energy_co2_emissions_per_capita	total_co2_emissions_excluding_lucf: float|None
#   total_co2_emissions_excluding_lucf_per_capita: float|None)

     case None:
       return Node(value, None)
     case Node(val, next):
       return Node(val, append(Node))
  
# ...
