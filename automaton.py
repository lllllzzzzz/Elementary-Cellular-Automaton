#!/usr/bin/python
 
import sys

def step(gen, rule_table):
    """Return the next step of automaton given a cell configuration."""
 
    gen = [0] + gen + [0]

    next_gen = []
    #print gen

    for i in xrange(1, len(gen) - 1):
        triple_bits = "".join(str(i) for i in gen[i - 1:i + 2])
        #print triple_bits, rule_table[triple_bits]
        #return [rule_table[triple_bits] for i in xrange(1, len(gen) - 1)]
        next_gen.append(rule_table[triple_bits])
        
    return next_gen[1:-1]

def compute_gens(rule, gen, steps):
    """Print N generations of Rule 90 with initial cell configuration."""

    #rule = bin(rule)[2:]
    rule = "0" * (8 - len(bin(rule)[2:])) + bin(rule)[2:]
    rule_table = dict()
    for i in xrange(0, 8):
        bits = "0" * (3 - len(bin(i)[2:])) + bin(i)[2:]
        #print bits
        #print int(rule[-i])
        rule_table[bits] = int(rule[i])

    print rule_table
   
    for i in xrange(0, steps):
        print_gen(gen)
        #print "".join(str(i) for i in gen)
        gen = [0] + step(gen, rule_table) + [0]

def print_gen(gen):
    """Print generation of automaton given a cell configuration."""

    print "".join(["*" if i == 1 else " " for i in gen])
 
def main():
    if len(sys.argv) != 4 or not (sys.argv[1] + sys.argv[2]).isdigit():
        print "Usage:", sys.argv[0], "[width] [steps]"
        sys.exit(0)
 
    rule = int(sys.argv[1])
    init_gen = [int(i) for i in sys.argv[2]]
    steps = int(sys.argv[3])
    compute_gens(rule, init_gen, steps)
 
if __name__ == "__main__":
    main()
