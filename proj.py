#_______________________________________________________________________________

#-----------------------------CALORIE TRACKER PROGRAM---------------------------
#_______________________________________________________________________________

print"\n\n"
print "                                     HELLO !!!"
print "                      WELCOME TO OUR CALORIE TRACKER PROGRAM..."
print "         WE PROVIDE YOU WITH INFO ON YOUR CALORIE BURN AFTER A GREAT WORKOUT!"
print "\n"
#READING ALL VALUES

x=input("Enter your mass in kgs : ")
y=input("Enter your height in metres : ")
age=input("Enter your age : ")
gen=raw_input("Enter your gender : ")


# CALCULATING THE BODY MASS INDEX RATIO

bmi=(x)/(y**2)
bm=float(bmi)
print "\n"


if bm<18.5:
   print "You are underweight"
elif bm>=18.5 and bm<=24.9:
   print "You are healthy"
elif bm>=24.9 and bm<=29.9:
   print "You are overweight,"
   print "You need to work out more and lose weight"
   x=1
elif bm>=30:
   print "You are overweight,"
   print "You need to work out more and lose weight"
   x=2
else:
   print "Invalid option chosen !"



# FOR PEOPLE WHO ARE OVERWEIGHT :-

if x==2 and x==2:
   print "\n"
   if gen=="m" or gen=="M":
      b=input("Enter the number of minutes spent on treadmill : ")
      c=input("Enter your average heart rate during this : ")
      treadmill=(((age*0.02017)-(x*0.09036)+(c*.6309)-(55.0969))*b)/4.184
      d=input("Enter the number of minutes spent on elliptical : ")
      f=input("Enter your average heart rate during this : ")
      elliptical=(((age*0.02017)-(x*0.09036)+(f*0.06309)-(55.0969))*d)/4.184
      o=treadmill+elliptical
      print "Total no. of calories burnt = ",o

   if gen=="f" or gen=="f":
      b=input("Enter the number of minutes spent on treadmill : ")
      c=input("Enter your average heart rate during this : ")
      treadmill=(((age*0.074)-(x*0.05742)+(c*0.4722)-(20.4022))*b)/4.184
      d=input("Enter the number of minutes spent on elliptical : ")
      f=input("Enter your average heart rate during this : ")
      elliptical=(((age*0.074)-(x*0.05742)+(d*0.4722)-(20.4022))*c)/4.184
      u=treadmill+elliptical
      print "Total no. of calories burnt = ",u
 
print "\n\n","                    Thank You And Have A Healthy Day Ahead !!!"

#________________________________THE END________________________________________
#_______________________________________________________________________________
