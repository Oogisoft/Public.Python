import sqlite3, sys, re, random,pprint

#regex pattern for meals
meal_pattern = re.compile(r'(.*):(.*)')

conn = sqlite3.connect('meal_and_ingredients_FIN.db', isolation_level=None)

#commands to make table
conn.execute('CREATE TABLE IF NOT EXISTS meals (row_id INTEGER PRIMARY KEY, name TEXT NOT NULL) STRICT')
conn.execute('CREATE TABLE IF NOT EXISTS ingredients (name TEXT, meal_id INTEGER, FOREIGN KEY(meal_id) REFERENCES meals (row_id))STRICT')

#print tables inside of db
#conn.execute('SELECT name FROM sqlite_schema WHERE type="table"')

#Inventory of DB Print
def show_tables():
    print('Current Meals:')
    pprint.pprint(conn.execute('SELECT * FROM meals').fetchall())
    print('')
    print('Current Ingredients:')
    pprint.pprint(conn.execute('SELECT * FROM ingredients').fetchall())
    print('')

while True:
    prompt1 = input('''Welcome to your Meal Database, see your options:
    A. Add a Meal to DB (Type "meal:ingredient1,ingredient2")
    B. Find Meal (Type "FIND MEAL")
    C. Show current tables (Type "TABLES")
    D. To exit (Type "Quit")
    ...GO:\n''')
    if prompt1.upper() == 'QUIT':
        print(conn.execute('SELECT * FROM meals').fetchall())
        print(conn.execute('SELECT * FROM ingredients').fetchall())
        sys.exit('Goodbye')
    elif prompt1.upper() == 'TABLES':
        show_tables()
    elif prompt1.upper() == 'FIND MEAL':
        prompt2 = input('''DO you want to do something else?:
    A. Type a meal name and I'll find its ingredients
    B. Type an ingredient and I'll find the meals that use it
    ....GO:\n''')
        meal_name = prompt2.lower()
        meal_check = conn.execute(f'SELECT * FROM meals WHERE name=?', (prompt2.lower(),)).fetchone()
        if meal_check:
            print(f'Match found for Meal: {prompt2}')
            for row in conn.execute(f'SELECT * FROM meals WHERE name=?', (prompt2.lower(),)):
                ingredient_list = conn.execute(f'SELECT * FROM meals INNER JOIN ingredients ON meals.row_id = ingredients.meal_id WHERE meals.name=?', (row[1],)).fetchall()
                print(f'Ingredients for your {prompt2}:')
                for ingredient in ingredient_list:
                    print(f'{ingredient[2]}')
            print(f'..\n...\nDone, do something else?\n\n')
        else:
            print(f'Match found for your Ingredient: {prompt2}')
            for row in conn.execute(f'SELECT * FROM ingredients WHERE name=?', (prompt2.lower(),)):
                meal = conn.execute(f'SELECT * FROM ingredients INNER JOIN meals ON meals.row_id = ingredients.meal_id WHERE ingredients.name=?', (row[0],)).fetchall()
                print(f'Meals with those ingredients:')
                for meal_name in meal:
                    print(meal_name[3])
            print(f'..\n...\nDone, do something else?\n\n')
    else:
        for groups in meal_pattern.findall(prompt1.lower()):
            meal_id = random.randint(10000, 99999)
            meal = str(groups[0]).lower()
            conn.execute(f'INSERT INTO meals VALUES (?,?)', (meal_id, meal))
            ingredients = groups[1].split(',')
            for ingredient in ingredients:
                conn.execute(f'INSERT INTO ingredients VALUES (?,?)', (ingredient.strip().lower(), (meal_id)))
            print('Meal: ' + meal + ' succesfully added to DB, unique_id = ' + str(meal_id))
            print(f'..\n...\nDone, do something else?\n\n')