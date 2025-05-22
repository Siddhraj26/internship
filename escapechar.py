'''txt = 'It\'s alright.'
print(txt) #\'	Single Quote


txt = "This will insert one \\ (backslash)."
print(txt) #\\	Backslash


txt = "Hello\nWorld!"
print(txt) #\n	New Line
'''

txt = "Hello\rWorld!"
print(txt) #\r	Carriage Return


txt = "Hello\tWorld!"
print(txt) #\t	Tab

#This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt) #\b	Backspace


#A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt) 


#A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) #\xhh	Hex value


# Form Feed example:
txt = "Hello\fWorld!"
print(txt) #\f	Form Feed





