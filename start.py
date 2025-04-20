import help_funcs
import strategy
import search_win
import asyncio
from threading import Thread


help_funcs.create_space()
if not(help_funcs.is_strat_created()):
    strategy.write_strategy()

Strategy1 = search_win.WIN()


while Strategy1.work:
    Strategy1.check_win()
    Strategy1.antibot()
