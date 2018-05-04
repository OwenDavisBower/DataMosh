'''
DataMosh v1.0.0

Developed by Owen Davis-Bower
OwenDavisBower.com
'''

import string, random, sys, os, shutil

# Generate a random string of characters
def randString(size=1, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for x in range(size))

def main():
	# Number of changes to make in process
	changes = 500
	# Position in text to start glitching
	minPos = 150
	# Number of characters to change at a time
	changeSize = 150

	# Accept optional arguments from commandline (changes, changeSize, and minPos)
	if len(sys.argv) >= 3:
		changes = int(sys.argv[2])
	if len(sys.argv) >= 4:
		changeSize = int(sys.argv[3])
		changeSize = min(changeSize, 2)
	if len(sys.argv) >= 5:
		minPos = int(sys.argv[4])

	# Extract filename and file extension from commandline argument
	fileName, fileExtension = os.path.splitext(sys.argv[1])
	# Print informational message at start
	print("Glitching " + fileName + fileExtension)
	# Generate a new file name to save glitched file to
	newFileName = fileName + '_Glitched'

	# Copy file to new file
	shutil.copyfile(fileName + fileExtension, newFileName + fileExtension)
	# Convert new file to text file for modification
	os.rename(newFileName + fileExtension, newFileName + '.txt')
	# Open new text file
	openedFile = open(newFileName + '.txt')
	# Extract text from text file
	text = openedFile.read()
	# Close text file to save memory
	openedFile.close()
	# Remove the temporary txt file
	os.remove(newFileName + '.txt')

	# Count the number of characters in file
	characterCount = len(text)
	# Convert text to list for quick mutability
	textList = list(text)

	# Ensure that there are enough characters
	if characterCount > minPos:
		# Modify the file the specified number of times
		for i in range(changes):
			# Select a random position to modify the file
			position = random.randrange(minPos, characterCount - 1)
			# Select a random size to modify (how many characters)
			# Confines size to within the existing characters, as to
			# not change file size which causes corruption.
			size = random.randrange(1, min(changeSize, characterCount - position))
			# Generate random characters for replacement
			newCharacters = randString(size)
			# Replace characters in location
			textList[position:position + size] = newCharacters;

	# Convert list back to text file
	text = ''.join(textList)
	# Create new file to copy finished version to
	writeFile = open(newFileName + fileExtension, 'w')
	# Write the modified text to a new file & close the file
	writeFile.write(text)
	writeFile.close()

	# Print informational message upon completion
	print("Wrote to: " + newFileName + fileExtension)

if __name__ == "__main__":
	main()