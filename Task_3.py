#import libraries here

def main():
  lenght=int(input("Enter the wavelength in nm: "))
  if lenght>=380 and lenght<450:
      print("The relevant color is Violet")
  elif lenght>=450 and lenght<495:
      print("The relevant color is Blue")
  elif lenght>=495 and lenght<570:
      print("The relevant color is Green")
  elif lenght>=570 and lenght<590:
      print("The relevant color is Yellow")
  elif lenght>=590 and lenght<620:
      print("The relevant color is Orange")
  elif lenght>=620 and lenght<=750:
      print("The relevant color is Red")
  else:
      print("Invalid input!")
  pass

if __name__ == "__main__":
  main()
