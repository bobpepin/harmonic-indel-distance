#!/bin/bash
## SBATCH --job-name=PairwiseDistance
## SBATCH --ntasks=4
## SBATCH --array=1-4
#SBATCH --gpus=0

echo "NODELIST=${SLURM_NODELIST}"

module load python/3.11.3
source ~/python-venv/python3.11/bin/activate

echo "Task ID: ${SLURM_ARRAY_TASK_ID}"
ARGS=`head -n ${SLURM_ARRAY_TASK_ID} args.txt | tail -1`
echo python3 pairwise_distances.py ${ARGS}
python3 pairwise_distances.py ${ARGS}