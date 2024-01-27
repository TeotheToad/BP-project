class LCG:
    def __init__(self, seed, x=16467, y=201467, z=2**10):
        self.x = x
        self.y = y
        self.z = z
        self.state = seed

    def random_number(self):
        self.state = ((self.y + self.x * self.state) % self.z)
        return (self.state / int(self.z))

def money_game(rounds):
    player_amount_of_money = 20 * [25]
    i = 0
    while i <= rounds:
        j = 0
        while j < len(player_amount_of_money):
            value = abs(hash(str(i + 1000)))
            lcg = LCG(seed=value)
            player = int(lcg.random_number() * (len(player_amount_of_money)-1))
            if player < j:
                player_amount_of_money[j] -= 1
                player_amount_of_money[player] += 1
            else:
                player_amount_of_money[j] -= 1
                player_amount_of_money[player+1] += 1
            j = j + 1
        while 0 in player_amount_of_money:
            player_amount_of_money.remove(0)
        i = i + 1
    return player_amount_of_money

rounds = 10000
final_amount_of_money = money_game(rounds)
print("final_amount_of_money:", final_amount_of_money)














