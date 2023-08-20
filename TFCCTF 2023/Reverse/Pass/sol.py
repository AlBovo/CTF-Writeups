#!/usr/bin/env python3
import angr

proj = angr.Project("./src")
win, lose = 0x4019B3, 0x401984
init = proj.factory.entry_state()
sim = proj.factory.simulation_manager(init)
s = sim.explore(find=win, avoid=lose)

print(s.found[0].posix.dumps(0).decode() + "}", end="")