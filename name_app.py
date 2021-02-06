
def fullName(fname, lname):
  if len(fname) == 0 or len(lname) == 0:
    return "First or last name empty"
  return fname + " " + lname

print(fullName("Michael", "Boly"))

    