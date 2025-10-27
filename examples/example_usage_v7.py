"""
黄金价格预测模型 V7.0 - 使用示例
Example Usage for Enhanced Gold Price Prediction Model V7.0

本脚本展示模型的各种使用方式和查询功能

作者: bluestart1204
日期: 2025-10-23
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.analysis.enhanced_model_v7 import EnhancedGoldPredictionModelV7


def example_1_basic_usage():
    """示例1: 基础使用 - 运行完整分析"""
    print("\n" + "=" * 80)
    print("示例1: 基础使用 - 运行完整分析")
    print("=" * 80)
    
    # 创建模型实例并运行完整分析
    model = EnhancedGoldPredictionModelV7()
    model.run_complete_analysis()
    
    return model


def example_2_single_factor_trace(model):
    """示例2: 查询单个因子"""
    print("\n" + "=" * 80)
    print("示例2: 查询单个因子 - 2023年央行购金")
    print("=" * 80)
    
    # 使用中文名查询
    result = model.trace_factor('央行购金', 2023)
    
    # 也可以使用英文名
    # result = model.trace_factor('central_bank', 2023)
    
    return result


def example_3_year_analysis(model):
    """示例3: 分析某一年的所有因子"""
    print("\n" + "=" * 80)
    print("示例3: 年度分析 - 2023年所有因子")
    print("=" * 80)
    
    # 分析2023年
    df = model.analyze_year(2023, export_csv=True)
    
    print("\n查看前5大驱动因子:")
    print(df.head())
    
    return df


def example_4_cross_year_comparison(model):
    """示例4: 跨年对比"""
    print("\n" + "=" * 80)
    print("示例4: 跨年对比 - 央行购金在2020-2023年的表现")
    print("=" * 80)
    
    # 对比央行购金在多个年份的表现
    years = [2020, 2021, 2022, 2023]
    df = model.compare_factor('央行购金', years)
    
    return df


def example_5_multiple_factors(model):
    """示例5: 查询多个因子"""
    print("\n" + "=" * 80)
    print("示例5: 查询多个因子 - 2023年的主要驱动力")
    print("=" * 80)
    
    # 查询2023年的几个关键因子
    factors = ['央行购金', '动量效应', '股市效应', '投资需求', '实际利率']
    
    for factor in factors:
        print(f"\n{'─' * 80}")
        print(f"📊 {factor}")
        print('─' * 80)
        result = model.trace_factor(factor, 2023, verbose=False)
        if result:
            print(f"  原始值: {result['layer_1']['raw_value']:+.2%}")
            print(f"  权重: {result['layer_3']['weight']:.3f}")
            print(f"  最终贡献: {result['layer_5']['final_contrib']:+.2%}")
            print(f"  排名: 第{result['layer_5']['rank']}位")


def example_6_historical_analysis(model):
    """示例6: 历史数据分析"""
    print("\n" + "=" * 80)
    print("示例6: 历史数据分析 - 主要事件年份")
    print("=" * 80)
    
    # 分析几个关键年份
    key_years = {
        2008: '金融危机',
        2013: 'QE削减',
        2020: '新冠疫情',
        2023: '当前年份'
    }
    
    for year, event in key_years.items():
        print(f"\n{'─' * 80}")
        print(f"📅 {year}年 - {event}")
        print('─' * 80)
        
        year_data = model.historical_data[year]
        print(f"  金价涨跌: {year_data['actual_return']:+.2%}")
        print(f"  起止价格: ${year_data['price'][0]} → ${year_data['price'][1]}")
        print(f"  市场状态: {year_data['market_state']}")
        
        if year_data.get('triggers'):
            trigger_names = [model.scenario_triggers[t]['name'] 
                           for t in year_data['triggers']]
            print(f"  触发器: {', '.join(trigger_names)}")


def example_7_validation(model):
    """示例7: 计算验证"""
    print("\n" + "=" * 80)
    print("示例7: 计算验证 - 检查多年的预测准确性")
    print("=" * 80)
    
    # 验证最近5年
    years = [2019, 2020, 2021, 2022, 2023]
    
    print("\n年份  预测值    实际值    误差     状态")
    print("─" * 60)
    
    for year in years:
        result = model.validate_calculation(year)
        if result:
            status = "✓" if abs(result['error']) < 0.1 else "⚠"
            print(f"{year}  {result['predicted']:+7.2%}  {result['actual']:+7.2%}  "
                  f"{result['error']:+7.2%}  {status}")


def example_8_export_data(model):
    """示例8: 批量导出数据"""
    print("\n" + "=" * 80)
    print("示例8: 批量导出 - 导出2020-2023年的分析结果")
    print("=" * 80)
    
    # 批量导出多年数据
    years = [2020, 2021, 2022, 2023]
    
    for year in years:
        model.analyze_year(year, export_csv=True)
        print(f"✓ 已导出 {year} 年数据")


def example_9_factor_comparison_table(model):
    """示例9: 因子对比表"""
    print("\n" + "=" * 80)
    print("示例9: 因子对比 - 主要因子在不同市场状态下的表现")
    print("=" * 80)
    
    # 选择不同市场状态的年份
    bullish_year = 2020  # 牛市
    bearish_year = 2013  # 熊市
    neutral_year = 2023  # 中性
    
    factors = ['央行购金', '实际利率', '股市效应', '动量效应']
    
    print(f"\n{'因子':12s}  {'牛市(2020)':>12s}  {'熊市(2013)':>12s}  {'中性(2023)':>12s}")
    print("─" * 60)
    
    for factor in factors:
        r1 = model.trace_factor(factor, bullish_year, verbose=False)
        r2 = model.trace_factor(factor, bearish_year, verbose=False)
        r3 = model.trace_factor(factor, neutral_year, verbose=False)
        
        if r1 and r2 and r3:
            contrib1 = r1['layer_5']['final_contrib']
            contrib2 = r2['layer_5']['final_contrib']
            contrib3 = r3['layer_5']['final_contrib']
            
            print(f"{factor:12s}  {contrib1:>+11.2%}  {contrib2:>+11.2%}  {contrib3:>+11.2%}")


def example_10_help_system(model):
    """示例10: 帮助系统"""
    print("\n" + "=" * 80)
    print("示例10: 查看帮助信息")
    print("=" * 80)
    
    model.help()


def main():
    """主函数 - 运行所有示例"""
    print("\n" + "═" * 80)
    print("黄金价格预测模型 V7.0 - 使用示例集")
    print("═" * 80)
    
    # 示例1: 基础使用
    model = example_1_basic_usage()
    
    # 等待用户继续
    input("\n按回车键继续查看更多示例...")
    
    # 示例2: 单因子追溯
    example_2_single_factor_trace(model)
    input("\n按回车键继续...")
    
    # 示例3: 年度分析
    example_3_year_analysis(model)
    input("\n按回车键继续...")
    
    # 示例4: 跨年对比
    example_4_cross_year_comparison(model)
    input("\n按回车键继续...")
    
    # 示例5: 多因子查询
    example_5_multiple_factors(model)
    input("\n按回车键继续...")
    
    # 示例6: 历史分析
    example_6_historical_analysis(model)
    input("\n按回车键继续...")
    
    # 示例7: 验证
    example_7_validation(model)
    input("\n按回车键继续...")
    
    # 示例8: 批量导出
    example_8_export_data(model)
    input("\n按回车键继续...")
    
    # 示例9: 对比表
    example_9_factor_comparison_table(model)
    input("\n按回车键继续...")
    
    # 示例10: 帮助
    example_10_help_system(model)
    
    print("\n" + "═" * 80)
    print("✅ 所有示例演示完成！")
    print("═" * 80)
    print("\n提示: 你可以使用 model.interactive_query() 进入交互式查询模式")


if __name__ == "__main__":
    # 运行所有示例（需要手动按回车继续）
    # main()
    
    # 或者只运行特定示例（无需交互）
    print("\n运行快速示例（无需交互）...")
    model = example_1_basic_usage()
    
    # 自动运行几个示例
    example_2_single_factor_trace(model)
    example_3_year_analysis(model)
    example_4_cross_year_comparison(model)
    example_7_validation(model)
    
    print("\n" + "═" * 80)
    print("✅ 快速示例完成！")
    print("═" * 80)
    print("\n💡 提示:")
    print("  - 运行 python examples/example_usage_v7.py 查看所有示例")
    print("  - 在 Python 中导入模型开始使用:")
    print("    from src.analysis.enhanced_model_v7 import EnhancedGoldPredictionModelV7")
    print("    model = EnhancedGoldPredictionModelV7()")
    print("    model.run_complete_analysis()")
