
def replacestrBlank(strToUpdate,old,new):
	"""
    This function take 3 parameters string and two sub string and use replace method 
	to replace old value by new value and return the new string
	"""
	return strToUpdate.replace(old, new)
	
	
	



def easy(questionStr,answer,current_question_number):
	"""
        This function take 3 parameters: string with blanks to fill and string with the correct answer ,variable of current_question_number and when user answer correct will call function to replace the blank and print correct with replaced blank else will ask him to try again
	"""
	print questionStr +"\n"
	replacedList=[questionStr]
	index=0
	while current_question_number < len(answer) :
		print "\n"
		user_input=raw_input('what should be substituted in for _'+str(current_question_number+1)+'_ ? ')
		if user_input.lower() == answer[current_question_number]:
			updatedStr=replacestrBlank(replacedList[index], '_'+str(current_question_number+1)+'_', user_input)
			print "\n" +"Correct ^___^" +"\n \n" +updatedStr
			replacedList.append(updatedStr)
			index +=1
			current_question_number += 1
		else :
			print "Try Again"		
	print "\n"+"\n  Congratulations, you have successfully finished the level  ^___^"
		    


def med(questionStr,answer,current_question_number):
	"""
        This function take 3 parameters: string with blanks to fill and string with the correct answer ,variable of current_question_number and when user answer correct will call function to replace the blank and print correct with replaced blank else will ask him to try again
	"""
	print questionStr +"\n"
	replacedList=[questionStr]
	index=0
	while current_question_number < len(answer) :
		print "\n"
		user_input=raw_input('what should be substituted in for _'+str(current_question_number+1)+'_ ? ')
		if user_input.lower() == answer[current_question_number]:
			updatedStr=replacestrBlank(replacedList[index], '_'+str(current_question_number+1)+'_', user_input)
			print "\n" +"Correct ^___^" +"\n \n" +updatedStr
			replacedList.append(updatedStr)
			index +=1
			current_question_number += 1
		else :
			print "Try Again"		
	print "\n"+"\n  Congratulations, you have successfully finished the level ^___^"



     
def hard(questionStr,answer,current_question_number):
	"""
        This function take 3 parameters: string with blanks to fill and string with the correct answer ,variable of current_question_number and when user answer correct will call function to replace the blank and print correct with replaced blank else will ask him to try again
	"""
	print questionStr +"\n"
	replacedList=[questionStr]
	index=0
	while current_question_number < len(answer) :
		print "\n"
		user_input=raw_input('what should be substituted in for _'+str(current_question_number+1)+'_ ? ')
		if user_input.lower() == answer[current_question_number]:
			updatedStr=replacestrBlank(replacedList[index], '_'+str(current_question_number+1)+'_', user_input)
			print "\n" +"Correct ^___^" +"\n \n" +updatedStr
			replacedList.append(updatedStr)
			index +=1
			current_question_number += 1
		else :
			print "Try Again"		
	print "\n"+"\n Congratulations, you have successfully finished the level ^___^"


    
    

	

def menu():
	"""
    This function munu function store questions and answers in lists and send the appropriate value index to functions after ask the user to choose the level to play 
	"""
	qusList=['Sky Color is: _1_  ,Leaves Color is: _2_ , Ocean Color is : _1_  , Milk Color is : _3_ , Tomato Color is: _4_','  This _1_ is about  proteins consists of three chapters, the first _2_ talks about the importance of _3_, the second _2_ talks _4_ the sources of _3_, the third _2_ talks _4_ the amount of daily requirement of _3_',
   " To _1_ good health, to _2_ true happiness to one's family, to _2_ peace to all, one must first discipline and control one's own _3_. If a man can control his _3_ he can find the way to Enlightenment, and all wisdom and virtue will naturally come to _4_."]
	print "" +"\n"
	answer=[['blue','green','white','red'],['book','chapter','proteins','about'],['enjoy','bring','mind','him']]
	current_question_number=0
	list_first_index=0
	list_second_index=1
	list_third_index=2
# Variable to store the value of the level chosen by the user
	level = raw_input('Enter easy For Easy Level, med For Intermediate Level , hard For Hard Level :')

# if statement for each level and if user enter wrong  input
	
	if level.lower() == 'easy':
		print "\n"
		easy(qusList[list_first_index],answer[list_first_index],current_question_number)
		
	elif level.lower() == 'med':
		print "\n"
		med(qusList[list_second_index],answer[list_second_index],current_question_number)
		
	elif level.lower() == 'hard':
		print "\n"
		hard(qusList[list_third_index],answer[list_third_index],current_question_number)
			
	else :
		print "wrong  Input Try Again"
		menu()


print "Hello In Made Lib"
print " "
menu()
