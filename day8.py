from setup import get_input_file_path
from typing import List, Dict, FrozenSet

sample_data = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""

def decode_simple(data: List[List[str]]) :
    count = 0
    for quad in data:
        for digit in quad:
            if len(digit) == 2:
                count += 1
            elif len(digit) == 3:
                count += 1
            elif len(digit) == 4:
                count += 1
            elif len(digit) == 7:
                count += 1

    return count


def decode(display: List[str]) -> Dict[FrozenSet[str], int]:
    cryptex = {}
    rosetta = {}

    for digit in display:
        code = frozenset(digit)
        if len(digit) == 2:
            cryptex[code] = 1
            rosetta[1] = code
        elif len(digit) == 3:
            cryptex[code] = 7
        elif len(digit) == 4:
            cryptex[code] = 4
            rosetta[4] = code
        elif len(digit) == 7:
            cryptex[code] = 8

    for digit in display:
        code = frozenset(digit)
        if len(digit) == 5:
            if len(code.intersection(rosetta[1])) == 2:
                cryptex[code] = 3
            elif len(code.intersection(rosetta[4])) == 2:
                cryptex[code] = 2
            else:
                cryptex[code] = 5
        elif len(digit) == 6:
            if len(code.intersection(rosetta[1])) == 1:
                cryptex[code] = 6
            elif len(code.intersection(rosetta[4])) == 4:
                cryptex[code] = 9
            else:
                cryptex[code] = 0

    return cryptex


def sum_outputs(inputs: List[List[str]], outputs: List[List[str]]) -> int:
    output_total = 0
    for i in range(len(inputs)):
        multiplier = 1000
        cryptex = decode(inputs[i])
        for digit in outputs[i]:
            code = frozenset(digit)
            value = cryptex[code]
            output_total += (value * multiplier)
            multiplier //= 10

    return output_total


def main():
    input_file = get_input_file_path()
    with open(input_file) as f:
        lines_input = f.readlines()

        parsed_outputs = [line.split("|")[1].strip().split(" ") for line in lines_input]
        parsed_inputs = [line.split("|")[0].strip().split(" ") for line in lines_input]

        c1 = decode_simple(parsed_outputs)
        c2 = sum_outputs(parsed_inputs, parsed_outputs)
        print("part1:", c1, "\npart2:", c2)


if __name__ == "__main__":
    main()
