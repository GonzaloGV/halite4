from kaggle_environments import make, evaluate

env = make('halite', debug=True)

env.run(['bot.py', 'bot.py'])
env.render(mode='ipython', width=400, height=300)