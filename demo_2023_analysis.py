#!/usr/bin/env python3
"""
演示脚本 - 展示2023年的详细因子分析
按照问题陈述中的格式输出
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from analysis.gold_price_model_v7 import GoldPriceModelV7


def main():
    """运行2023年的详细分析示例"""
    print("=" * 80)
    print("黄金价格预测模型 V7.0 - 2023年详细分析示例")
    print("=" * 80)
    print()
    
    # 创建模型实例
    model = GoldPriceModelV7()
    
    # 分析2023年
    result = model.analyze_year(2023)
    
    # 1. 逐因子追溯分析
    print("=" * 80)
    print("【第一部分】逐因子追溯分析")
    print("=" * 80)
    print()
    
    # 显示央行购金因子的详细追溯
    central_bank_factor = [f for f in result['factors'] if f.name == '央行购金'][0]
    model.print_factor_trace(2023, central_bank_factor)
    
    print("\n" + "=" * 80)
    
    # 显示另一个因子（股市效应）的详细追溯
    stock_factor = [f for f in result['factors'] if f.name == '股市效应'][0]
    model.print_factor_trace(2023, stock_factor)
    
    # 2. 因子贡献汇总
    print("\n" + "=" * 80)
    print("【第二部分】因子贡献汇总")
    print("=" * 80)
    model.print_factor_summary(result)
    
    # 3. 触发器分析
    print("\n" + "=" * 80)
    print("【第三部分】触发器分析")
    print("=" * 80)
    model.print_trigger_analysis(result)
    
    # 4. 计算一致性验证
    print("\n" + "=" * 80)
    print("【第四部分】计算一致性验证")
    print("=" * 80)
    model.print_validation(result)
    
    # 5. 文件输出说明
    print("\n" + "=" * 80)
    print("【第五部分】报告文件")
    print("=" * 80)
    print("\n📁 已生成以下报告文件：")
    print("\n1️⃣  年度CSV报告:")
    print("   📄 reports/year_2023_contributions.csv")
    print("      - 包含所有因子的详细数据")
    print("      - 可在Excel中打开查看")
    
    print("\n2️⃣  汇总Excel报告:")
    print("   📄 reports/factor_contribution_2000_2023.xlsx")
    print("      - 包含2000-2023年所有因子数据")
    print("      - 支持多维度分析")
    
    print("\n3️⃣  触发器分析报告:")
    print("   📄 reports/trigger_analysis_2000_2023.xlsx")
    print("      - 包含每年的触发器激活情况")
    print("      - 包含验证结果")
    
    print("\n" + "=" * 80)
    print("✅ 演示完成！")
    print("=" * 80)


if __name__ == '__main__':
    main()
