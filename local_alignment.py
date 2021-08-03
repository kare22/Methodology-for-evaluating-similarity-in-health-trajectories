## Get local alignment between person1(horizontal) and person2(vertical)
def get_local_alignment(p1, p2, match=1, mismatch=-1, gap_penalty=-1):
    # Initialisation
    matrix = [[0 for i in range(len(p2) + 1)] for j in range(len(p1) + 1)]
    for i in range(len(p1) + 1):
        matrix[i][0] = i * gap_penalty
    for i in range(len(p2) + 1):
        matrix[0][i] = i * gap_penalty

    # Fill
    for i in range(len(p1)):
        for j in range(len(p2)):
            p1_diagnosis = p1[i][0]
            p2_diagnosis = p2[j][0]
            left = matrix[i][j + 1] + gap_penalty
            right = matrix[i + 1][j] + gap_penalty
            diagonal = matrix[i][j] + (match if p1_diagnosis == p2_diagnosis else mismatch)
            matrix[i + 1][j + 1] = max(left, right, diagonal, 0)

    # Find the biggest alignment value
    MAX = None
    for row in matrix:
        row_max = max(row)
        MAX = row_max if MAX == None or row_max > MAX else MAX

    return MAX
