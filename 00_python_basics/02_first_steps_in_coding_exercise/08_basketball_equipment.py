yearly_basketball_training = int(input())
basketball_shoes = (yearly_basketball_training - (yearly_basketball_training * 40/100))
basketball_suit = (basketball_shoes - (basketball_shoes * 20/100))
basketball_ball = (basketball_suit / 4)
basketball_accessories = (basketball_ball / 5)
basketball_equipment = (yearly_basketball_training + basketball_shoes + basketball_suit + basketball_ball + basketball_accessories)
print(basketball_equipment)