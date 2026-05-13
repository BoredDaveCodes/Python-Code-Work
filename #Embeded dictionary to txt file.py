#Embeded dictionary to txt file
#Author: Dave Muton

food = {1: {
            "Food":"Pepsi Max",
            "Cost":"£1.35",
            "Weight":"500ml",
            "Calories":"2kcal",
            "Carbohydrates":"0",
            "Total Fat":"0",
            "Cholesterol":"0",
            "Sodium":"0",
            "Potassium":"0",
            "Protein":"0",
            "Sugar":"0"
            },

        2: {
            "Food":"Dino Nuggies",
                "Cost":"£2.45",
                "Weight":"100g",
                "Calories":"258kcal",
                "Carbohydrates":"20.5g",
                "Total Fat":"14.0g",
                "Cholesterol":"0mg",
                "Sodium":"0.8g",
                "Potassium":"0mg",
                "Protein":"12.0g",
                "Sugar":"0g"
                },

        3: {
            "Food":"Batchelors Super Noodle Pots, Chicken",
                "Cost":"£1",
                "Weight":"75g",
                "Calories":"132kcal",
                "Carbohydrates":"17.5g",
                "Total Fat":"5.7g",
                "Cholesterol":"0mg",
                "Sodium":"0.8g",
                "Potassium":"0mg",
                "Protein":"12.0g",
                "Sugar":"0g"
                }
        }
with open("food_nutrition.txt", "w") as f:
    for key, item in food.items():
        f.write("Item 1:"+food[1]+"\n")
        f.write("Item 2:"+food[2]+"\n")
        f.write("Item 3:"+food[3]+"\n")
        f.close()