"""
简单测试 - 验证模型功能
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from analysis.gold_price_model_v7 import GoldPriceModelV7


def test_model_initialization():
    """测试模型初始化"""
    model = GoldPriceModelV7()
    assert model is not None
    assert len(model.factors_config) == 7
    print("✓ 模型初始化测试通过")


def test_analyze_year():
    """测试年份分析功能"""
    model = GoldPriceModelV7()
    
    # 测试2023年
    result = model.analyze_year(2023)
    
    assert result['year'] == 2023
    assert 'factors' in result
    assert len(result['factors']) == 7
    assert 'total_contribution' in result
    assert 'activated_triggers' in result
    assert 'trigger_contribution' in result
    assert 'predicted_change' in result
    assert 'actual_change' in result
    assert 'difference' in result
    assert 'validation_passed' in result
    
    print("✓ 年份分析功能测试通过")


def test_analyze_all_years():
    """测试所有年份分析"""
    model = GoldPriceModelV7()
    
    for year in range(2000, 2024):
        result = model.analyze_year(year)
        assert result['year'] == year
        assert len(result['factors']) == 7
    
    print("✓ 所有年份分析测试通过 (2000-2023)")


def test_factor_attributes():
    """测试因子属性"""
    model = GoldPriceModelV7()
    result = model.analyze_year(2023)
    
    for factor in result['factors']:
        assert hasattr(factor, 'name')
        assert hasattr(factor, 'category')
        assert hasattr(factor, 'raw_value')
        assert hasattr(factor, 'normalized_value')
        assert hasattr(factor, 'weight')
        assert hasattr(factor, 'transmission_coef')
        assert hasattr(factor, 'contribution')
        assert hasattr(factor, 'contribution_pct')
    
    print("✓ 因子属性测试通过")


def test_export_functions():
    """测试导出功能"""
    import os
    import tempfile
    
    model = GoldPriceModelV7()
    
    # 使用临时目录
    with tempfile.TemporaryDirectory() as tmpdir:
        # 测试单年导出
        filename = model.export_year_report(2023, tmpdir)
        assert os.path.exists(filename)
        
        # 测试所有年份导出
        excel_file, trigger_file = model.export_all_years(2000, 2003, tmpdir)
        assert os.path.exists(excel_file)
        assert os.path.exists(trigger_file)
    
    print("✓ 导出功能测试通过")


def main():
    """运行所有测试"""
    print("=" * 60)
    print("运行模型测试...")
    print("=" * 60)
    print()
    
    try:
        test_model_initialization()
        test_analyze_year()
        test_analyze_all_years()
        test_factor_attributes()
        test_export_functions()
        
        print()
        print("=" * 60)
        print("✅ 所有测试通过！")
        print("=" * 60)
        return 0
        
    except AssertionError as e:
        print()
        print("=" * 60)
        print(f"❌ 测试失败: {e}")
        print("=" * 60)
        return 1
    except Exception as e:
        print()
        print("=" * 60)
        print(f"❌ 错误: {e}")
        print("=" * 60)
        import traceback
        traceback.print_exc()
        return 1


if __name__ == '__main__':
    sys.exit(main())
