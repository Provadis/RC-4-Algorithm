def key_scheduling_algorithm(key: list, modulus: int, verbose=None):
    S = []
    for i in range(modulus):
        S.append(i)

    j = 0
    if verbose:
        print(f" KSA\n|\t|K =|{key}")
        print(f"|i\t|j\t|{S}")
    for i in range(modulus):
        j = (j + S[i] + key[i % len(key)]) % modulus
        S[i], S[j] = S[j], S[i]
        if verbose:
            print(f"|{i}\t|{j}\t|{S}")
    return S


def pseudo_random_generator(S: int, modulus: int, length: int, verbose=None):
    i = 0
    j = 0
    stream = []
    if verbose:
        print(f"\n PRGA \n|i\t|j\t|{S}|Output")

    for _ in range(length):
        i = (i + 1) % modulus
        j = (j + S[i]) % modulus
        S[i], S[j] = S[j], S[i]
        stream.append(S[(S[i] + S[j]) % modulus])
        if verbose:
            print(f"|{i}\t|{j}\t|{S}|{S[(S[i] + S[j]) % modulus]}")

    return stream


if __name__ == '__main__':
    key = [6, 7, 2, 3, 4, 5]
    modulus = 8
    length = 8
    verbose = True  # set to "True" for Output after each step
    S = key_scheduling_algorithm(key, modulus, verbose)
    pseudo_random_generator(S, modulus, length, verbose)
