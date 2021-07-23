n=(input())
game=input()
print('Friendship') if game.count('A') == game.count('D') else print('Anton') if game.count('A') > game.count('D') and game.count('A') != game.count('D') else print('Danik')
