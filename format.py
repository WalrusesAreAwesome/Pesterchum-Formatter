text = open("input.txt").read().split("\n")

colors = {
	"CBH": "2ecc71",
	"SMH": "f1c40f",
	"SFH": "3498db",
	"TAH": "e91e63",
	"HAH": "9b59b6",
	"EB": "0715cd",
	"TT1": "b536da",
	"TG1": "e00707",
	"GG1": "4ac925",
	"GT": "1f9400",
	"TT2": "f2a400",
	"TG2": "ff6ff2",
	"GG2": "00d5f2",
	"AA": "a10000",
	"AT": "a15000",
	"TA": "a1a100",
	"CG": "626262",
	"AC": "416600",
	"GA": "008141",
	"GC": "008282",
	"AG": "005682",
	"CT": "000056",
	"TC": "2b0057",
	"CA": "61006a",
	"CC": "77003c",
	"UU": "",
	"uu": ""
}

handles = {
	"TT1": "TT",
	"TG1": "TG",
	"GG1": "GG",
	"TT2": "TT",
	"TG2": "TG",
	"GG2": "GG",
}

print('      "content": "|PESTERLOG|', end = "")
for message in text:
	print('<br /><span style=\\"color: #{}\\">'.format(colors[message[0:message.index(":")]]), end = "")
	print(message[0:2], end = "")
	print(message[message.index(":")::], end = "</span>")
print('",')