# Placeholders - are taking the place of something

# %s = string
# %d = Integer

>>> name = "Jake"
>>> name + "is 15 years old"

>>> sentence = "%s is 15 years old"
>>> sentence%name

>>> sentence%("Jacob")

>>> sentence = "%s %s is a genius"
>>> sentence%("Jacob", "Hanson")

>>>sent = "%s is %d"
>>> sent%("Barack", 50)