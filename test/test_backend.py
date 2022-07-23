import time
import warnings
from framework.core.quantum_circuit import QuantumCircuit
from framework.core.backend import CUDA_HOME


from framework.core.backend.NumpyBackend import NumpyBackend

def test_Numpy_backend():
    backend = NumpyBackend # 7.89 sec
    # backend = SparseBackend # 0.04 sec
    # backend = CUDABackend # 1.21 sec
    # backend = CUDASparseBackend # 0.43 sec

    qc = QuantumCircuit(
        qregs=[2, 2, 3, 3, 3, 2, 2, 2, 2, 2,], 
        init_states=[1, 1, 1, 0, 1, 0, 0, 0, 0,],
        backend=backend
    )

    qc.cx(acting_on=(0, 2), plus=1)
    qc.cx(acting_on=(2, 5), plus=1)
    qc.cx(acting_on=(0, 2), plus=2)
    # qc.cx(acting_on=(1, 2), plus=1)
    # qc.cx(acting_on=(2, 6), plus=1)
    # qc.cx(acting_on=(1, 2), plus=2)
    # qc.cx(acting_on=(0, 3), plus=1)
    # qc.cx(acting_on=(3, 7), plus=1)
    # qc.cx(acting_on=(0, 3), plus=2)
    # qc.cx(acting_on=(1, 3), plus=1)
    # qc.cx(acting_on=(3, 8), plus=1)
    # qc.cx(acting_on=(1, 3), plus=2)

    qc.measure_all()

    start_time = time.time()
    result = qc.run()
    end_time = time.time()

    warnings.warn(f"Time elapsed for numpy backend: {end_time - start_time}s")
    assert True

from framework.core.backend.SparseBackend import SparseBackend

def test_Sparse_backend():
    backend = SparseBackend # 0.04 sec
    # backend = NumpyBackend # 7.89 sec
    # backend = CUDABackend # 1.21 sec
    # backend = CUDASparseBackend # 0.43 sec

    qc = QuantumCircuit(
        qregs=[2, 2, 3, 3, 3, 2, 2, 2, 2, 2,], 
        init_states=[1, 1, 1, 0, 1, 0, 0, 0, 0,],
        backend=backend
    )

    qc.cx(acting_on=(0, 2), plus=1)
    qc.cx(acting_on=(2, 5), plus=1)
    qc.cx(acting_on=(0, 2), plus=2)
    # qc.cx(acting_on=(1, 2), plus=1)
    # qc.cx(acting_on=(2, 6), plus=1)
    # qc.cx(acting_on=(1, 2), plus=2)
    # qc.cx(acting_on=(0, 3), plus=1)
    # qc.cx(acting_on=(3, 7), plus=1)
    # qc.cx(acting_on=(0, 3), plus=2)
    # qc.cx(acting_on=(1, 3), plus=1)
    # qc.cx(acting_on=(3, 8), plus=1)
    # qc.cx(acting_on=(1, 3), plus=2)

    qc.measure_all()

    start_time = time.time()
    result = qc.run()
    end_time = time.time()

    warnings.warn(f"Time elapsed for sparse backend: {end_time - start_time}s")
    assert True

if CUDA_HOME:
    from framework.core.backend.CUDABackend import CUDABackend

    def test_CUDA_backend():
        backend = CUDABackend # 1.21 sec
        # backend = SparseBackend # 0.04 sec
        # backend = NumpyBackend # 7.89 sec
        # backend = CUDASparseBackend # 0.43 sec

        qc = QuantumCircuit(
            qregs=[2, 2, 3, 3, 3, 2, 2, 2, 2, 2,], 
            init_states=[1, 1, 1, 0, 1, 0, 0, 0, 0,],
            backend=backend
        )

        qc.cx(acting_on=(0, 2), plus=1)
        qc.cx(acting_on=(2, 5), plus=1)
        qc.cx(acting_on=(0, 2), plus=2)
        # qc.cx(acting_on=(1, 2), plus=1)
        # qc.cx(acting_on=(2, 6), plus=1)
        # qc.cx(acting_on=(1, 2), plus=2)
        # qc.cx(acting_on=(0, 3), plus=1)
        # qc.cx(acting_on=(3, 7), plus=1)
        # qc.cx(acting_on=(0, 3), plus=2)
        # qc.cx(acting_on=(1, 3), plus=1)
        # qc.cx(acting_on=(3, 8), plus=1)
        # qc.cx(acting_on=(1, 3), plus=2)

        qc.measure_all()

        start_time = time.time()
        result = qc.run()
        end_time = time.time()

        warnings.warn(f"Time elapsed for cuda backend: {end_time - start_time}s")
        assert True

    from framework.core.backend.CUDASparseBackend import CUDASparseBackend

    def test_CUDASparse_backend():
        backend = CUDASparseBackend # 0.43 sec
        # backend = CUDABackend # 1.21 sec
        # backend = SparseBackend # 0.04 sec
        # backend = NumpyBackend # 7.89 sec

        qc = QuantumCircuit(
            qregs=[2, 2, 3, 3, 3, 2, 2, 2, 2, 2,], 
            init_states=[1, 1, 1, 0, 1, 0, 0, 0, 0,],
            backend=backend
        )

        qc.cx(acting_on=(0, 2), plus=1)
        qc.cx(acting_on=(2, 5), plus=1)
        qc.cx(acting_on=(0, 2), plus=2)
        # qc.cx(acting_on=(1, 2), plus=1)
        # qc.cx(acting_on=(2, 6), plus=1)
        # qc.cx(acting_on=(1, 2), plus=2)
        # qc.cx(acting_on=(0, 3), plus=1)
        # qc.cx(acting_on=(3, 7), plus=1)
        # qc.cx(acting_on=(0, 3), plus=2)
        # qc.cx(acting_on=(1, 3), plus=1)
        # qc.cx(acting_on=(3, 8), plus=1)
        # qc.cx(acting_on=(1, 3), plus=2)

        qc.measure_all()

        start_time = time.time()
        result = qc.run()
        end_time = time.time()

        warnings.warn(f"Time elapsed for cuda-sparse backend: {end_time - start_time}s")
        assert True

