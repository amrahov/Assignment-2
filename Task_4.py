#import libraries here

def main():
  year=int(input("Enter the year [ex. 2021]: "))
  if year>0:
      if year%12==0:
          print(f"{year} is the year of the Monkey")
      elif year%12==1:
          print(f"{year} is the year of the Rooster")
      elif year%12==2:
          print(f"{year} is the year of the Dog")
      elif year%12==3:
          print(f"{year} is the year of the Pig")
      elif year%12==4:
          print(f"{year} is the year of the Rat")
      elif year%12==5:
          print(f"{year} is the year of the Ox")
      elif year%12==6:
          print(f"{year} is the year of the Tiger")
      elif year%12==7:
          print(f"{year} is the year of the Hare")
      elif year%12==8:
          print(f"{year} is the year of the Dragon")
      elif year%12==9:
          print(f"{year} is the year of the Snake")
      elif year%12==10:
          print(f"{year} is the year of the Horse")
      else:
          print(f"{year} is the year of the Sheep")
  else:
      print("Invalid year!")
  pass

if __name__ == "__main__":
  main()
