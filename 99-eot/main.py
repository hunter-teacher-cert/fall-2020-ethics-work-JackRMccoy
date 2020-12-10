# default values
print('\033[1;32;44m Let\'s Save the Earth \033[22;39;49m')
print("        _____")
print("    ,-:` \;',`'-, ")
print("  .'-;_,;  ':-;_,'.")
print(" /;   '/    ,  _`.-\\")
print("| '`. (`     /` ` \`|")
print("|:.  `\`-.   \_   / |")
print("|     (   `,  .`\ ;'|")
print(" \     | .'     `-'/")
print("  `.   ;/        .'")
print("jgs `'-._____.\n\n")

currentLifeSpan = 1.25
globalPhoneSales = 1.5
print("Current figures estimate that 1.5 billion smartphones are sold every year.  The average consumer keeps their phone for about 15 months.")

def saveTheWorld():
  newLife = float(input("How many months do you keep your phone? \n"))/12
  percentChange = (newLife - currentLifeSpan)/currentLifeSpan
  newPhoneSales = globalPhoneSales*(currentLifeSpan/newLife)
  print("\nIf everybody kept their phones for %3.2f years..." %(newLife))
  phonesSaved = int((globalPhoneSales - newPhoneSales) *1000)
  print()
  print("That's a reduction of about " + str(phonesSaved) +" million phones per year!")
  print("\nCurrently, about 22% of phones purchased are bought used.")
  usedPercent = (int(input("What percentage of people should buy used phones?\n")))
  usedPhoneSales = newPhoneSales*(1-usedPercent/100)
  usedSaves = (newPhoneSales-usedPhoneSales)*1000
  print("\nIf %d percent of people bought refurbished phones, that would save an additional %d million phones." %(usedPercent, usedSaves))
  print("With those numbers combined, that is %3.2f billion phones not produced." %((phonesSaved+usedSaves)/1000))
  print("That is %3.2f billion kg of CO2 saved." %((phonesSaved+usedSaves)*16/1000))
  print("\nThis is %3.2f millionths of a percent of the total CO2 output of the world.\n" %((phonesSaved+usedSaves)*16/5000))  


saveTheWorld()
print("\033[1;32;44mWe... did it?\033[22;39;49m\n")
print("At the current rate of production, the important Rare Earth Element Neodymium, used in production of wind turbines, electric cars, solar cells, batteries, and nearly every type of modern electronic, might run out in about 20 years.  Your efforts have increased that time span and reduced the cost of green electronics.\n")
goAgain = int(input("Would you like to tweak the numbers? 1 for yes, 2 for no.\n"))
while (goAgain == 1):
  saveTheWorld()
  print("\033[1;32;44mWe're still screwed aren't we?\033[22;39;49m\n")
  goAgain = int(input("Would you like to tweak the numbers? 1 for yes, 2 for no.\n"))
  print()

print("Hey at least neodymium might last a little longer?")

