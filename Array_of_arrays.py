food_groups = [
  ["apple", "orange", "grape", "tangerine"], 
  ["chicken", "steak", "fish"], 
  ["wheat", "oatmeal", "rice"], 
  ["spinach", "lettuce", "corn"],  
   
   
   
    ]
for food_group in food_groups:
    for food_item in food_group:
        print(f"The {food_item} is in the {food_group} group.")


food_groups.clear()
print(food_groups)