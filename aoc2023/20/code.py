import sys; sys.dont_write_bytecode = True; from util import *
from  heapq import heappush, heappop

class Module:
    def __init__(self, string):
        self.memory = None
        self.memory_last_on = defaultdict(int)
        self.memory_cycle_on = defaultdict(int)
        self.last_on = None
        self.last_off = None
        self.cycle_on = None
        self.cycle_off = None
        description, destinations = string.split(' -> ')
        self.destinations = [d.strip() for d in destinations.split(",")]
        if description[0] == '&':
            self.type = 'conjunction'
            self.memory = {}
        elif description[0] == '%':
            self.type = 'flipflop'
            self.memory = False
        elif description == 'broadcaster':
            self.type = 'broadcaster'
        else:
            assert False, description
        self.label =description.strip("&%")
    
    def add_input(self, input):
        if self.type == 'conjunction':
            self.memory[input] = False
    
    def print(self):
        print(f"{self.label} - {self.type} - D:{self.destinations} - M:{self.memory}")
        print(f"{self.label} - ON: {self.cycle_on} - OFF:{self.cycle_off}")
        print(f"{self.label} - ON: {self.memory_cycle_on}")
        print(f"{self.label} - ON: {math.lcm(*self.memory_cycle_on.values())}")

    
    def process(self, pulse, input, i): # False if low, True if high
        if self.type == 'broadcaster':
            return [(self.label, d, pulse) for d in self.destinations]    
        if self.type == 'flipflop':
            if pulse:
                return []
            else:
                self.memory = not self.memory
                if self.memory: # just turned on
                    if self.last_on:
                        self.cycle_on = i - self.last_on
                    self.last_on = i
                    return [(self.label, d, True) for d in self.destinations]
                else:
                    if self.last_off:
                        self.cycle_off = i - self.last_off
                    self.last_off = i
                    return [(self.label, d, False) for d in self.destinations]
        if self.type == 'conjunction':
            if not self.memory[input] and pulse:
                self.memory_cycle_on[input] = i-self.memory_last_on[input]
                self.memory_last_on[input] = i
            self.memory[input] = pulse
            
            if all(self.memory.values()):
                return [(self.label, d, False) for d in self.destinations]
            else:
                return [(self.label, d, True) for d in self.destinations]
        assert False, (f"{self.label} - {self.type} - D:{self.destinations} - M:{self.memory}", pulse, input)

def do_case(inp: str, sample=False):
    def sprint(*a, **k): sample and print(*a, **k)

    # Part 1
    lines = inp.splitlines()
    modules = {}
    for line in lines:
        module = Module(line)
        modules[module.label] = module
    for m in modules.values():
        for d in m.destinations:
            if d in modules:
                modules[d].add_input(m.label)
    low=0
    high=0
    for i in range(0,100000000):
        pulses = [('button','broadcaster', False)]
        while len(pulses)>0:
            pulse = pulses.pop(0)
            if pulse[2]:
                high+=1
            else:
                low+=1
            if pulse[1] == 'rx' and pulse[2] == False:
                print(f"Part 2: {i+1}")
                print(i+1)
                return
            if pulse[1] not in modules:
                pass
            else:
                new_pulses = modules[pulse[1]].process(pulse[2], pulse[0], i)
                # for new_pulse in new_pulses:
                #     print(f"{new_pulse[0]} -{new_pulse[2]}-> {new_pulse[1]}")
                pulses+=new_pulses

        #print(f"{i}: {low}*{high}={low*high}")
        if(i % 100) == 0:
            print(i)
            modules['gj'].print()
        if(i==999):
            print(f"Part 1: {low}*{high}={low*high}")


    

        
        






                


    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD


run_samples_and_actual([
# Part 1
r"""
""",
    r"""

""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

"""],[
# Part 2
r"""
""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

""",r"""

"""], do_case)

