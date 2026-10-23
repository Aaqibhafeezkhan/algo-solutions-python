<<<<<<< HEAD:practice_problem_solutions (2026)/practice229.py
# Weighted Word Mapping

class Solution:
    def mapWordWeights(self, words, weights) -> str:
        alp = dict(zip(range(25, -1, -1),[chr(i) for i in range(97, 123)]))

        res = ""
        for word in words:
            t = sum([weights[ord(w) - 97] for w in word]) % 26
            print(t)
            res += alp[t]

        return res

s = Solution()
print(s.mapWordWeights(["abcd","def","xyz"], [5,3,12,14,1,2,3,2,10,6,6,9,7,8,7,10,8,9,6,9,9,8,3,7,7,2]))
=======
# CodeWars - The Solar System - Lost Moons

planet_moons = {
    'Mercury': [],
    'Venus': [],
    'Earth': ['Moon'],
    'Mars': ['Deimos', 'Phobos'],
    'Jupiter': ['Callisto', 'Europa', 'Ganymede', 'Io'],
    'Saturn': ['Dione', 'Iapetus', 'Rhea', 'Tethys', 'Titan'],
    'Uranus': ['Ariel', 'Miranda', 'Oberon', 'Titania', 'Umbriel'],
    'Neptune': ['Nereid', 'Proteus', 'Triton']
}

def lost_moons(planets, moons):
    res = []
    for planet in sorted(planets, key=lambda x: ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"].index(x)):
        temp = [planet]
        right = True
        for moon in planet_moons[planet]:
            if moon in moons:
                if right:
                    temp.append(moon)
                else:
                    temp.insert(0, moon)
                right = not right
        res.append(temp)
    return res

print(lost_moons(['Earth', 'Mars', 'Jupiter'], ['Moon', 'Phobos', 'Europa'])) # [['Earth', 'Moon'], ['Mars', 'Phobos'], ['Jupiter', 'Europa']]
print(lost_moons(['Earth', 'Mars', 'Jupiter'], ['Deimos', 'Ganymede', 'Io'])) # [['Earth'], ['Mars', 'Deimos'], ['Jupiter', 'Ganymede', 'Io']]
print(lost_moons(['Earth', 'Mars', 'Jupiter'], ['Callisto', 'Dione', 'Iapetus'])) # [['Earth'], ['Mars'], ['Jupiter', 'Callisto']]
>>>>>>> 96c2367 (chore: refactor the project structure):solutions/python/practice229.py
