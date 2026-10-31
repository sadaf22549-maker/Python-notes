#Conclusion
import time

for i in range(1,68):
	print("=",end="")
print("\n")

time.sleep(3)
print("This is just the begining...".center(67,"*"))
print("\n")
logo = [
    "          ********",
    "       *************",
    "      *****    *****",
    "      *****",
    "      *****",
    "       ************",
    "          ********",
    "              *****",
    "      *****   *****",
    "      *************",
    "         ********"
]

width = 50

for line in logo:
    print(line.center(width))
print("\n")

for i in range(1,68):
	print("=",end="")		