import pylcs
import multiprocessing
from tqdm import tqdm
import numpy as np
import sys
import click

@click.command
@click.option('--workers', default=4, help='Number of worker processes.')
@click.option('--batch_size', default=4, help='Batch size.')
@click.option("--start_offset", default=0, help="Start offset")
@click.option("--end_offset", default=None, help="End offset")
@click.argument("input_file")
@click.argument("output_file")
def main(input_file, output_file, workers=16, batch_size=4, start_offset=0, end_offset=None):
    with open(input_file) as fh:
        lines = [x.rstrip("\n") for x in fh.readlines()]
    if end_offset is None:
        end_offset = len(lines)
    else:
        end_offset = min(int(end_offset), len(lines))
    inputs = []
    for offset in range(start_offset, len(lines), batch_size):
        remaining = min(batch_size, end_offset - offset)
        if remaining <= 0:
            break
        kwargs = {"seqs": lines, "offset": offset, "count": remaining}
        inputs.append(kwargs)
    pool = multiprocessing.Pool(workers)
    results_it = pool.imap(compute_lcs_kwargs, inputs)
    blocks = []
    for result in tqdm(results_it, total=len(inputs)):
        blocks.append(result)
    lcs_matrix = np.vstack(blocks)
    # full_lcs_matrix = lcs_matrix + (lcs_matrix.T * (1-np.eye(lcs_matrix.shape[0])))
    np.save(output_file, lcs_matrix, allow_pickle=False)

def compute_lcs_kwargs(kwargs):
    return compute_lcs(**kwargs)

def compute_lcs(seqs, offset=0, count=1):
    if offset + count >= len(seqs):
        count = len(seqs) - offset
    lengths = np.array([len(x) for x in seqs])
    lcs_matrix = np.zeros((count, len(seqs)), dtype=int)
    for i in range(count):
        lcs_matrix[i, (i+offset):] = pylcs.lcs_sequence_of_list(seqs[offset+i], seqs[(offset+i):])
    return lcs_matrix

if __name__ == "__main__":
    main()