import heapq


def min_comb(arr):
    heapq.heapify(arr)
    total = 0

    while len(arr) > 1:
        new_comb = heapq.heappop(arr) + heapq.heappop(arr)
        total += new_comb

        heapq.heappush(arr, new_comb)
    return total


if __name__ == "__main__":
    cables = [1, 2, 4, 10]
    total = min_comb(cables)
    print(total)  # 27
