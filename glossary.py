import json

glossary = {}

definition = """
'Exchange' is shorthand for a 'Shuffle Exchange. This means that Spark is sending data between executors, probably across the network. This is more often described as merely a 'shuffle'.  This happens between jobs. 
"""

glossary["exchange"] = definition

with open("glossary.json", "w") as f:
  json.dump(glossary, f)
