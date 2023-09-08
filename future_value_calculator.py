import matplotlib.pyplot as plt
import numpy as np

class FutureValueCalculator:
    def __init__(self, monthly_deposit, annual_interest_rate, years):
        # 初期化メソッド
        self._monthly_deposit = monthly_deposit  # 月々の積み立て額
        self._annual_interest_rate = annual_interest_rate  # 年間利率
        self._years = years  # 積み立て期間（年）

    def _calculate_future_value(self, years):
        # 未来の価値を計算するプライベートメソッド
        # 年利率を月利率に変換
        monthly_interest_rate = self._annual_interest_rate / 100.0 / 12.0

        # 積み立て期間ごとに利息と元本を計算
        total_amount = 0
        months = years * 12  # 積み立て期間を月数に変換
        for month in range(months):
            total_amount += self._monthly_deposit
            total_amount *= 1 + monthly_interest_rate
        base_total = months * self._monthly_deposit
        interest_total = total_amount - base_total
        return base_total, interest_total, total_amount

    def _format_with_commas(self, number):
        # 数字をカンマ区切りの文字列にフォーマットするプライベートメソッド
        return "{:,.0f}".format(number)

    def display_results(self):
        # 結果を表示するメソッド
        base_total, interest_total, total_amount = 
self._calculate_future_value(self._years)
        formatted_monthly_deposit = 
self._format_with_commas(self._monthly_deposit)
        formatted_annual_interest_rate = 
self._format_with_commas(self._annual_interest_rate)
        formatted_base_total = self._format_with_commas(base_total)
        formatted_interest_total = 
self._format_with_commas(interest_total)
        formatted_total_amount = self._format_with_commas(total_amount)
        yeild_rate = total_amount / base_total

        print("月々の積み立て額: {}円".format(formatted_monthly_deposit))
        print("年利率: {}%".format(formatted_annual_interest_rate))
        print("積み立て期間: {}年".format(self._years))
        print("積み立て期間後の元本の合計: 
{}円".format(formatted_base_total))
        print("積み立て期間後の元本と利息の合計: 
{}円".format(formatted_total_amount))
        print("積み立て期間後の利息の合計: 
{}円".format(formatted_interest_total))
        print("利回り（元本に対する割合）: {:.2%}".format(yeild_rate))

    def plot_results(self):
        # 結果をプロットするメソッド
        years_range = range(1, self._years + 1)
        total_amounts = []

        for year in years_range:
            _, _, total_amount = self._calculate_future_value(year)
            total_amounts.append(total_amount / 10000)  # 
単位を1万円に変更

        base_totals = [self._calculate_future_value(year)[0] / 10000 for 
year in years_range]  # 年ごとの元本合計

        fig, ax = plt.subplots()

        ax.set_xlabel('year')
        ax.set_ylabel('10,000yen', labelpad=10)  # 
縦軸のラベルと目盛りの位置を調整
        ax.plot(years_range, total_amounts, marker='o', linestyle='-', 
color='red', label='principal_and_interest_sum')
        ax.bar(years_range, base_totals, color='blue', alpha=0.5, 
label='base total')
        ax.legend(loc='upper left')  # 凡例を表示

        fig.tight_layout()
        plt.show()

# クラスを使って計算と表示を行う
monthly_deposit = 70000
annual_interest_rate = 5
investment_period = 50

calculator = FutureValueCalculator(
    monthly_deposit, annual_interest_rate, investment_period
)
calculator.display_results()  # 結果の表示
calculator.plot_results()  # グラフの描画

