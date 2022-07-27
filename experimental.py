from qudiet.core import backend
from src.qudiet.qasm.qasm_parser import parse_qasm
import argparse, glob, pickle, warnings, time

def arguments():
    description = '''
    Runs all the qasm circuit present in a file, and
    saves a copy of the result in the same directory
    '''
    epilog = '''
    Example : python3 experimental.py -b numpy testbench/tof_qutrit/
      [OR]
    Example : python3 experimental.py -b sparse testbench/tof_full/
    '''

    # Initialize parser
    parser = argparse.ArgumentParser(description=description, epilog=epilog)

    # Adding optional argument
    parser.add_argument("-m", "--mode", help = "Selects the mode of action. [pkl,txt]", default='txt')
    parser.add_argument("-b", "--backend", help = "Selects the backend. [sparse, numpy, cuda, sparse-cuda]", default='sparse')
    parser.add_argument('-v', '--verbose', action='count', default=0)
    parser.add_argument("path", help = "path of files", default='./')

    # Read arguments from command line
    args = parser.parse_args()

    operator = args.mode
    path = args.path
    verbose = args.verbose

    backend = args.backend
    suffix = "" + args.backend + ""

    if backend not in ["sparse", "numpy", "cuda", "sparse-cuda"]:
        raise Exception(f"Backend {backend} not found.")

    if backend == "sparse":
        from src.qudiet.core.backend.SparseBackend import SparseBackend
        print("[i] Using Sparse Backend")
        backend = SparseBackend
    elif backend == "numpy":
        from src.qudiet.core.backend.NumpyBackend import NumpyBackend
        print("[i] Using Numpy Backend")
        backend = NumpyBackend
    elif backend == "cuda":
        from src.qudiet.core.backend.CUDABackend import CUDABackend
        print("[i] Using Cuda Backend")
        backend = CUDABackend
    elif backend == "sparse-cuda":
        from src.qudiet.core.backend.CUDASparseBackend import CUDASparseBackend
        print("[i] Using Sparse Cuda Backend")
        backend = CUDASparseBackend

    return operator, path, verbose, backend, suffix

def main():
    operate_on, directory_path, verbose, backend, suffix = arguments()
    directory_path += "/**/*."+operate_on

    files = glob.glob(directory_path, recursive = True)

    if operate_on in ["txt", "qasm"]:
        for file in files:
            try:
                start = time.time()
                qc = parse_qasm(file, backend=backend)
                load = time.time()
                result = qc.run()
                end = time.time()

                result = {
                    'value': result,
                    'config': qc.get_circuit_config(),
                    'loading-time': load-start,
                    'execution-time': end-load,
                }

                output = file[:-3]+suffix+'.pkl'

                with open(output, "wb") as out_file:
                    pickle.dump(result, out_file)

                if verbose:
                    print(f"[o] File '{file}' ran successfully. Result saved in {output}...")

                print(f"[o] Result for file '{file}' \n[o]\t{result}\n[o]")

            except Exception as e: #IndexError as ie:
                # result = ie.args
                # warnings.warn(f"[x] File '{file}' got exception '{e}'...")
                print(f"[x] File '{file}' got exception '{e}'...\n[x]")
    elif operate_on in ["pkl", "pickle"]:
        for file in files:
            with open(file, "rb") as out_file:
                result = pickle.load(out_file)
                print(f"[o] Result '{file}' found. \n[o]\t{result}\n[o]")
    pass

# operate_on = "pkl"
# directory_path = "testbench/tof_qutrit" + "/**/*."+operate_on

# files = glob.glob(directory_path, recursive = True)

# if operate_on == "txt":
#     for file in files:
#         print(file)
#         try:
#             result = parse_qasm(file).run()
#         except IndexError as ie:
#             result = ie.args
#         with open(file[:-3]+'pkl', "wb") as out_file:
#             pickle.dump(result, out_file)

# elif operate_on == "pkl":
#     for file in files:
#         with open(file, "rb") as out_file:
#             result = pickle.load(out_file)
#             print(result)

if __name__ == '__main__':
    main()