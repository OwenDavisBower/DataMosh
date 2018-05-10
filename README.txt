DataMosh v1.0.0
OwenDavisBower.com

DataMosh modifies raw file data in order to create "glitchy" effects.
The program will generate the glitched version in a new file, so you
do not need to worry about corrupting your original version.

Instructions:
- Navigate to directory containing DataMosh (use CD command) in terminal
- Type command: python DataMosh.py <FileToGlitch> <GlitchAmount> <GlitchSize> <StartPos>
  = Example: python DataMosh.py OriginalVideo.MOV 6000 200 100
  = Note: You can use '_'s to leave a parameter default
  	- Example: python DataMosh.py OriginalVideo.MOV _ _ 100

<FileToGlitch> should be the filepath to the file you want to glitch,
including extensions.
 - NOTE: DataMosh is currently sensitive to filenames that include spaces
   and parenthesis in the current version.

<GlitchAmount> refers to the number of glitches you want to be made to the file,
the more glitches the "glitchier" the outcome. The default value is 500.

<GlitchSize> refers to the amount of data to modify each "glitch".
The default value is 150.

<StartPos> refers to the minimum position in the data to begin glitching from.
The default value is 150.
 - WARNING: Low starting positions may breach header data, making files unreadable.

 * Sample video to test the program: http://bit.ly/2IwhRwM *