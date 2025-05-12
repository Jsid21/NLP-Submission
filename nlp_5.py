words = ["playing", "played", "studies", "students","happily"]
def create_table(words):
  table = []
  add=""
  delete=""
  root = ""
  table = []
  for word in words:
    if word.endswith("ing") and len(word)>4:
      root = word[:-3]
      delete = "ing"
      add=""
    elif word.endswith("ies"):
      root = word[:-3] + "y"
      add = "y"
      delete = "ies"
    elif word.endswith("ed"):
      root = word[:-2]
      delete = "ed"
      add=""
    elif word.endswith("ly"):
      root = word[:-2]
      add = "y"
      delete = "ly"
      add=""
    elif word.endswith("s"):
      root = word[:-1]
      delete = "s"
      add=""
    else:
      root = word
      add=""
      delete=""
    
    table.append({"word":word,"root":root,"add":add,"delete":delete})
  return table
table = create_table(words)
print(f"{'Word':<12}{'Root':<10}{'Add':<10}{'Delete':<10}")

for entry in table:
  print(f"{entry['word']:<12}{entry['root']:<10}{entry['add']:<10}{entry['delete']:<10}")
