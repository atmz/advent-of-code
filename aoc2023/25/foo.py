
import sys; sys.dont_write_bytecode = True; from util import *

def do_case(inp: str, sample=False):
    def sprint(*a, **k): sample and print(*a, **k)

    from pyvis.network import Network

    nodes = set()
    
    net = Network(notebook=True)
    for line in inp.splitlines():
        source, dest = line.split(':')
        dests = dest.split()
        if source not in nodes:
            net.add_node(source)
            nodes.add(source)
        for d in dests:
            if d not in nodes:
                net.add_node(d)
                nodes.add(d)
            net.add_edge(source, d)

    net.show("example.html")
    return  # RETURNED VALUE DOESN'T DO ANYTHING, PRINT THINGS INSTEAD


run_samples_and_actual([
# Part 1
r"""jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr
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

