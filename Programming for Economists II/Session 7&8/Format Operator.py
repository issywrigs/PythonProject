#% is overloaded to work with strings
#When applied to integer numbers it is the modulus operator.
#When applied to strings it allows us to construct new strings by replacing parts of the string with the data stored in variables

template = "Today is %s"
template % "Tuesday" #Today is Tuesday

#A format sequence starts with %.
#It can be anywhere in the string
#After the % you need a conversion type.
#The most common conversion types are: %d – integer, %g – float, %x – hexadecimal, %s – string
template = "%s I have seen %d %s."
template % ("Today", 3, "dogs") # 'Today I have seen 3 dogs.'
template % ("On Monday", 7, "cats") # 'On Monday I have seen 7 cats.'

#If more than 1 format sequence then the arguments must be placed between () = tuple

