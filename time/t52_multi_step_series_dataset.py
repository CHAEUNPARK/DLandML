from numpy import array

def split_sequence(sequence, n_steps_in, n_steps_out):
    X, y = list(), list()
    for i in range(len(sequence)):
        end_ix = i + n_steps_in
        out_end_ix = end_ix + n_steps_out
        if out_end_ix > len(sequence):
            break
        seq_x, seq_y = sequence[i:end_ix], sequence[end_ix: out_end_ix]
        X.append(seq_x)
        y.append(seq_y)
    return array(X), array(y)

raw_seq = [10, 20, 30, 40, 50, 60, 70, 80, 90]
n_steps_in, n_steps_out = 3, 2

X, y = split_sequence(raw_seq, n_steps_in, n_steps_out)

for i in range(len(X)):
    print(X[i], y[i])
print(X.shape)
print(y.shape)