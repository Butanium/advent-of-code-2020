file_lines = open('puzzle_inputs/puzzle_input_day_7.txt').read().split('.\n')
color_properties_list = []
name_color_list = []
file_test_lines  = open('tests/test_day_7_2.txt').read().split('.\n')


class Color:
    def __init__(self, string: str):
        splited = string.split(' bags contain ')
        self.name = splited[0]
        name_color_list.append(self.name)
        colors = splited[1].split(', ')
        self.reachable_colors = []
        self.reachable_colors_count = []
        self.gold = self.name == 'shiny gold'
        self.active = False
        for color in colors:
            c = ''
            n = ''
            i = 0
            begin = False
            while i < len(color) - 4 - (color[-1] == 's' or (color[-1] == '.' and color[-2] == 's')) - (
                    color[-1] == '.'):
                if color[i].isdigit():
                    n += color[i]
                if not begin and color[i].isalpha():
                    begin = True
                if begin:
                    c += color[i]
                i += 1
            if c == 'no other':
                self.active = True
                break
            self.reachable_colors.append(c)
            self.reachable_colors_count.append(int(n))
        if 'shiny gold' in self.reachable_colors:
            self.gold = True
        print(self.reachable_colors_count)
        color_properties_list.append(self)

    def is_gold(self, visited_bags=()):
        if self.gold:
            return True
        if self.active:
            return False
        if not visited_bags:
            visited_bags = []

        for color in self.reachable_colors:
            if color in visited_bags:
                continue
            bag = get_color(color)
            if bag.gold:
                self.gold = True
                return True
            elif bag.active:
                visited_bags.append(color)
                continue
            else:
                if bag.is_gold(visited_bags):
                    self.gold = True
                    return True
                else:
                    visited_bags.append(color)
                    continue
        self.active = True
        return False

    def get_bags(self):
        score = 0
        if not self.reachable_colors:
            return 1
        for i in range(len(self.reachable_colors)):
            color = self.reachable_colors[i]
            f = self.reachable_colors_count[i]
            score += f*get_color(color).get_bags()
        return score+1


def get_color(name) -> Color:
    return color_properties_list[name_color_list.index(name)]

for color_line in file_lines:
    Color(color_line)

# for color_line in file_test_lines:
#     Color(color_line)

result = 0

# for bag in color_properties_list:
#     result += bag.is_gold()
shiny_bag = get_color('shiny gold')
print(shiny_bag.name)
print(shiny_bag.get_bags()-1)

# print(result)

