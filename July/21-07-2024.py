    def findMaxProduct(self, arr):
        mod = int(1e9 + 7)
        neg_count = 0
        max_neg = float('-inf')
        pos_product = 1
        neg_product = 1
        has_non_zero = False

        for num in arr:
            if num < 0:
                neg_count += 1
                max_neg = max(max_neg, num)

        skip_max_neg = (neg_count % 2 == 1)

        for num in arr:
            if num < 0:
                if skip_max_neg and num == max_neg:
                    skip_max_neg = False
                    continue
                neg_product = (neg_product * abs(num)) % mod
            elif num > 0:
                pos_product = (pos_product * num) % mod
                has_non_zero = True

        if not has_non_zero and neg_count <= 1:
            return 0
        return (neg_product * pos_product) % mod
