import glob
import pickle
from src.framework.qasm.qasm_parser import parse_qasm

operate_on = "pkl"
directory_path = "testbench/tof_qutrit" + "/**/*."+operate_on

files = glob.glob(directory_path, recursive = True)

if operate_on == "txt":
    for file in files:
        print(file)
        try:
            result = parse_qasm(file).run()
        except IndexError as ie:
            result = ie.args
        with open(file[:-3]+'pkl', "wb") as out_file:
            pickle.dump(result, out_file)

elif operate_on == "pkl":
    for file in files:
        with open(file, "rb") as out_file:
            result = pickle.load(out_file)
            print(result)
