#---------------------
# Summer Davis
# COSC 1336
# Project 6
#---------------------
# Objective: Program will read a file (data.txt) that contains
# integer values and create a list.
#
# Program will display:
# - the numbers
# - the count of the numbers
# - the sum of the numbers
# - the average of the numbers
# - the maximum integer
# - the minimum integer
# 
#---------------------

# Display the start of the project
def header ():
    print('\n')
    print('Grade Statistics Summary')
    print('-' * 80)

# Collect and organize all of the program tasks
def main():
    
    # Header of the project
    header()

    # Read file and collect list of numbers
    numbers = readData('data.txt')

    # Generate grade statistics summary
    generateSummary(numbers)
    
    # End of project display
    footer()

# Generate the average of a list
def generateAverage(numbers):

    average = sum(numbers)/len(numbers)
    return average
    
# Display the numbers from a list
def generateNumbers(numbers):
    
    numberSet = ', '.join(map(str, numbers))
    return numberSet
        
# Generate grade statistics summary
def generateSummary(numbers):

    # Display numbers
    print(f'The numbers are {generateNumbers(numbers)}')

    # Display count
    print(f'The count of numbers is {len(numbers)}')

    # Display sum
    print(f'The sum of numbers is {sum(numbers)}')

    # Display average
    print(f'The average of the numbers is {generateAverage(numbers):,.2f}')

    # Display max number
    print(f'The max number is {max(numbers)}')

    # Display min number
    print(f'The min number is {min(numbers)}')

# Read file and return list of numbers
def readData(file):
    fileName = open(file, 'r')

    numbers = []
    
    for line in fileName:
        newLine = line.strip('\n')
        numbers.append(int(newLine))

    fileName.close()

    return numbers


# Get users entry of string data
def getStringEntry(prompt):
    while (True):
        value = input(prompt)
        return  value


# Get users entry of ONLY float data
def getFloatEntry(prompt):
    while (True):
        try:
            value = float(input(prompt))
            return value

        except ValueError: 
            print('Error Msg: Non Numbers entered.')

# Get users entry of ONLY integer data
def getIntegerEntry(prompt):
    while (True):
        try:
            value = int(input(prompt))
            return value
        

        except ValueError: 
            print('Error Msg: Non Integers entered.')
    
# Display the end of the project
def footer():
    print('\n')
    print('-' * 80)
    print('End of Project 6')

# Call the main function  
main()
