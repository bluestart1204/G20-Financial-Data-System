#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
黄金价格预测模型 V7.0 演示脚本
Demonstration script for Gold Price Prediction Model V7.0
"""

from src.analysis.enhanced_model_v7 import GoldPricePredictionModelV7


def demo_basic_usage():
    """演示基本用法"""
    print("\n" + "="*70)
    print("示例 1: 基本用法 - 运行完整分析")
    print("="*70)
    
    model = GoldPricePredictionModelV7()
    model.run_complete_analysis()


def demo_data_access():
    """演示数据访问"""
    print("\n" + "="*70)
    print("示例 2: 访问特定年份的数据")
    print("="*70 + "\n")
    
    model = GoldPricePredictionModelV7()
    
    # 访问2008年金融危机的数据
    print("📊 2008年金融危机：")
    data_2008 = model.annual_data[2008]
    print(f"  金价变化: ${data_2008['price'][0]} → ${data_2008['price'][1]}")
    print(f"  收益率: {data_2008['actual_return']:.1%}")
    print(f"  市场状态: {data_2008['market_state']}")
    print(f"  触发器: {', '.join(data_2008['triggers'])}")
    print(f"  VIX恐慌指数: {data_2008['vix']:+.2f}")
    print(f"  股市表现: {data_2008['equity']:.1%}")
    
    print("\n📊 2020年疫情冲击：")
    data_2020 = model.annual_data[2020]
    print(f"  金价变化: ${data_2020['price'][0]} → ${data_2020['price'][1]}")
    print(f"  收益率: {data_2020['actual_return']:.1%}")
    print(f"  市场状态: {data_2020['market_state']}")
    print(f"  触发器: {', '.join(data_2020['triggers'])}")
    print(f"  M2货币增速: {data_2020['M2']:.1%}")
    print(f"  VIX恐慌指数: {data_2020['vix']:+.2f}")


def demo_period_analysis():
    """演示周期分析"""
    print("\n" + "="*70)
    print("示例 3: 分析不同时期的表现")
    print("="*70 + "\n")
    
    model = GoldPricePredictionModelV7()
    
    periods = {
        '科技泡沫期 (2000-2003)': range(2000, 2004),
        '牛市加速期 (2004-2007)': range(2004, 2008),
        '金融危机期 (2008-2009)': range(2008, 2010),
        'QE时代 (2010-2012)': range(2010, 2013),
        'Taper恐慌 (2013-2015)': range(2013, 2016),
        '复苏期 (2016-2019)': range(2016, 2020),
        '疫情与加息 (2020-2023)': range(2020, 2024)
    }
    
    for period_name, years in periods.items():
        returns = [model.annual_data[year]['actual_return'] 
                  for year in years if year in model.annual_data]
        avg_return = sum(returns) / len(returns) if returns else 0
        total_return = ((1 + sum(returns)) - 1) if returns else 0
        
        print(f"{period_name}:")
        print(f"  平均年收益率: {avg_return:+.1%}")
        print(f"  累计收益: {total_return:+.1%}")
        print()


def demo_factor_analysis():
    """演示因子分析"""
    print("\n" + "="*70)
    print("示例 4: 关键因子分析")
    print("="*70 + "\n")
    
    model = GoldPricePredictionModelV7()
    
    # 分析央行购金趋势
    print("📈 央行购金趋势变化：")
    key_years = [2000, 2005, 2010, 2015, 2020, 2023]
    for year in key_years:
        cb = model.annual_data[year]['central_bank']
        print(f"  {year}年: {cb:+.1%}")
    
    print("\n📈 实际利率变化：")
    for year in key_years:
        rate = model.annual_data[year]['real_rate']
        print(f"  {year}年: {rate:+.2%}")
    
    print("\n📈 M2货币增速：")
    for year in key_years:
        m2 = model.annual_data[year]['M2']
        print(f"  {year}年: {m2:+.1%}")


def demo_extreme_years():
    """演示极端年份分析"""
    print("\n" + "="*70)
    print("示例 5: 最佳与最差年份")
    print("="*70 + "\n")
    
    model = GoldPricePredictionModelV7()
    
    # 找出收益最高的5年
    years_returns = [(year, data['actual_return']) 
                     for year, data in model.annual_data.items()]
    years_returns.sort(key=lambda x: x[1], reverse=True)
    
    print("🏆 收益最高的5年：")
    for i, (year, return_rate) in enumerate(years_returns[:5], 1):
        data = model.annual_data[year]
        triggers = ', '.join(data['triggers']) if data['triggers'] else '无特殊事件'
        print(f"  {i}. {year}年: {return_rate:+.1%} - {triggers}")
    
    print("\n📉 收益最低的5年：")
    for i, (year, return_rate) in enumerate(years_returns[-5:], 1):
        data = model.annual_data[year]
        triggers = ', '.join(data['triggers']) if data['triggers'] else '无特殊事件'
        print(f"  {i}. {year}年: {return_rate:+.1%} - {triggers}")


def main():
    """运行所有演示"""
    print("\n" + "🌟"*35)
    print("黄金价格预测模型 V7.0 - 综合演示")
    print("🌟"*35)
    
    demo_basic_usage()
    demo_data_access()
    demo_period_analysis()
    demo_factor_analysis()
    demo_extreme_years()
    
    print("\n" + "="*70)
    print("✅ 演示完成！")
    print("="*70 + "\n")


if __name__ == "__main__":
    main()
