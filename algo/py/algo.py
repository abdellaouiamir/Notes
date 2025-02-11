def find_minimum(nums):
    minimum = float("inf")
    if len(nums) == 0:
        return None
    for num in nums:
        if num < minimum:
            minimum = num
    return minimum
def median_followers(nums):
    if len(nums) == 0:
        return None
    nums = sorted(nums)
    n = len(nums)
    if n % 2 == 0:
        return (nums[n // 2 - 1] + nums[n // 2]) / 2
    return nums[n // 2]
def get_estimated_spread(audiences_followers):
    num_followers = len(audiences_followers)
    if num_followers == 0:
        return 0

    sum = 0
    for num in audiences_followers:
        sum += num

    average_audience_followers = sum / num_followers
    return average_audience_followers * (num_followers**1.2)
def num_possible_orders(num_posts):
    product = 1
    for i in range(1, num_posts + 1):
        product *= i
    return product
def decayed_followers(intl_followers, fraction_lost_daily, days):
    res = intl_followers * (1 - fraction_lost_daily) ** days
    return res
import math
def log_scale(data, base):
    return [math.log(i, base) for i in data]
def find_max(nums):
    max = -float("inf")
    for num in nums:
        if num > max:
            max = num
    return max
def find_last_name(names_dict, first_name):
    try:
        return names_dict[first_name]
    except KeyError:
        return None
def binary_search(target, arr):
    low = 0
    high = len(arr) - 1
    while low <= high:
        median = (low + high) // 2
        if arr[median] == target:
            return True
        elif arr[median] < target:
            low = median + 1
        else:
            high = median - 1
    return False
def remove_duplicates(nums):
    unique_nums = []
    for num in nums:
        if num not in unique_nums:
            unique_nums.append(num)
    return unique_nums
##################################################
class Influencer:
    def __init__(self, num_selfies, num_bio_links):
        self.num_selfies = num_selfies
        self.num_bio_links = num_bio_links

    def __repr__(self):
        return f"({self.num_selfies}, {self.num_bio_links})"


# dont touch above this line


def vanity(influencer):
    return influencer.num_bio_links * 5 + influencer.num_selfies


def vanity_sort(influencers):
    result = sorted(influencers, key=vanity)
    return result
#########################################

