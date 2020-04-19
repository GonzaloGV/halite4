from kaggle_environments import make, evaluate

env = make('halite', debug=True)

env.run(['bot.py', 'bot.py'])
with open('run.html', 'w') as file:
    file.write(env.render(mode='html', width=400, height=300))