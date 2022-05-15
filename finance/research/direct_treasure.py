from datetime import date, timedelta

import investpy
import pandas as pd


class Treasure:

    def __init__(self):
        self.treasure = {}
        search = investpy.search_quotes(text='tesouro',
                                        products=['bonds'],
                                        countries=['brazil'],
                                        )
        for result in search:
            self.treasure[result.symbol[:9]] = result

    def get_list(self) -> list:
        """ Returns a list of all symbols

        Returns:
            list: List of all symbols in the treasure brazil
        ex: [
            'LFT030123', 'LFT030124', 'LFT030127', 'LFT090122', 'LFT090123',
            'LTN010123', 'LTN070124', 'NTB031523', 'NTB051523', 'NTB051535',
            'NTB051545', 'NTB051555', 'NTB081522', 'NTB081524', 'NTB081526',
            'NTB081528', 'NTB081530', 'NTB081540', 'NTB081550']"""
        return sorted(self.treasure.keys())

    def get_historical_data(self, symbol:str, days:int=1)-> pd.DataFrame:
        """Returns the historical data for a given symbol

        Args:
            symbol (str): symbols defined in get_list()
            days (int, optional): number days. Defaults to 1.

        Returns:
            pd.DataFrame: historical data for the given symbol
            
        ex:  treasure.get_historical_data('LFT030127')
        
            Date         Open      High       Low        Close      Change Pct
            2022-05-10  11531.937  11531.937  11531.937  11531.937  0.0"""     

        to_date = date.today().strftime('%d/%m/%Y')
        from_date = (date.today() - timedelta(days=days)).strftime('%d/%m/%Y')
        return self.treasure[symbol].retrieve_historical_data(
            from_date=from_date, to_date=to_date)[1:]


if __name__ == "__main__":
    treasure = Treasure()
    print(treasure.get_historical_data('LFT030127'))
