class HL_input:
    def __init__(self,HorL):
        self.HorL = HorL




while True:
    option = input("Will the next card be higher or lower? [h/l]")
    if option.lower() == "h" or option.lower() == "l":
        break
    else:
        print("Please type h(for higher) or l(for lower)")  
HL = HL_input(option)
