import numpy as np
import matplotlib.pyplot as plt
import math


def generatePlot(windowSize, pitchValues):
	fig = plt.figure()
	ax = fig.add_subplot(111)

	ax.set(title='Accelerometer reading for Raw Pitch Angles and Moving Average of '+str(windowSize)+' Pitch Angles', ylabel='Pitch Angle (in degrees)', xlabel='Number of Readings')

	ax.plot(pitchValues.keys(), pitchValues.values(), linewidth=1)

	movingAverageValues = movingAverage(windowSize, pitchValues)
	ax.plot(movingAverageValues.keys(), movingAverageValues.values(), color='red', linewidth=1)

	mean = np.mean(list(movingAverageValues.values()), dtype=np.float32)
	std = np.std(list(movingAverageValues.values()), dtype=np.float32)
	ax.text(280, 18, 'The mean of the Moving Average is '+str(mean))
	ax.text(280, 17, 'The standard deviation of Moving Average is '+str(std))

	ax.legend(['Raw Data', 'Moving Average of '+str(windowSize)])
	plt.show()


def movingAverage(windowSize, dataValues):
	newValues = dict()
	keys = list(dataValues.keys())
	values = list(dataValues.values())

	sumofValues = 0
	sumofKeys = 0
	for i in range(0, windowSize, 1):
		sumofValues = sumofValues + values[i]
		sumofKeys = sumofKeys + keys[i]

	for i in range(1, len(values)-windowSize, 1):
		newValues[sumofKeys/windowSize] = sumofValues/windowSize
		sumofValues = sumofValues - values[i-1]
		sumofKeys = sumofKeys - keys[i-1]
		sumofValues = sumofValues + values[i + windowSize-1]
		sumofKeys = sumofKeys +keys[i + windowSize-1]

	return newValues

fileName = "imudata.txt"
pitchValues = dict()

count = 0
with open(fileName) as file:
	content = file.readlines()
	for line in content:
		separtateValues = line.split(" ")
		pitchValues[count] = int(separtateValues[4])
		count = count+1


generatePlot(2, pitchValues)

generatePlot(4, pitchValues)

generatePlot(8, pitchValues)

generatePlot(16, pitchValues)

generatePlot(64, pitchValues)

generatePlot(128, pitchValues)









