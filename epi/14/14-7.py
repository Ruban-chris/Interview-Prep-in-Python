class Interval:
    def __init__(self):
        self.start = {'value': None, 'inclusive': False}
        self.end = {'value': None, 'inclusive': False}
    def __str__(self):
        startBracket = '[' if self.start['inclusive'] else '('
        endBracket = ']' if self.end['inclusive'] else ')'
        startValue = self.start['value']
        endValue = self.end['value']
        
        result = [startBracket, str(startValue), ',',str(endValue), endBracket]
        return ''.join(result)

    def __lt__(self, other):
        if self.start['value'] == other.start['value']:
            if self.start['inclusive'] == other.start['inclusive']:
                if self.end['value'] == other.end['value']:
                    if not(self.end['inclusive']) and other.end['inclusive']:
                        return True
                    else:
                        return False
                elif self.end['value'] < other.end['value']:
                    return True
                else:
                    return False
            elif self.start['inclusive'] and not(other.start['inclusive']):
                return True
            else:
                return False
        elif self.start['value'] < other.start['value']:
            return True
        else:
            return False
            

interval1e5e = Interval()
interval1e5e.start['value'] = 1
interval1e5e.start['inclusive'] = False
interval1e5e.end['value'] = 5
interval1e5e.end['inclusive'] = False

interval1e5i = Interval()
interval1e5i.start['value'] = 1
interval1e5i.start['inclusive'] = False
interval1e5i.end['value'] = 5
interval1e5i.end['inclusive'] = True

interval1i5e = Interval()
interval1i5e.start['value'] = 1
interval1i5e.start['inclusive'] = True
interval1i5e.end['value'] = 5
interval1i5e.end['inclusive'] = False

interval1i5i = Interval()
interval1i5i.start['value'] = 1
interval1i5i.start['inclusive'] = True
interval1i5i.end['value'] = 5
interval1i5i.end['inclusive'] = True

interval2i5i = Interval()
interval2i5i.start['value'] = 2
interval2i5i.start['inclusive'] = True
interval2i5i.end['value'] = 5
interval2i5i.end['inclusive'] = True

myList = [interval1e5e, interval1e5i, interval1i5e, interval1i5i, interval2i5i]

for interval in sorted(myList):
    print(interval)