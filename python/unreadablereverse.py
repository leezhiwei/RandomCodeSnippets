# tried to reverse it, idk if it worked
import codecs
import base64
command = 'print("Hello World")'
commandbit = str.encode(command)
b642 = base64.b64encode(base64.b64encode(commandbit))
print(f"Here is weirdtext {b642}")
rot = codecs.encode("exec(__import__('base64').b64decode(__import__('base64').b64decode(weirdtext)))", 'rot13')
last = f"exec(__import__('codecs').decode('''{rot}'''))"
exec(f"finale = base64.b16encode(b\"{last}\")")
print(finale)
