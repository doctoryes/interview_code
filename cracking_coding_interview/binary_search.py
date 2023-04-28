class BinarySearch:
    """
    """

    # def _search_slice(self, nums, target, start_idx):
    #     if len(nums) == 1:
    #         if nums[0] == target:
    #             return start_idx
    #     else:
    #         half_length = len(nums) // 2
    #         if nums[half_length - 1] >= target:
    #             return self._search_slice(nums[0:half_length], target, start_idx)
    #         else:
    #             return self._search_slice(nums[half_length:], target, start_idx + half_length)

    # def _search_index_recurse(self, nums, target, start_idx, end_idx):
    #     if start_idx == end_idx:
    #         if nums[start_idx] == target:
    #             return start_idx
    #     else:
    #         # New middle point between start and end.
    #         idx = (end_idx - start_idx) // 2 + start_idx
    #         if nums[idx] >= target:
    #             return self._search_index_recurse(nums, target, start_idx, idx)
    #         else:
    #             return self._search_index_recurse(nums, target, idx + 1, end_idx)

    def _search_index(self, nums, target, start_idx, end_idx):
        while True:
            if start_idx == end_idx:
                if nums[start_idx] == target:
                    return start_idx
                else:
                    return None

            # New middle point between start and end.
            idx = (end_idx - start_idx) // 2 + start_idx
            if nums[idx] >= target:
                end_idx = idx
            else:
                start_idx = idx + 1

    def search(self, nums: list[int], target: int) -> int:
        """
        Searches a list of ints using binary search to find the target number.
        Returns the index of the target, None if not found.
        """
        # result = self._search_slice(nums, target, 0)
        # result = self._search_index_recurse(nums, target, 0, len(nums) - 1)
        result = self._search_index(nums, target, 0, len(nums) - 1)
        return result if result is not None else -1

