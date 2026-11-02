# Week 1.6, Session 1: Task 5

# Write a program here that uses the QuakeFeed and QuakeDataset
# classes to download earthquake data from a USGS data feed,
# analyze it and display the results

# See README.md for full details of what is required and what
# program output should look like

from feed import QuakeFeed
from quake import Quake
from dataset import QuakeDataset



userLevel = input("Enter a significance level")
userPeriod = input("Enter a time period")

userQuake = QuakeFeed(userLevel, userPeriod)
userQuakeDataset = QuakeDataset(userQuake)

print(userQuakeDataset.reader())