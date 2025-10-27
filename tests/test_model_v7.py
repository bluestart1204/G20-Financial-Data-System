"""
测试脚本 - 黄金价格预测模型 V7.0
Test Script for Enhanced Gold Price Prediction Model V7.0

功能测试:
1. 模型初始化
2. 数据加载
3. 因子追溯
4. 年度分析
5. 跨年对比
6. 计算验证
7. 导出功能

作者: bluestart1204
日期: 2025-10-23
"""

import sys
import os

# 添加项目路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.analysis.enhanced_model_v7 import EnhancedGoldPredictionModelV7
import pandas as pd
import numpy as np


def test_model_initialization():
    """测试1: 模型初始化"""
    print("\n" + "=" * 80)
    print("测试1: 模型初始化")
    print("=" * 80)
    
    try:
        model = EnhancedGoldPredictionModelV7()
        
        # 检查基本属性
        assert hasattr(model, 'historical_data'), "缺少 historical_data 属性"
        assert hasattr(model, 'factor_definitions'), "缺少 factor_definitions 属性"
        assert hasattr(model, 'scenario_triggers'), "缺少 scenario_triggers 属性"
        assert len(model.factor_name_map) == 15, f"因子数量错误: {len(model.factor_name_map)}"
        
        print("✓ 模型初始化成功")
        print(f"✓ 因子数量: {len(model.factor_name_map)}")
        print(f"✓ 因子名称映射正确")
        
        return True, model
    except Exception as e:
        print(f"✗ 测试失败: {e}")
        return False, None


def test_data_loading(model):
    """测试2: 数据加载"""
    print("\n" + "=" * 80)
    print("测试2: 数据加载")
    print("=" * 80)
    
    try:
        model.setup_historical_data_with_new_factors()
        model.define_scenario_triggers()
        
        # 检查数据完整性
        assert len(model.historical_data) == 24, f"历史数据年份不足: {len(model.historical_data)}"
        assert 2000 in model.historical_data, "缺少2000年数据"
        assert 2023 in model.historical_data, "缺少2023年数据"
        assert len(model.scenario_triggers) == 18, f"触发器数量错误: {len(model.scenario_triggers)}"
        
        # 检查数据结构
        sample_year = model.historical_data[2023]
        assert 'actual_return' in sample_year, "缺少 actual_return 字段"
        assert 'factors' in sample_year, "缺少 factors 字段"
        assert 'market_state' in sample_year, "缺少 market_state 字段"
        assert len(sample_year['factors']) == 15, f"2023年因子数量错误: {len(sample_year['factors'])}"
        
        print("✓ 数据加载成功")
        print(f"✓ 历史数据: {len(model.historical_data)} 年 (2000-2023)")
        print(f"✓ 因子数据完整")
        print(f"✓ 触发器: {len(model.scenario_triggers)} 个")
        
        return True
    except Exception as e:
        print(f"✗ 测试失败: {e}")
        return False


def test_weight_optimization(model):
    """测试3: 权重优化"""
    print("\n" + "=" * 80)
    print("测试3: 权重优化")
    print("=" * 80)
    
    try:
        weights = model.optimize_weights_with_new_factors()
        
        # 检查权重
        assert weights is not None, "权重为空"
        assert len(weights) == 15, f"权重数量错误: {len(weights)}"
        
        # 检查权重和是否接近1
        total_weight = sum(weights.values())
        assert 0.99 <= total_weight <= 1.01, f"权重和不正确: {total_weight}"
        
        # 检查传导系数
        assert model.transmission_coefficients is not None, "传导系数为空"
        
        print("✓ 权重优化成功")
        print(f"✓ 权重总和: {total_weight:.4f}")
        print(f"✓ 前5大权重:")
        sorted_weights = sorted(weights.items(), key=lambda x: x[1], reverse=True)
        for factor, weight in sorted_weights[:5]:
            factor_cn = model.factor_name_map[factor]
            print(f"    {factor_cn:12s}: {weight:.3f}")
        
        return True
    except Exception as e:
        print(f"✗ 测试失败: {e}")
        return False


def test_factor_trace(model):
    """测试4: 因子追溯"""
    print("\n" + "=" * 80)
    print("测试4: 因子追溯")
    print("=" * 80)
    
    try:
        # 测试中文名查询
        result1 = model.trace_factor('央行购金', 2023, verbose=False)
        assert result1 is not None, "中文名查询失败"
        assert result1['year'] == 2023, "年份不正确"
        assert result1['factor_name'] == 'central_bank', "因子名不正确"
        
        # 测试英文名查询
        result2 = model.trace_factor('central_bank', 2023, verbose=False)
        assert result2 is not None, "英文名查询失败"
        
        # 检查5层数据
        assert 'layer_1' in result1, "缺少第1层数据"
        assert 'layer_2' in result1, "缺少第2层数据"
        assert 'layer_3' in result1, "缺少第3层数据"
        assert 'layer_4' in result1, "缺少第4层数据"
        assert 'layer_5' in result1, "缺少第5层数据"
        
        print("✓ 因子追溯成功")
        print(f"✓ 2023年央行购金:")
        print(f"    原始值: {result1['layer_1']['raw_value']:+.2%}")
        print(f"    权重: {result1['layer_3']['weight']:.3f}")
        print(f"    最终贡献: {result1['layer_5']['final_contrib']:+.2%}")
        print(f"    排名: 第{result1['layer_5']['rank']}位")
        
        # 详细输出一次
        print("\n✓ 详细追溯输出测试:")
        model.trace_factor('央行购金', 2023, verbose=True)
        
        return True
    except Exception as e:
        print(f"✗ 测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_year_analysis(model):
    """测试5: 年度分析"""
    print("\n" + "=" * 80)
    print("测试5: 年度分析")
    print("=" * 80)
    
    try:
        # 不导出CSV
        df = model.analyze_year(2023, export_csv=False)
        
        assert df is not None, "返回结果为空"
        assert isinstance(df, pd.DataFrame), "返回类型不是DataFrame"
        assert len(df) == 15, f"结果行数不正确: {len(df)}"
        assert '因子' in df.columns, "缺少'因子'列"
        assert '贡献' in df.columns, "缺少'贡献'列"
        
        print("✓ 年度分析成功")
        print(f"✓ 分析结果: {len(df)} 个因子")
        print(f"✓ 数据列: {list(df.columns)}")
        
        return True
    except Exception as e:
        print(f"✗ 测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_factor_comparison(model):
    """测试6: 跨年对比"""
    print("\n" + "=" * 80)
    print("测试6: 跨年对比")
    print("=" * 80)
    
    try:
        years = [2020, 2021, 2022, 2023]
        df = model.compare_factor('央行购金', years)
        
        assert df is not None, "返回结果为空"
        assert isinstance(df, pd.DataFrame), "返回类型不是DataFrame"
        assert len(df) == len(years), f"结果行数不正确: {len(df)}"
        assert '年份' in df.columns, "缺少'年份'列"
        assert '贡献' in df.columns, "缺少'贡献'列"
        
        print("✓ 跨年对比成功")
        print(f"✓ 对比年份: {years}")
        print(f"✓ 数据列: {list(df.columns)}")
        
        return True
    except Exception as e:
        print(f"✗ 测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_validation(model):
    """测试7: 计算验证"""
    print("\n" + "=" * 80)
    print("测试7: 计算验证")
    print("=" * 80)
    
    try:
        result = model.validate_calculation(2023)
        
        assert result is not None, "返回结果为空"
        assert 'year' in result, "缺少year字段"
        assert 'predicted' in result, "缺少predicted字段"
        assert 'actual' in result, "缺少actual字段"
        assert 'error' in result, "缺少error字段"
        
        print("✓ 计算验证成功")
        print(f"✓ 2023年预测值: {result['predicted']:+.2%}")
        print(f"✓ 2023年实际值: {result['actual']:+.2%}")
        print(f"✓ 误差: {result['error']:+.2%}")
        
        return True
    except Exception as e:
        print(f"✗ 测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_export_functionality(model):
    """测试8: 导出功能"""
    print("\n" + "=" * 80)
    print("测试8: 导出功能")
    print("=" * 80)
    
    try:
        # 导出年度分析
        df = model.analyze_year(2020, export_csv=True)
        
        # 检查文件是否创建
        import os
        csv_file = 'results/factor_analysis_2020.csv'
        assert os.path.exists(csv_file), f"CSV文件未创建: {csv_file}"
        
        # 读取验证
        df_read = pd.read_csv(csv_file)
        assert len(df_read) > 0, "CSV文件为空"
        
        print("✓ 导出功能成功")
        print(f"✓ CSV文件已创建: {csv_file}")
        print(f"✓ 文件大小: {os.path.getsize(csv_file)} 字节")
        
        return True
    except Exception as e:
        print(f"✗ 测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False


def test_complete_analysis(model):
    """测试9: 完整分析流程"""
    print("\n" + "=" * 80)
    print("测试9: 完整分析流程")
    print("=" * 80)
    
    try:
        # 创建新实例运行完整流程
        model_new = EnhancedGoldPredictionModelV7()
        model_new.run_complete_analysis()
        
        # 检查输出文件
        import os
        csv_file = 'results/model_v7_complete_report.csv'
        assert os.path.exists(csv_file), f"完整报告未创建: {csv_file}"
        
        # 读取验证
        df = pd.read_csv(csv_file)
        expected_rows = 24 * 15  # 24年 × 15因子
        assert len(df) == expected_rows, f"数据行数不正确: {len(df)} (期望 {expected_rows})"
        
        print("✓ 完整分析流程成功")
        print(f"✓ 完整报告已创建: {csv_file}")
        print(f"✓ 数据行数: {len(df)}")
        print(f"✓ 数据列: {list(df.columns)}")
        
        return True
    except Exception as e:
        print(f"✗ 测试失败: {e}")
        import traceback
        traceback.print_exc()
        return False


def run_all_tests():
    """运行所有测试"""
    print("\n" + "=" * 80)
    print("开始测试 - 黄金价格预测模型 V7.0")
    print("=" * 80)
    
    results = []
    
    # 测试1: 初始化
    success, model = test_model_initialization()
    results.append(("模型初始化", success))
    
    if not success or model is None:
        print("\n❌ 初始化失败，无法继续测试")
        return
    
    # 测试2-3: 数据加载和权重优化
    success = test_data_loading(model)
    results.append(("数据加载", success))
    
    if success:
        success = test_weight_optimization(model)
        results.append(("权重优化", success))
    
    # 测试4-7: 核心功能
    if success:
        success = test_factor_trace(model)
        results.append(("因子追溯", success))
        
        success = test_year_analysis(model)
        results.append(("年度分析", success))
        
        success = test_factor_comparison(model)
        results.append(("跨年对比", success))
        
        success = test_validation(model)
        results.append(("计算验证", success))
        
        success = test_export_functionality(model)
        results.append(("导出功能", success))
    
    # 测试9: 完整流程（独立测试）
    success = test_complete_analysis(model)
    results.append(("完整分析流程", success))
    
    # 汇总结果
    print("\n" + "=" * 80)
    print("测试结果汇总")
    print("=" * 80)
    
    passed = 0
    failed = 0
    
    for test_name, success in results:
        status = "✓ 通过" if success else "✗ 失败"
        print(f"{test_name:20s}: {status}")
        if success:
            passed += 1
        else:
            failed += 1
    
    print("=" * 80)
    print(f"总计: {passed + failed} 个测试")
    print(f"通过: {passed} 个")
    print(f"失败: {failed} 个")
    print(f"成功率: {passed/(passed+failed)*100:.1f}%")
    print("=" * 80)
    
    if failed == 0:
        print("\n🎉 所有测试通过！模型功能正常。")
    else:
        print(f"\n⚠️  有 {failed} 个测试失败，请检查。")


if __name__ == "__main__":
    run_all_tests()
