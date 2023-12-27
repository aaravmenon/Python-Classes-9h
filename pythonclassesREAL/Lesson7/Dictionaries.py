band = {
    "vocals": "Plant",
    "guitar": "Page"
}

band2 = dict(vocals="Plant", guitar="Pages")

print(len(band))
print(type(band))

print(band["vocals"])
print(band.get("guitar"))
print(band.keys())
print(band.values())
print(band.items())

print("guitar" in band)
print("triangle" in band)

band["vocals"] = "Coverdales"
band.update({"Bass": "JPJ"})

band["drums"] = "Bonham"

print(band.popitem())

band2.clear()
print(band2)
del band2

band2 = band.copy()
band2["Drums"] = "Aarav"
print(band)
print(band2)

member1 = {
    "name": "Jimmy",
    "instrument": "vocals"
}
member2 = {
    "name": "Joel",
    "instrument": "guitar"
}
band = {
    "member1": member1,
    "member2": member2
}
print(band)
print(band["member1"]["name"])

nums = {1, 2, 3, 4}

nums2 = set((1, 2, 3, 4))

print(nums)
print(nums2)
print(type(nums))
print(len(nums))

nums = {1, 2, 2, 3}
print(nums)

nums = {1, True, 2, False, 3, 4, 0}
print(nums)

print(2 in nums)

nums.add(8)
print(nums)

morenums = {5, 6, 7}
nums.update(morenums)
print(nums)

one = {1, 2, 3}
two = {5, 6, 7}

mynewset = one.union(two)
print(mynewset)

one = {1, 2, 3}
two = {2, 3, 4}

one.intersection_update(two)
print(one)

one = {1, 2, 3}
two = {2, 3, 4}

one.symmetric_difference_update(two)
print(one)