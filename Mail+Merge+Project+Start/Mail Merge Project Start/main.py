#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open('./Input/Names/invited_names.txt', mode='r') as f:
    data = f.read()

data = data.split('\n')

with open('./Input/Letters/starting_letter.txt', mode='r') as f:
    template = f.read()

for person in data:
    with open(f'./Output/ReadyToSend/Letter_for_{person}.txt', mode='w') as f:
        new_template = template.replace('[name]', person)
        f.write(new_template)