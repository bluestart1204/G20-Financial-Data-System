"""
测试黄金价格预测模型和导出功能
Test Gold Price Prediction Model and Export Functionality
"""

import os
import sys
import unittest
import pandas as pd
from pathlib import Path

# 添加src/analysis到路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src', 'analysis'))

from gold_price_model import GoldPricePredictionModel
import export_analysis


class TestGoldPriceModel(unittest.TestCase):
    """测试黄金价格预测模型"""
    
    def setUp(self):
        """初始化测试"""
        self.model = GoldPricePredictionModel()
    
    def test_model_initialization(self):
        """测试模型初始化"""
        self.assertIsNotNone(self.model)
        self.assertEqual(len(self.model.factors), 8)
        self.assertEqual(len(self.model.triggers), 5)
    
    def test_analyze_year_structure(self):
        """测试analyze_year返回结构"""
        result = self.model.analyze_year(2020)
        
        # 检查必需的键
        required_keys = [
            'year', 'factor_contributions', 'trigger_contributions',
            'trigger_activations', 'total_contribution', 'trigger_contribution',
            'predicted_return', 'actual_return', 'difference'
        ]
        
        for key in required_keys:
            self.assertIn(key, result)
        
        # 检查年份
        self.assertEqual(result['year'], 2020)
        
        # 检查因子贡献数量
        self.assertEqual(len(result['factor_contributions']), 8)
        
        # 检查触发器数量
        self.assertEqual(len(result['trigger_contributions']), 5)
    
    def test_analyze_year_range(self):
        """测试年份范围验证"""
        # 测试有效年份
        result = self.model.analyze_year(2000)
        self.assertEqual(result['year'], 2000)
        
        result = self.model.analyze_year(2023)
        self.assertEqual(result['year'], 2023)
        
        # 测试无效年份
        with self.assertRaises(ValueError):
            self.model.analyze_year(1999)
        
        with self.assertRaises(ValueError):
            self.model.analyze_year(2024)
    
    def test_factor_contributions_calculation(self):
        """测试因子贡献计算"""
        result = self.model.analyze_year(2010)
        
        # 验证所有因子都有贡献值
        for factor_name in self.model.factors.keys():
            self.assertIn(factor_name, result['factor_contributions'])
            self.assertIsInstance(result['factor_contributions'][factor_name], float)
    
    def test_trigger_activations(self):
        """测试触发器激活逻辑"""
        # 2008年应该激活金融危机触发器
        result_2008 = self.model.analyze_year(2008)
        self.assertTrue(result_2008['trigger_activations']['金融危机'])
        
        # 2020年应该激活疫情冲击触发器
        result_2020 = self.model.analyze_year(2020)
        self.assertTrue(result_2020['trigger_activations']['疫情冲击'])
        
        # 2018年应该激活贸易战触发器
        result_2018 = self.model.analyze_year(2018)
        self.assertTrue(result_2018['trigger_activations']['贸易战'])
    
    def test_get_all_years_analysis(self):
        """测试批量年份分析"""
        results = self.model.get_all_years_analysis(2000, 2023)
        
        # 应该返回24年的数据
        self.assertEqual(len(results), 24)
        
        # 检查年份连续性
        years = [r['year'] for r in results]
        self.assertEqual(years, list(range(2000, 2024)))


class TestExportFunctionality(unittest.TestCase):
    """测试导出功能"""
    
    def setUp(self):
        """初始化测试"""
        self.model = GoldPricePredictionModel()
        self.test_output_dir = '/tmp/test_reports'
        Path(self.test_output_dir).mkdir(parents=True, exist_ok=True)
    
    def tearDown(self):
        """清理测试文件"""
        import shutil
        if os.path.exists(self.test_output_dir):
            shutil.rmtree(self.test_output_dir)
    
    def test_export_factor_contribution_summary(self):
        """测试导出因子贡献汇总表"""
        output_file = export_analysis.export_factor_contribution_summary(
            self.model, self.test_output_dir
        )
        
        # 检查文件是否创建
        self.assertTrue(os.path.exists(output_file))
        
        # 检查Excel文件内容
        xlsx = pd.ExcelFile(output_file)
        
        # 检查工作表
        self.assertIn('因子贡献汇总', xlsx.sheet_names)
        self.assertIn('因子贡献矩阵', xlsx.sheet_names)
        self.assertIn('触发器激活记录', xlsx.sheet_names)
        
        # 读取汇总表
        df_summary = pd.read_excel(output_file, sheet_name='因子贡献汇总')
        self.assertEqual(len(df_summary), 24)  # 2000-2023共24年
        
        # 检查必要列
        required_columns = ['年份', '因子贡献总和', '触发器贡献', '实际涨跌', '差异']
        for col in required_columns:
            self.assertIn(col, df_summary.columns)
    
    def test_generate_factor_heatmap(self):
        """测试生成因子贡献热力图"""
        output_file = export_analysis.generate_factor_heatmap(
            self.model, self.test_output_dir
        )
        
        # 检查文件是否创建
        self.assertTrue(os.path.exists(output_file))
        self.assertTrue(output_file.endswith('.png'))
        
        # 检查文件大小（应该大于0）
        self.assertGreater(os.path.getsize(output_file), 0)
    
    def test_generate_factor_trends(self):
        """测试生成年度因子贡献趋势图"""
        output_file = export_analysis.generate_factor_trends(
            self.model, self.test_output_dir
        )
        
        # 检查文件是否创建
        self.assertTrue(os.path.exists(output_file))
        self.assertTrue(output_file.endswith('.png'))
        
        # 检查文件大小
        self.assertGreater(os.path.getsize(output_file), 0)
    
    def test_generate_trigger_statistics(self):
        """测试生成触发器激活统计图表"""
        output_file = export_analysis.generate_trigger_statistics(
            self.model, self.test_output_dir
        )
        
        # 检查文件是否创建
        self.assertTrue(os.path.exists(output_file))
        self.assertTrue(output_file.endswith('.png'))
        
        # 检查文件大小
        self.assertGreater(os.path.getsize(output_file), 0)


class TestReportGeneration(unittest.TestCase):
    """测试完整报告生成流程"""
    
    def test_reports_directory_exists(self):
        """测试reports目录存在且包含所有文件"""
        project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        reports_dir = os.path.join(project_root, 'reports')
        
        # 检查目录存在
        self.assertTrue(os.path.exists(reports_dir))
        
        # 检查必要文件
        required_files = [
            'factor_contribution_summary.xlsx',
            'factor_heatmap.png',
            'factor_trends.png',
            'trigger_statistics.png'
        ]
        
        for filename in required_files:
            file_path = os.path.join(reports_dir, filename)
            self.assertTrue(
                os.path.exists(file_path),
                f"Required file not found: {filename}"
            )
            self.assertGreater(
                os.path.getsize(file_path), 0,
                f"File is empty: {filename}"
            )


if __name__ == '__main__':
    # 运行测试
    unittest.main(verbosity=2)
