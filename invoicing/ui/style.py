from ansi_colours import AnsiColours as Colour

class Style:
    @staticmethod
    def create_title(title):
        return "\n" + title + "\n" + Style.create_underline(title)

    @staticmethod
    def create_underline(title):
        return Colour.blue("".join(['-' for _ in range(len(title))]))
