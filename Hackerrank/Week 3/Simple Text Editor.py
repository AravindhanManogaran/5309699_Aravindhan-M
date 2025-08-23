import sys

def simpleTextEditor(operations):
    S = []           # current text as list
    history = []     # stack to store past operations
    output = []      # results of print operations

    for op in operations:
        parts = op.split()
        t = int(parts[0])

        if t == 1:  # append(W)
            W = parts[1]
            S.extend(W)
            history.append(("append", len(W)))

        elif t == 2:  # delete(k)
            k = int(parts[1])
            if k <= len(S):
                deleted = S[-k:]
                del S[-k:]
            else:
                deleted = S[:]
                S.clear()
            history.append(("delete", deleted))

        elif t == 3:  # print(k)
            k = int(parts[1])
            if 1 <= k <= len(S):
                output.append(S[k-1])

        elif t == 4:  # undo
            if history:
                last_op = history.pop()
                if last_op[0] == "append":
                    length = last_op[1]
                    del S[-length:]
                elif last_op[0] == "delete":
                    S.extend(last_op[1])

    sys.stdout.write("\n".join(output))


if __name__ == "__main__":
    input_data = sys.stdin.read().strip().split("\n")
    Q = int(input_data[0])
    operations = input_data[1:]
    simpleTextEditor(operations)
