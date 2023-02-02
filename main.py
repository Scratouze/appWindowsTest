# Test exercices @Scratouze 2023

from myBank.repository.dataBase_util import createDB
from utils.appController import container


createDB()
container.mainloop()
