#Getting candidates names for the club
from pyscript import display, document


def get_name(e):
    document.getElementById('div1').innerHTML = ' '
    f_name = document.getElementById('fname').value
    l_name = document.getElementById('lname').value
    First_ruby_students = ['prinze', 'maria', 'lindsay', 'joaquin', 'lucian'] #list of first names
    Last_ruby_students = ['alminario', 'agatha', 'esguerra', 'tabije', 'veran'] #list of last names

    first_name = document.getElementById('fname').value.lower() #display the name in lower case
    last_name = document.getElementById('lname').value.lower() #display the name in lower case 2
    name_checker = first_name in First_ruby_students and last_name in Last_ruby_students
    display_message = ('Sorry, your name is not in this list', f'{first_name} {last_name} Congrats on getting in this list!') #message to be displayed

    display(display_message[name_checker], target = 'div1') #display message in the div1