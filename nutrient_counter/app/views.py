from django.shortcuts import render, redirect
from .models import Food, Consume, HealthGoal
from django.http import JsonResponse
from .forms import FoodForm, HealthGoalForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

def page_view(request):
    return render(request, 'landing_page.html')

@login_required
def index(request):
    if request.method == 'POST':
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        consume = Consume(user=user, food_consumed=consume)
        consume.save()

        # Redirect to the same page to prevent duplicate form submissions
        return redirect('index')  # Ensure 'index' is the name of your URL pattern

    foods = Food.objects.all()
    consumed_food = Consume.objects.filter(user=request.user)

    return render(request, 'index.html', {'foods': foods, 'consumed_food': consumed_food})



def delete_consume(request, id):
    consumed_food = Consume.objects.get(id=id)
    if request.method=="POST":
        consumed_food.delete()
        return redirect('/')
    return render(request, 'delete.html')



def nutrient_data(request):
    consumed = Consume.objects.filter(user=request.user)
    data = {
        "carbs": sum(c.food_consumed.carbs for c in consumed),
        "proteins": sum(c.food_consumed.proteins for c in consumed),
        "fats": sum(c.food_consumed.fats for c in consumed),
        "calories": sum(c.food_consumed.calories for c in consumed),
    }
    return JsonResponse(data)





@login_required
def chart_data(request):
    consumed = Consume.objects.filter(user=request.user)
    goal, _ = HealthGoal.objects.get_or_create(user=request.user)

    data = {
        "labels": [c.food_consumed.name for c in consumed],
        "carbs": [c.food_consumed.carbs for c in consumed],
        "proteins": [c.food_consumed.proteins for c in consumed],
        "fats": [c.food_consumed.fats for c in consumed],
        "calories": [c.food_consumed.calories for c in consumed],
        "goal_carbs": goal.carb_goal,
        "goal_proteins": goal.protein_goal,
        "goal_fats": goal.fat_goal,
        "goal_calories": goal.daily_calorie_goal,
    }
    return JsonResponse(data)







def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})




from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("index")  # Redirect to homepage or dashboard
    else:
        form = AuthenticationForm()
    
    return render(request, "login.html", {"form": form})





def logout_view(request):
    logout(request)
    return redirect("login")






def add_food(request):
    if request.method == "POST":
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()  # Saves the food to the global registry
            return redirect("index")  # Redirects back to the homepage
    else:
        form = FoodForm()
    return render(request, "add_food.html", {"form": form})







@login_required
def update_goals(request):
    goal, created = HealthGoal.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = HealthGoalForm(request.POST, instance=goal)
        if form.is_valid():
            form.save()
            return redirect("index")
    else:
        form = HealthGoalForm(instance=goal)
    return render(request, "update_goals.html", {"form": form})
