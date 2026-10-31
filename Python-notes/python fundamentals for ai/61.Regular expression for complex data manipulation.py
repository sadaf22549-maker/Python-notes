#Regular expression
'''regular expression is used for complex data manipulation'''

import re #for using regular expression,we have to import re.

text='''Our research team has three members: Alex, Sarah, and David.
Contact details:
alex123@gmail.com
sarah456@yahoo.com
david789@gmail.com
mike101@gmail.com
lisa202@yahoo.com
Mission records:
MARS-1001 launched on 12/05/2024.
MOON-2001 launched on 15/08/2023.
MARS-1002 launched on 20/11/2025.
MOON-2002 launched on 03/02/2024.
MARS-1003 launched on 17/06/2022.
The rover traveled 125 kilometers, collected 45 samples, and captured 230 images. Another rover traveled 200 kilometers, collected 60 samples, and captured 310 images.'''

pattern1=r"\w+@\w+.com"
pattern2=r"\w+-\d+"
pattern3=r"\d+/\d+/\d+"
'''r is used to identify it as a pattern.
\w+ -->one or many digits,letters & underscores
\d+ -->one or many digits
'''

gmail=re.findall(pattern1,text)
mission_records=re.findall(pattern2,text)
date=re.findall(pattern3,text)
#.findall() is a method by which we can extract our required words.we have to pass 2 params here.Pattern & our text.

for i in gmail:
	print(i)
print("\n")	
for i in mission_records:
	print(i)
print("\n")	
for i in date:
	print(i)		
