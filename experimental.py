from xmlrpc.client import boolean
from rich.console import Console
from qudiet.core import backend
from src.qudiet.qasm.qasm_parser import parse_qasm
import argparse, glob, pickle, warnings, time
import pprint

console = Console()


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
    parser.add_argument("-m", "--mode", help = "Selects the mode of action. [pkl,txt,qasm]", default='txt')
    parser.add_argument("-b", "--backend", help = "Selects the backend. [sparse, numpy, cuda, sparse-cuda]", default='sparse')
    parser.add_argument('-v', '--verbose', action='count', default=0)
    parser.add_argument('-t', '--terminal', type=boolean, default=False)
    parser.add_argument("path", help = "path of files", default='./')

    # Read arguments from command line
    args = parser.parse_args()

    operator = args.mode
    path = args.path
    verbose = args.verbose
    terminal = args.terminal

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

    return operator, path, verbose, backend, suffix, terminal

def main():
    operate_on, directory_path, verbose, backend, suffix, terminal = arguments()
    directory_path += "/**/*."+operate_on

    files = glob.glob(directory_path, recursive = True)
    console.print(f"Analyzing {files} files...")

    if operate_on in ["txt", "qasm"]:
        for file in files:
            display = f"[bold green]Working on {file}..."
            if terminal:
                with console.status(display) as status:
                    routine(file, backend, suffix, verbose)
            else:
                console.print(display)
                routine(file, backend, suffix, verbose)


    elif operate_on in ["pkl", "pickle"]:
        for file in files:
            with open(file, "rb") as out_file:
                result = pickle.load(out_file)
                console.print(f"[o] Result '{file}' found. \n[o]\t{result}\n[o]")
    pass

def routine(file, backend, suffix, verbose):
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

        output = ".".join(file.split(".")[:-1])+"-"+suffix+'.pkl'

        with open(output, "wb") as out_file:
            pickle.dump(result, out_file)

        console.print(f"[bold yellow]---->[white] Result for file [bold green]'{file}': ", result)

        if verbose:
            console.print(f"[bold]saved in [purple]{output}\n")

    except Exception as e: #IndexError as ie:
        # result = ie.args
        # print(f"[x] File '{file}' got exception '{e}'...")
        warnings.warn(f"[x] File '{file}' got exception '{e}'...")
        console.print(f"[bold red][x][white] File [bold green]'{file}'[white] got exception '{e}'...\n[x]")

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