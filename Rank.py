# A Group project by Team Happiness(Serena Sinha, Aayush Kumar Pathak, Lakshay )
''' SECTION - KOC09'''

def nameRank(names, marks, updates, n):
	
	# list of students
	x = [[0 for j in range(3)] for i in range(n)]
	for i in range(n):
		
		# Storing name of the student
		x[i][0] = names[i]
		
		# Updateing the marks of the student
		x[i][1]= marks[i] + updates[i]
		
		# current rank of the student
		x[i][2] = i + 1
		
	highest = x[0]
	for j in range(1, n):
		if (x[j][1] >= highest[1]):
			highest = x[j]
			
	# Print the Required output
	print("Name: ", highest[0], ", Jump in Rank: ",
			abs(highest[2] - 1), sep="")

#__main-Bodys___

# Names of the students
names= ["Serena", "Aayush", "Lakshay"]

# Marks of the students
marks = [80, 79, 75]

# Updates in marks
updates = [0, 2, +5]

# Number of students
n = len(marks)
# Calling function 
nameRank(names, marks, updates, n)


