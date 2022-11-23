from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from .forms import BreakfastForm
from .models import Contact , Breakfast , Lunch , Dinner
import random

class Food(object):

	def __init__(self, meal_type, name, amount, calories):
		self.meal_type = meal_type
		self.name = name
		self.amount = amount
		self.calories = int(calories)

# Home page 
def index(request):
    return render(request,'MyApp/index.html')

# BMI calculator page 
def bmi(request):
    return render(request,'MyApp/bmi.html')


# Diet Plan page 
def dietplan(request):
    if request.method == 'POST':
        # Get all details from the user 
        resp_weight =int(request.POST['weight'])
        resp_height = int(request.POST['height'])
        resp_age = int(request.POST['age'])
        resp_gender = request.POST['gender']    
        resp_al = request.POST['activity_level']
        resp_bodyTarget = request.POST['bodyTarget']

        # Calculate BMR according to user information 
        if resp_gender == 'm':
            BMR = (10 * resp_weight ) + (6.25 * resp_height) - (5 * resp_age) + 5
        else: 
            BMR = (10 * resp_weight) + (6.25 * resp_height) - (5 * resp_age) - 161

        # Verify the accuracy of the information the user has provided. 
        if BMR <= 0:
            context=dict()
            context["msg"]="Invalid data! Please enter correct data."

            return render(request,'MyApp/dietplan.html',context=context)

        # BMR calculated based on exercise type 
        if resp_al == 'S':
            minBMR,maxBMR = BMR * 1,BMR * 1.2
        elif resp_al == 'L':
            minBMR,maxBMR = BMR * 1.2,BMR * 1.375
        elif resp_al == 'M':
            minBMR,maxBMR = BMR * 1.375,BMR * 1.550
        elif resp_al == 'V':
            minBMR,maxBMR = BMR * 1.550,BMR * 1.725
        elif resp_al == 'E':
            minBMR,maxBMR = BMR * 1.725,BMR * 1.900
        

        # BMR calculated based on user target weight
        minBMR = minBMR * eval(resp_bodyTarget)
        maxBMR = maxBMR * eval(resp_bodyTarget)

        # BMR divided for Breakfast, Lunch and Dinner 
        min_breakfast_calories = 0.12 * minBMR 
        max_breakfast_calories = 0.12 * maxBMR

        min_lunch_calories = 0.44 * minBMR 
        max_lunch_calories = 0.44 * maxBMR

        min_dinner_calories = 0.44 * minBMR 
        max_dinner_calories = 0.44 * maxBMR

        try : 
            
            get_all_breakfast_items = Breakfast.objects.filter(calories__gte=min_breakfast_calories,calories__lte=max_breakfast_calories)
            # Check if any food items with specified calorie requirement exist in database 
            if get_all_breakfast_items.exists():
                breakfast_item = random.choice(get_all_breakfast_items) 
            else:
                avg_breakfast_calories = (min_breakfast_calories+max_breakfast_calories)//2
                breakfast_item = Food("Breakfast","Food item","Calories: " + str(avg_breakfast_calories)+ " /",avg_breakfast_calories) 


            get_all_lunch_items = Lunch.objects.filter(calories__gte=min_lunch_calories,calories__lte=max_lunch_calories)
            # Check if any food items with specified calorie requirement exist in database 
            if get_all_lunch_items.exists():
                lunch_item = random.choice(get_all_lunch_items) 
            else:
                avg_lunch_calories = (min_lunch_calories+max_lunch_calories)//2
                lunch_item = Food("Lunch","Food item","Calories: " + str(avg_lunch_calories) + " /",avg_lunch_calories) 

            
            get_all_dinner_items = Dinner.objects.filter(calories__gte=min_dinner_calories,calories__lte=max_dinner_calories)
            # Check if any food items with specified calorie requirement exist in database 
            if get_all_dinner_items.exists():
                dinner_item = random.choice(get_all_dinner_items) 
            else:
                avg_dinner_calories = (min_dinner_calories+max_dinner_calories)//2
                dinner_item = Food("Dinner","Food item","Calories: " + str(avg_dinner_calories)+ " /",avg_dinner_calories) 

            context = {}
            context["BreakfastName"] = Food("Breakfast", breakfast_item.name, breakfast_item.amount, breakfast_item.calories)
            context["LunchName"] = Food("Lunch", lunch_item.name, lunch_item.amount, lunch_item.calories)
            context["DinnerName"] = Food("Dinner", dinner_item.name, dinner_item.amount, dinner_item.calories)
            context["BCal"] = breakfast_item.calories
            context["LCal"] = lunch_item.calories
            context["DCal"] = dinner_item.calories
        except : 
            context=dict()
            context["msg"]="Error occured while making the diet plan."
            return render(request,'MyApp/dietplan.html',context=context)
        
        # Show the dietplan 
        return render(request,"MyApp/show.html",context=context)

    # Get user information for getting a dietplan 
    return render(request,'MyApp/dietplan.html')

# Contact Us page
@csrf_protect
def contactus(request):
    if request.method == 'POST':
        resp_name = request.POST['user_name']
        resp_email = request.POST['email']
        resp_message = request.POST['message']
        contact = Contact()
        contact.user_name = resp_name
        contact.email = resp_email
        contact.msg = resp_message
        contact.save()

        return render(request,'MyApp/thankyou.html')
    else:
        return render(request,'MyApp/contact.html')