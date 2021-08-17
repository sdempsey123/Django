from django.shortcuts import render, redirect
# add redirect to give views file a place to redirect
import random
# Create your views here.
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    # Need session variable that will last and persist, make a key of gold with value at 0. Migrate
    if 'activities' not in request.session:
        request.session['activities'] = []
    return render(request, "index.html")

def process_money(request):
    print("The form has been submitted!")
    print(request.POST)
    # have this line for POST routes
    
    if request.POST['building'] == 'farm':
        # I want building because it was used on my form in html
        num = random.randint(10,20)
        request.session['gold'] += num
        # Now we can use the variable, look for outside source for random.randint 
    # With building in all of the forms, we can keep asking questions (below)
        request.session['activities'].append("You earned  " + str(num) + "! Yay!")
    elif request.POST['building'] == 'cave':
        num = random.randint(5,10) 
        request.session['gold'] += num
        request.session['activities'].append("You earned  " + str(num) + "! Yay!") 
    elif request.POST['building'] == 'house':
        num = random.randint(2,5) 
        request.session['gold'] += num
        request.session['activities'].append("You earned  " + str(num) + "! Yay!") 
    elif request.POST['building'] == 'casino':
        num = random.randint(-50, 50)
        request.session['gold'] += num
        if num > 0:
            request.session['activities'].append("You earned  " + str(num) + "! Yay!")
        elif num == 0:
            request.session['activities'].append("You earned nothing!")
        else:
            request.session['activities'].append("You lost  " + str(abs(num)) + "! Boooo!")   

        
    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')

    # Having problems getting the top number in html to change
    # Needed to make an if statement on Line 8 to get the top number to change