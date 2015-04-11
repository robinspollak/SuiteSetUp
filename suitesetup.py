from flask import Flask
from flask import render_template
import random
class Suite:
	def __init__(self,name,room1,room2,room3,room4,room5,room6,numpeople,numsing,numdub,num2rm,balc,pat,cr,encbath,enclosed,subfree):
		self.name=name
		self.rooms=[room1,room2,room3,room4,room5,room6]
		self.drawnumbersused=[]
		for room in self.rooms:
			if room==0:
				rooms.remove(room)
		self.numpeople=numpeople
		self.numsing=numsing
		self.numdub=numdub
		self.balc=(True if balc=='1' else False)	
		self.pat=(True if pat=='1' else False)
		self.cr=(True if cr=='1' else False)	
		self.encbath=encbath
		self.enclosed=(True if enclosed=='1' else False)
		self.subfree=(True if subfree=='1' else False)
	def __repr__(self):
		toreturn = ''
		if self.numsing==1:
			if self.numdub==1:
				toreturn+=('%s is a %s person suite with %s single and %s double. ') %(self.name,self.numpeople,self.numsing,self.numdub)
			else:
				toreturn+=('%s is a %s person suite with %s single and %s doubles. ') %(self.name,self.numpeople,self.numsing,self.numdub)
		elif self.numdub==1:
			toreturn+=('%s is a %s person suite with %s singles and %s double. ') %(self.name,self.numpeople,self.numsing,self.numdub)
		else:
			toreturn+=('%s is a %s person suite with %s singles and %s doubles. ') %(self.name,self.numpeople,self.numsing,self.numdub)
		if self.balc:
			toreturn+='This suite has a balcony. '
		if self.pat:
			toreturn+='This suite has a patio. '
		if self.cr:
			toreturn+='This suite has a common room. '
		if self.subfree:
			toreturn+='This suite is in a subfree housing area. '
		if self.enclosed:
			if self.encbath==1:
				toreturn+='This is a fully enclosed suite that has %s bathroom. '%(self.encbath)
			else:
				toreturn+='This is a fully enclosed suite that has %s bathrooms. '%(self.encbath)
		else:
			toreturn+='This suite is more of a hallway, the bathrooms are on your hall. '
		toreturn+="The average room draw number required to get this suite is %d"%(self.getAverage())
		return toreturn
	def __getitem__(self,key):
		return self
	def adddrawnum(self,num):
		self.drawnumbersused.append(num)
	def getAverage(self):
		temp=0
		for number in self.drawnumbersused:
			temp+=float(number)
		return round((temp/(len(self.drawnumbersused))),2)

class roomDraw:
	def __init__(self,grade,drawnumber,building,rmnum):
		self.grade=grade
		self.num=drawnumber
		if building=='BLSD':
			self.building='Blaisdell'
		elif building=='MUDD':
			self.building='Mudd'
		elif building=='HAR':
			self.building='Harwood'
		elif building=='SMI':
			self.building='Smiley'
		elif building=='CL-I':
			self.building='Clark I'
		elif building=='N-CL':
			self.building='Norton Clark'
		elif building=='CL-V':
			self.building='Clark V'
		elif building=='WALK':
			self.building='Walker'
		elif building=='LWRY':
			self.building='Lawry'
		elif building=='POM':
			self.building='Pomona'
		elif building=='SNTG':
			self.building='Sontag'
		else:
			self.building = ''
		self.rmnum=rmnum
	def __str__(self):
		return('A %s with draw number %s chose room %s in %s')%(self.grade,self.num,self.rmnum,self.building)


suitedata = open('textfiles/suitedata.txt')
twok12 = open('textfiles/2012.txt')
twok13 = open('textfiles/2013.txt')
twok14 = open('textfiles/2014.txt')
#parse the suite data
listoflines = []
blaisdell,mudd,harwood,smiley,clarki,nortonclark,clarkv,walker,lawry,pomona,sontag = [],[],[],[],[],[],[],[],[],[],[]
for line in suitedata:
	listoflines.append(line)
splitlist = []
for suite in listoflines:
	splitlist.append(suite.split(','))
for mylist in splitlist:
	mylist[-1]=mylist[-1].strip('\n')
	if mylist[1]=='Blaisdell':
		blaisdell.append(mylist)
	if mylist[1]=='Mudd':
		mudd.append(mylist)
	if mylist[1]=='Harwood':
		harwood.append(mylist)
	if mylist[1]=='Smiley':
		smiley.append(mylist)
	if mylist[1]=='Clark I':
		clarki.append(mylist)
	if mylist[1]=='Norton Clark':
		nortonclark.append(mylist)
	if mylist[1]=='Clark V':
		clarkv.append(mylist)
	if mylist[1]=='Lawry':
		lawry.append(mylist)
	if mylist[1]=='Walker':
		walker.append(mylist)
	if mylist[1]=='Pomona':
		pomona.append(mylist)
	if mylist[1]=='Sontag':
		sontag.append(mylist)
#parse the room draw data
data = [twok12,twok13,twok14]
listofdraws = []
for year in data:
	listoflines=[]
	for line in year:
		listoflines.append(line)
	splitlist=[]
	for draw in listoflines:
		splitlist.append(draw.split(','))
	for mylist in splitlist:
		mylist[-1]==mylist[-1].strip('\n')
		if (not(mylist[2]=='') and not(mylist[3]=='')):
			listofdraws.append(roomDraw(mylist[0],mylist[1],mylist[2],mylist[3]))


buildings = [blaisdell,mudd,harwood,smiley,clarki,nortonclark,clarkv,walker,lawry,pomona,sontag]
mylist = []
for building in buildings:
	for i in range(len(building)):
		suite = building[i]
		objectsuite=Suite(suite[0],suite[2],suite[3],suite[4],suite[5],suite[6],suite[7],suite[8],suite[9],suite[10],suite[11],suite[12],suite[13],suite[14],suite[15],suite[16],suite[17])
		building[i]=objectsuite
for draw in listofdraws:
	draw.rmnum=draw.rmnum.strip('\n')
	if draw.building=='Blaisdell':
		for suite in blaisdell:
			if draw.rmnum in suite.rooms:
				suite.adddrawnum(draw.num)
	if draw.building=='Mudd':
		for suite in mudd:
			if draw.rmnum in suite.rooms:
				suite.adddrawnum(draw.num)
	if draw.building=='Harwood':
		for suite in harwood:
			if draw.rmnum in suite.rooms:
				suite.adddrawnum(draw.num)
	if draw.building=='Smiley':
		for suite in smiley:
			if draw.rmnum in suite.rooms:
				suite.adddrawnum(draw.num)
	if draw.building=='Clark I':
		for suite in clarki:
			if draw.rmnum in suite.rooms:
				suite.adddrawnum(draw.num)
	if draw.building=='Norton Clark':
		for suite in nortonclark:
			if draw.rmnum in suite.rooms:
				suite.adddrawnum(draw.num)
	if draw.building=='Clark V':
		for suite in clarkv:
			if draw.rmnum in suite.rooms:
				suite.adddrawnum(draw.num)
	if draw.building=='Lawry':
		for suite in lawry:
			if draw.rmnum in suite.rooms:
				suite.adddrawnum(draw.num)
	if draw.building=='Walker':
		for suite in walker:
			if draw.rmnum in suite.rooms:
				suite.adddrawnum(draw.num)
	if draw.building=='Pomona':
		for suite in pomona:
			if draw.rmnum in suite.rooms:
				suite.adddrawnum(draw.num)
	if draw.building=='Sontag':
		for suite in sontag:
			if draw.rmnum in suite.rooms:
				suite.adddrawnum(draw.num)
allsuites=[]
for building in buildings:
	for suite in building:
		allsuites.append([suite.name,suite.getAverage()])

for i in range(len(allsuites)):
	for j in range(len(allsuites)-1,i,-1):
		if (allsuites[j][1]<allsuites[j-1][1]):
			temp=allsuites[j]
			allsuites[j]=allsuites[j-1]
			allsuites[j-1]=temp



class Person:
	def __init__(self,grade,low,medium,high):
		self.grade=grade
		self.low=low
		self.medium=medium
		self.high=high
	def __str__(self):
		if self.low:
			if self.medium:
				return 'this %s has had their low and medium draw numbers already.'%self.grade
			if self.high:
				return 'this %s has had their low and high draw numbers already.'%self.grade
			else:
				return 'this %s has had their low draw number already.'%self.grade
		if self.medium:
			if self.high:
				return 'this %s has had their medium and high draw numbers already.'%self.grade
			else:
				return 'this %s has had their medium draw number already.'%self.grade
		if self.high:
			return 'this %s has had their high draw number already.'%self.grade
		return 'this %s has not had any of their draw numbers yet.'%self.grade

def getRandomDrawNumber(person):
	random.seed()
	if person.grade=='Senior':
		if person.low:
			if person.medium:
				return random.randint(1,133)
			elif person.high:
				return random.randint(133,266)
		if person.medium:
			if person.high:
				return random.randint(266,400)
	elif person.grade=='Junior':
		if person.low:
			return random.randint(401,666)
		if person.medium:
			temp=random.randint(0,1)
			if temp==1:
				return random.randint(401,534)
			else:
				return random.randint(666,800)
		if person.high:
			return random.randint(534,800)
	else:
		temp=random.randint(0,2)
		if temp==0:
			return random.randint(1066,1200)
		if temp==1:
			return random.randint(933,1066)
		else:
			return random.randint(800,933)

def getGroupNumber(person1,person2,person3,person4):
	temp=0
	for i in range(1000):
		temp+=(getRandomDrawNumber(person1)+getRandomDrawNumber(person2)+getRandomDrawNumber(person3)+getRandomDrawNumber(person4))/4
	return temp/1000

def processGroup(person1,person2,person3,person4):
	number = getGroupNumber(person1,person2,person3,person4)
	for i in range(len(allsuites)):
		if allsuites[i][1]<number:
			continue
		return [allsuites[i-3][0],allsuites[i][0],allsuites[i+1][0],allsuites[i+4][0]]
robin=Person('Senior',True,True,False)
chuck=Person('Senior',False,True,True)
tim=Person('Senior',True,False,True)
will=Person('Senior',True,True,False)
suitesetup = Flask(__name__)
@suitesetup.route('/')
def homePage():
	return render_template('index.html')
@suitesetup.route('/explore')
def explorePage():
	return render_template('explore.html')
@suitesetup.route('/getmatched')
def getMatched():
	return render_template('getmatched.html')
@suitesetup.route('/northcampus')
def northCampus():
	return render_template('northcampus.html')
@suitesetup.route('/southcampus')
def southCampus():
	return render_template('southcampus.html')
@suitesetup.route('/Pomona')
def Pomona():
	topass = []
	for suite in pomona:
		topass.append(repr(suite))
	length = len(pomona)
	return render_template('dorm.html',topass=topass,length=length)
@suitesetup.route('/Sontag')
def Sontag():
	topass = []
	for suite in sontag:
		topass.append(repr(suite))
	length = len(sontag)
	return render_template('dorm.html',topass=topass,length=length)
@suitesetup.route('/Lawry')
def Lawry():
	topass = []
	for suite in lawry:
		topass.append(repr(suite))
	length = len(lawry)
	return render_template('dorm.html',topass=topass,length=length)
@suitesetup.route('/Clark5')
def Clark5():
	topass = []
	for suite in clarkv:
		topass.append(repr(suite))
	length = len(clarkv)
	return render_template('dorm.html',topass=topass,length=length)
@suitesetup.route('/NortonClark')
def ClarkIII():
	topass = []
	for suite in nortonclark:
		topass.append(repr(suite))
	length = len(nortonclark)
	return render_template('dorm.html',topass=topass,length=length)
@suitesetup.route('/ClarkI')
def ClarkI():
	topass = []
	for suite in clarki:
		topass.append(repr(suite))
	length = len(clarki)
	return render_template('dorm.html',topass=topass,length=length)
@suitesetup.route('/Walker')
def Walker():
	topass = []
	for suite in walker:
		topass.append(repr(suite))
	length = len(walker)
	return render_template('dorm.html',topass=topass,length=length)
@suitesetup.route('/Blaisdell')
def Blaisdell():
	topass = []
	for suite in blaisdell:
		topass.append(repr(suite))
	length = len(blaisdell)
	return render_template('dorm.html',topass=topass,length=length)
@suitesetup.route('/Mudd')
def Mudd():
	topass = []
	for suite in mudd:
		topass.append(repr(suite))
	length = len(mudd)
	return render_template('dorm.html',topass=topass,length=length)
@suitesetup.route('/Harwood')
def Harwood():
	topass = []
	for suite in harwood:
		topass.append(repr(suite))
	length = len(harwood)
	return render_template('dorm.html',topass=topass,length=length)
@suitesetup.route('/Smiley')
def Smiley():
	topass = []
	for suite in smiley:
		topass.append(repr(suite))
	length = len(smiley)
	return render_template('dorm.html',topass=topass,length=length)
if __name__== '__main__':
	suitesetup.run(debug=True)















