
# l = int(input("Enter length: "))
# w = int(input("Enter width: "))
# h = int(input("Enter height: "))

def volume(l, w, h):
  if l < 0 or w < 0 or h < 0:
      return "Cannot have negative volume"
  return (l * w * h)

# print(volume(l, w, h))

    