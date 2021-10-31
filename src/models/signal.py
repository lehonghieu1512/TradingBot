from src.models.converter import Converter

class Signal:


    @classmethod
    def text_to_signal(cls, text: str):
        text = text.lower()
        symbol = Converter.get_symbol(text)

        if not symbol:
            return None


        text = Converter.clean_text(text)

        entries = Converter.get_entry(text)
        if not entries:
            return None

        entry1, entry2 = entries

        targets = Converter.get_targets(text)
        if not targets:
            return None

        target1, target2 = targets


        stoploss = Converter.get_stoploss(text)
        if not stoploss:
            return None

        return Signal(symbol, entry1, target1, stoploss)



    def __init__(self, symbol: str, entry: float, target: float, sl: float, leverage: float =3):
        self.symbol = symbol
        self.entry = entry
        self.target = target
        self.sl = sl
        self.leverage = leverage

