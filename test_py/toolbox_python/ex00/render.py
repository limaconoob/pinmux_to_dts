from sys import argv
from os.path import exists

def main(av):
	if len(av) == 2:
		script, from_file = av
		if not exists("./settings.py"):
			print ("Error (Settings): unexisting file [settings.py]")
		elif from_file.endswith(".template") and exists(from_file):
			in_file = open(from_file)
			indata = in_file.read()
			bonjour = open("./settings.py")
			salut = indata.split()
			for ligne in salut:
				if "=" in ligne:
					print (ligne)
					line = ligne.split()
					if len(line) == 3 and line[0] == "=":
						pass
						#for data in indata:
						#	if 
			out_file = open("./file.html", 'w')
			out_file.write(indata)
			out_file.close()
			in_file.close()
	else:
		print("Error (Usage): python render.py [{}.template]")

main(argv)
