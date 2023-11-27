#Modulo Operator
FirstName = 'Angela'
LastName = 'Teyvi'
EmailSubject = 'Welcome to the team'

#single variable in string literal
#print('Hello, %s' % FirstName)

b = 'Hello, Miss %s \n %s! '% (LastName, EmailSubject)
#print(b)

#using dictionaries
#print('Hello, %(LastName)s \n%(EmailSubject)s' % {'LastName':'Teyvi','EmailSubject': 'Welcome to the team'})

#using str.format()
#print('Hello, {}! \n{}'.format(LastName, EmailSubject))

#using positions
#print('Hello, {1} \n{0}'.format(EmailSubject, FirstName))

#print("Balance: ${:.2f}".format(5425.9292))
#print("{:=^30}".format("Centered string"))

print(f'Hello, {LastName} \n{EmailSubject.upper()}')