DataMosh v1.0.0
OwenDavisBower.com

DataMosh modifies raw file data in order to create "glitchy" effects.
The program will generate the glitched version in a new file, so you
do not need to worry about corrupting your original version.

Instructions:
- Navigate to directory containing DataMosh (use CD command) in terminal
- Type command: python DataMosh.py <FileToGlitch> <Changes> <ChangeSize> <MinPos>
  = Example: python DataMosh.py OriginalVideo.MOV 6000 200 100

<FileToGlitch> should be the filepath to the file you want to glitch,
including any extensions.
 - NOTE: DataMosh is currently sensitive to filenames that include spaces
   and parenthesis in the current version.

<Changes> refers to the number of changes you want to be made to the file,
the more changes the "glitchier" the outcome. The default value is 500.

<ChangeSize> refers to the number of characters to modify each change.
The default value is 150.

<MinPos> refers to the minimum position in the data to begin modifying from.
The default value is 150.
 - WARNING: Low minimum positions may breach header data, making files unreadable.