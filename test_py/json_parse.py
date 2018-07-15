import json
from pprint import pprint

with open("../AM335xMichel.pinmux") as bonjour:
  coucou = json.load(bonjour)

pprint (coucou)
