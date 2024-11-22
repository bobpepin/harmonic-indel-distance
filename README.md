This repository contains notebooks to fit support vector machines using harmonic edit distance and edit distance kernels. The notebooks are:
1. `FLIP1.ipynb` to solve a regression task on the FLIP thermostability dataset
2. `ncRNA2.ipynb` to solve a classification task for ncRNA data

Both notebooks are supported by command-line scripts to compute longest common subsequence matrices in parallel and on slurm clusters:
1. `pairwise_distances.py` computes a subset of the rows for a LCS matrix
2. `Assemble Distance Matrices.ipynb` assembles the submatrices computed by `pairwise_distances.py` into a LCS matrix
3. `slurm_generate_commands.py` and `pairwise_slurm.py` are helped scripts to run `pairwise_distances.py` in parallel on a slurm cluster

The scripts use the following datasets:
1. `FLIP1.ipynb` uses the data from `splits/meltome/splits.zip` in `https://github.com/J-SNACKKB/FLIP`. To be unzipped in a subdirectory `FLIP/meltome`.
2. `ncRNA2.ipynb` uses ncBench from `https://forge.ibisc.univ-evry.fr/ccreux/ncBench`. Git repository to be cloned into the root directory.