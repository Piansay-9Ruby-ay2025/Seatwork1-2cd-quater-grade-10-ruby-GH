# working with Lists
from pyscript import document
country = ("Brunei", "Cambodia", "Indonesia", "Laos", "Malaysia", "Singapore", "Timor-Leste","Vietnam")
nickname = ("The Land of Unexpected Treasures","Kingdom of Wonder", "The Emerald of the Equator", "The Land of a Million Elephants","The Land of Diversity","The Lion City", "The Land of the Sleeping Crocodile","The Land of the Blue Dragon")

# Functions
def show_name(e):
    chosen_east_country = document.getElementById("country").value

    best_best_nickname = nickname[int(chosen_east_country)]

    document.getElementById("result").innerText = best_best_nickname