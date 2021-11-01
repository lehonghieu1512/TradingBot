import re
from typing import Optional, List
from src.config import regex_pattern, signal

class Converter:



    @classmethod
    def clean_text(cls, text) -> str:
        result = re.sub(regex_pattern.remove_special_except_dot, " ", text)
        result = re.sub(' +', ' ', result)

        return result

    @classmethod
    def get_symbol(cls, text) -> Optional[str]:
        search = re.search(regex_pattern.symbol, text)
        if search:
            result = search.group()
            return result
        return None

    @classmethod
    def _get_by_one_entry(cls, entry_text: str, text: str) -> Optional[List[float]]:
        re_pattern = regex_pattern.entry.format(entry_text)
        match = re.search(re_pattern,  text)
        if match:
            try:
                entry1 = float(match.group(1))
                entry2 = float(match.group(3))
            except Exception as e:
                print("Could not parse entries")
                return None
        else:
            return None

        return [entry1, entry2]

    @classmethod
    def _get_by_one_stoploss(cls, sl_text: str, text: str) -> Optional[float]:
        re_pattern = regex_pattern.stoploss.format(sl_text)
        match = re.search(re_pattern,  text)
        if match:
            try:
                stoploss = float(match.group(1))
            except Exception as e:
                print("Could not parse entries")
                return None
        else:
            return None

        return stoploss

    @classmethod
    def _get_by_one_target(cls, target_text: str, text: str) -> Optional[List[float]]:
        re_pattern = regex_pattern.target.format(target_text)
        match = re.search(re_pattern,  text)
        if match:
            try:
                target1 = float(match.group(1))
                target2 = float(match.group(3))
            except Exception as e:
                print("Could not parse entries")
                return None
        else:
            return None

        return [target1, target2]

    @classmethod
    def get_entry(cls, text) -> Optional[List[float]]:
        for entry_text in signal.entry:
            entries = cls._get_by_one_entry(entry_text, text)
            if entries:
                return entries
        return None

    @classmethod
    def get_stoploss(cls, text) -> Optional[float]:
        for sl_text in signal.sl_signals:
            stoploss = cls._get_by_one_stoploss(sl_text, text)
            if stoploss:
                return stoploss
        return None

    @classmethod
    def get_targets(cls, text) -> Optional[List[float]]:
        for sl_text in signal.target_signals:
            stoploss = cls._get_by_one_target(sl_text, text)
            if stoploss:
                return stoploss
        return None