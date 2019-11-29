class Pencil:

    def __init__(self, pointDurability=20, length=10):
        self.writtenText = ""
        self.pointDurabilityDefault = pointDurability
        self.pointDurability = pointDurability
        self.length = length

    def write(self, text):
        degradedText = self.degradeText(text)
        self.writtenText += degradedText
        self.pointDurability = self.pointDurability - self.textDurabilityCost(degradedText)
        return self.writtenText

    def sharpen(self):
        if self.length > 0:
            self.length -= 1
            self.pointDurability = self.pointDurabilityDefault
        return self.length

    def degradeText(self, text):
        pointDurability = self.pointDurability
        degradedText = ""
        for char in text:
            durabilityCost = self.textDurabilityCost(char)
            if durabilityCost <= pointDurability:
                degradedText += char
                pointDurability -= durabilityCost
            else:
                break
        return degradedText

    def textDurabilityCost(self, text):
        durabilityCost = 0
        for char in text:
            if len(char.strip()) == 0:
                pass
            elif char.islower():
                durabilityCost += 1
            else:
                durabilityCost += 2
        return durabilityCost
