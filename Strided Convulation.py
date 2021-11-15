import numpy as np


def conv_forward(A_prev, W, b, hparams):
    stride = hparams["stride"]
    pad = hparams["pad"]

    m, h_prev, w_prev, c_prev = A_prev.shape

    # number of channels in the input
    f, f, c_prev, n_c = W.shape

    n_h = int((h_prev - f + 2 * pad) / stride) + 1
    n_w = int((w_prev - f + 2 * pad) / stride) + 1

    Z = np.zeros((m, n_h, n_w, n_c))
    # A_prev_pad = zero_pad(A_prev, pad)
    for i in range(m):
        for h in range(n_h):
            for w in range(n_w):
                for c in range(n_c):
                    w_start = w * stride
                    w_end = w_start + f
                    h_start = h * stride
                    h_end = h_start + f

                    Z[i, h, w, c] = conv_single_step(A_prev_pad[i, h_start:h_end, w_start:w_end, :], W[:, :, :, c],
                                                     b[:, :, :, c])
    return Z
