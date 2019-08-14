import urllib.request
import subprocess
x = 0
y = 0
already = []

while 1 == 1:
	try:
		batcmd = "curl -S --fail --silent --show-error https://meme-api.herokuapp.com/gimme"
		result = subprocess.check_output(batcmd, shell=True)
		result = str(result)
		while "imgur" in result:
			batcmd = "curl -S --fail --silent --show-error https://meme-api.herokuapp.com/gimme"
			result = subprocess.check_output(batcmd, shell=True)
			result = str(result)
		sep = '"url":"'
		result = result.rsplit(sep, 1)[1]
		result = result.rsplit("\"", 1)[0]
		name = result.replace("https://i.redd.it/","")
	except:
		pass
	try:
		if name in already:
			y = y + 1
			pass
		else:
			try:
				urllib.request.urlretrieve(result, name)
				x = x + 1
				already.append(name)
				print("Got [" + str(x) + "] " + name + " Duplicates " + str(y))
			except:
				pass
	except:
		pass
