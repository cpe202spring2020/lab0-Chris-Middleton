def weight_on_planets():

	earthWeight = float(input("What do you weigh on earth? "))
	marsWeight = earthWeight*0.38
	jupiterWeight = earthWeight*2.34
	print("\nOn Mars you would weigh %.2f pounds.\nOn Jupiter you would weigh %.2f pounds."%(marsWeight,jupiterWeight))


if __name__ == '__main__':
	weight_on_planets()
