#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试黄金价格预测模型 V7.0
Test for Gold Price Prediction Model V7.0
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from src.analysis.enhanced_model_v7 import GoldPricePredictionModelV7


def test_data_completeness():
    """测试数据完整性"""
    model = GoldPricePredictionModelV7()
    
    # 验证年份数量
    assert len(model.annual_data) == 24, f"应该有24年数据，实际有{len(model.annual_data)}年"
    
    # 验证年份范围
    years = sorted(model.annual_data.keys())
    assert years[0] == 2000, f"起始年份应该是2000，实际是{years[0]}"
    assert years[-1] == 2023, f"结束年份应该是2023，实际是{years[-1]}"
    
    # 验证年份连续性
    for i in range(2000, 2024):
        assert i in model.annual_data, f"缺少{i}年的数据"
    
    print("✅ 数据完整性测试通过")


def test_factors_completeness():
    """测试因子完整性"""
    model = GoldPricePredictionModelV7()
    
    # 验证因子数量
    assert len(model.factors) == 15, f"应该有15个因子，实际有{len(model.factors)}个"
    
    # 验证每年都包含所有因子
    for year, data in model.annual_data.items():
        for factor in model.factors:
            assert factor in data, f"{year}年缺少因子: {factor}"
    
    print("✅ 因子完整性测试通过")


def test_data_structure():
    """测试数据结构"""
    model = GoldPricePredictionModelV7()
    
    # 验证每年的数据结构
    for year, data in model.annual_data.items():
        # 必要字段
        assert 'actual_return' in data, f"{year}年缺少 actual_return"
        assert 'price' in data, f"{year}年缺少 price"
        assert 'market_state' in data, f"{year}年缺少 market_state"
        assert 'triggers' in data, f"{year}年缺少 triggers"
        
        # 价格应该是元组
        assert isinstance(data['price'], tuple), f"{year}年的价格不是元组"
        assert len(data['price']) == 2, f"{year}年的价格元组应该包含2个元素"
        
        # 触发器应该是列表
        assert isinstance(data['triggers'], list), f"{year}年的触发器不是列表"
    
    print("✅ 数据结构测试通过")


def test_key_years():
    """测试关键年份"""
    model = GoldPricePredictionModelV7()
    
    # 2001年 - 911恐袭
    assert 'geopolitical_shock' in model.annual_data[2001]['triggers']
    
    # 2002年 - 会计丑闻
    assert 'trust_crisis' in model.annual_data[2002]['triggers']
    
    # 2008年 - 金融危机
    assert 'liquidity_crisis' in model.annual_data[2008]['triggers']
    
    # 2009年 - QE启动
    assert 'qe_launch' in model.annual_data[2009]['triggers']
    
    # 2011年 - 历史高点
    assert 'bubble_peak' in model.annual_data[2011]['triggers']
    
    # 2013年 - Taper恐慌
    assert 'taper_tantrum' in model.annual_data[2013]['triggers']
    
    # 2020年 - 疫情冲击
    assert 'pandemic' in model.annual_data[2020]['triggers']
    
    print("✅ 关键年份测试通过")


def test_validation_method():
    """测试数据验证方法"""
    model = GoldPricePredictionModelV7()
    
    # 应该通过验证
    assert model.validate_data_completeness() == True
    
    print("✅ 数据验证方法测试通过")


def test_summary_statistics():
    """测试汇总统计"""
    model = GoldPricePredictionModelV7()
    
    stats = model.get_summary_statistics()
    
    assert stats['years_count'] == 24
    assert stats['factors_count'] == 15
    assert stats['positive_years'] + stats['negative_years'] == 24
    assert -1 <= stats['avg_return'] <= 1  # 平均收益率应该在合理范围内
    
    print("✅ 汇总统计测试通过")


def main():
    """运行所有测试"""
    print("=" * 60)
    print("黄金价格预测模型 V7.0 - 单元测试")
    print("=" * 60)
    print()
    
    test_data_completeness()
    test_factors_completeness()
    test_data_structure()
    test_key_years()
    test_validation_method()
    test_summary_statistics()
    
    print()
    print("=" * 60)
    print("✅ 所有测试通过！")
    print("=" * 60)


if __name__ == "__main__":
    main()
