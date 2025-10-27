"""
黄金价格预测模型 V7.0 - Gold Price Prediction Model V7.0

深度分析黄金价格的因子贡献模型，支持逐年因子分析和触发器机制。
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple
from dataclasses import dataclass


@dataclass
class Factor:
    """因子数据类"""
    name: str  # 因子名称
    category: str  # 所属端（技术端、需求端、金融端等）
    raw_value: float  # 原始数值
    normalized_value: float  # 归一化值
    weight: float  # 优化权重
    transmission_coef: float  # 传导系数
    contribution: float  # 最终贡献
    
    @property
    def contribution_pct(self) -> float:
        """贡献百分比"""
        return self.contribution * 100


class GoldPriceModelV7:
    """
    黄金价格预测模型 V7.0
    
    功能：
    1. 逐年分析因子贡献（2000-2023）
    2. 计算归一化、权重、传导系数
    3. 触发器分析
    4. 生成详细报告
    """
    
    def __init__(self):
        """初始化模型"""
        # 定义因子配置
        self.factors_config = {
            '动量效应': {'category': '技术端', 'weight': 0.250},
            '央行购金': {'category': '需求端', 'weight': 0.198},
            '股市效应': {'category': '金融端', 'weight': 0.164},
            '美元指数': {'category': '金融端', 'weight': 0.150},
            '通胀预期': {'category': '宏观端', 'weight': 0.120},
            '地缘风险': {'category': '风险端', 'weight': 0.088},
            '实际利率': {'category': '金融端', 'weight': 0.030},
        }
        
        # 传导系数（默认为1.0，可根据市场环境调整）
        self.transmission_coefficient = 1.0
        
        # 触发器配置
        self.triggers = {
            '金融危机': {'threshold': 0.15, 'multiplier': 1.5},
            '极端事件': {'threshold': 0.20, 'multiplier': 2.0},
        }
        
        # 历史数据（模拟数据，实际应从数据库或文件加载）
        self._initialize_historical_data()
    
    def _initialize_historical_data(self):
        """初始化历史数据（2000-2023）"""
        # 这里使用模拟数据，实际应从真实数据源加载
        np.random.seed(42)
        years = range(2000, 2024)
        
        self.historical_data = {}
        for year in years:
            # 模拟各因子的原始数据（年度变化率）
            data = {
                '动量效应': np.random.uniform(-0.15, 0.25),
                '央行购金': np.random.uniform(-0.05, 0.15),
                '股市效应': np.random.uniform(-0.30, 0.30),
                '美元指数': np.random.uniform(-0.20, 0.15),
                '通胀预期': np.random.uniform(-0.10, 0.20),
                '地缘风险': np.random.uniform(-0.05, 0.25),
                '实际利率': np.random.uniform(-0.15, 0.10),
                '实际金价变化': np.random.uniform(-0.20, 0.30),  # 实际金价变化
            }
            self.historical_data[year] = data
    
    def analyze_year(self, year: int) -> Dict:
        """
        分析指定年份的因子贡献
        
        Args:
            year: 年份（2000-2023）
            
        Returns:
            包含详细分析结果的字典
        """
        if year not in self.historical_data:
            raise ValueError(f"年份 {year} 不在数据范围内（2000-2023）")
        
        year_data = self.historical_data[year]
        factors = []
        
        # 第1步：计算每个因子的贡献
        for factor_name, config in self.factors_config.items():
            raw_value = year_data[factor_name]
            normalized_value = raw_value  # 归一化处理（这里假设已归一化）
            weight = config['weight']
            transmission = self.transmission_coefficient
            
            # 计算贡献
            contribution = normalized_value * weight * transmission
            
            factor = Factor(
                name=factor_name,
                category=config['category'],
                raw_value=raw_value,
                normalized_value=normalized_value,
                weight=weight,
                transmission_coef=transmission,
                contribution=contribution
            )
            factors.append(factor)
        
        # 第2步：计算总贡献
        total_contribution = sum(f.contribution for f in factors)
        
        # 第3步：检查触发器
        trigger_contribution = 0.0
        activated_triggers = []
        
        # 简单的触发器逻辑：如果某些因子组合超过阈值
        if abs(total_contribution) > 0.10:
            # 检查是否激活特定触发器
            for trigger_name, trigger_config in self.triggers.items():
                if abs(total_contribution) > trigger_config['threshold']:
                    trigger_contribution = total_contribution * (trigger_config['multiplier'] - 1.0)
                    activated_triggers.append(trigger_name)
                    break
        
        # 第4步：计算预测值
        predicted_change = total_contribution + trigger_contribution
        actual_change = year_data['实际金价变化']
        
        # 第5步：计算差异
        difference = actual_change - predicted_change
        
        return {
            'year': year,
            'factors': factors,
            'total_contribution': total_contribution,
            'activated_triggers': activated_triggers,
            'trigger_contribution': trigger_contribution,
            'predicted_change': predicted_change,
            'actual_change': actual_change,
            'difference': difference,
            'validation_passed': abs(difference) < 0.01
        }
    
    def print_factor_trace(self, year: int, factor: Factor):
        """
        打印单个因子的追溯分析
        
        Args:
            year: 年份
            factor: 因子对象
        """
        print(f"\n📊 {year}年 {factor.name} 因子追溯\n")
        
        print("【第1层：原始数据】")
        print(f"  原始数值: {factor.raw_value:+.2f} ({factor.raw_value*100:+.1f}%)\n")
        
        print("【第2层：归一化处理】")
        print(f"  归一化值: {factor.normalized_value:+.2f}\n")
        
        print("【第3层：权重应用】")
        print(f"  优化权重: {factor.weight:.2f}")
        print(f"  原始贡献: {factor.normalized_value:+.2f} × {factor.weight:.2f} = {factor.normalized_value * factor.weight:+.3f}\n")
        
        print("【第4层：传导系数】")
        print(f"  最终传导: {factor.transmission_coef:.2f}\n")
        
        print("【第5层：最终影响】")
        print(f"  对金价贡献: {factor.contribution:+.3f} ({factor.contribution_pct:+.1f}%)")
    
    def print_factor_summary(self, result: Dict):
        """
        打印因子贡献汇总
        
        Args:
            result: analyze_year 返回的结果字典
        """
        year = result['year']
        factors = result['factors']
        
        print(f"\n📊 {year}年 所有因子贡献汇总\n")
        print("━" * 80)
        print(f"{'因子':<12} {'端':<8} {'原始值':<10} {'权重':<8} {'贡献':<10} {'占比':<10}")
        print("━" * 80)
        
        # 按贡献度排序
        sorted_factors = sorted(factors, key=lambda f: abs(f.contribution), reverse=True)
        
        total_abs_contribution = sum(abs(f.contribution) for f in factors)
        
        for factor in sorted_factors:
            proportion = (abs(factor.contribution) / total_abs_contribution * 100) if total_abs_contribution > 0 else 0
            print(f"{factor.name:<12} {factor.category:<8} {factor.raw_value*100:+6.1f}%  "
                  f"{factor.weight:<8.3f} {factor.contribution_pct:+6.1f}%  {proportion:+6.1f}%")
        
        print("━" * 80)
        print(f"总贡献（不含触发器）: {result['total_contribution']*100:+.1f}%")
        print(f"实际涨跌: {result['actual_change']*100:+.1f}%")
        print(f"触发器贡献: {result['trigger_contribution']*100:+.1f}%")
        print("━" * 80)
    
    def print_trigger_analysis(self, result: Dict):
        """
        打印触发器分析
        
        Args:
            result: analyze_year 返回的结果字典
        """
        year = result['year']
        print(f"\n📊 {year}年 触发器分析\n")
        
        if result['activated_triggers']:
            print(f"激活触发器: {', '.join(result['activated_triggers'])}")
            print(f"触发器贡献: {result['trigger_contribution']*100:+.1f}%")
        else:
            print("激活触发器: 无")
    
    def print_validation(self, result: Dict):
        """
        打印计算一致性验证
        
        Args:
            result: analyze_year 返回的结果字典
        """
        year = result['year']
        print(f"\n📊 {year}年 计算一致性验证\n")
        
        print(f"因子贡献总和: {result['total_contribution']:+.4f}")
        print(f"触发器贡献: {result['trigger_contribution']:+.4f}")
        print(f"模型预测: {result['predicted_change']:+.4f}")
        print(f"实际值: {result['actual_change']:+.4f}")
        print(f"差异: {result['difference']:.4f} ({'通过' if result['validation_passed'] else '未通过'})")
    
    def export_year_report(self, year: int, output_dir: str = 'reports'):
        """
        导出年度因子贡献报告
        
        Args:
            year: 年份
            output_dir: 输出目录
        """
        import os
        os.makedirs(output_dir, exist_ok=True)
        
        result = self.analyze_year(year)
        
        # 准备数据
        data = []
        for factor in result['factors']:
            data.append({
                '因子名称': factor.name,
                '所属端': factor.category,
                '原始数值': factor.raw_value,
                '归一化值': factor.normalized_value,
                '优化权重': factor.weight,
                '传导系数': factor.transmission_coef,
                '最终贡献': factor.contribution,
                '贡献百分比': factor.contribution_pct
            })
        
        df = pd.DataFrame(data)
        
        # 添加汇总信息
        summary_data = {
            '因子名称': '汇总',
            '所属端': '',
            '原始数值': '',
            '归一化值': '',
            '优化权重': '',
            '传导系数': '',
            '最终贡献': result['total_contribution'],
            '贡献百分比': result['total_contribution'] * 100
        }
        df = pd.concat([df, pd.DataFrame([summary_data])], ignore_index=True)
        
        # 导出CSV
        filename = os.path.join(output_dir, f'year_{year}_contributions.csv')
        df.to_csv(filename, index=False, encoding='utf-8-sig')
        
        return filename
    
    def export_all_years(self, start_year: int = 2000, end_year: int = 2023, 
                        output_dir: str = 'reports'):
        """
        导出所有年份的报告
        
        Args:
            start_year: 起始年份
            end_year: 结束年份
            output_dir: 输出目录
        """
        import os
        os.makedirs(output_dir, exist_ok=True)
        
        # 1. 生成每年的单独报告
        for year in range(start_year, end_year + 1):
            self.export_year_report(year, output_dir)
            print(f"✓ 已生成 {year} 年度报告")
        
        # 2. 生成汇总Excel - 因子贡献
        all_data = []
        for year in range(start_year, end_year + 1):
            result = self.analyze_year(year)
            for factor in result['factors']:
                all_data.append({
                    '年份': year,
                    '因子名称': factor.name,
                    '所属端': factor.category,
                    '原始数值': factor.raw_value,
                    '归一化值': factor.normalized_value,
                    '优化权重': factor.weight,
                    '传导系数': factor.transmission_coef,
                    '最终贡献': factor.contribution,
                    '贡献百分比': factor.contribution_pct
                })
        
        df_all = pd.DataFrame(all_data)
        excel_file = os.path.join(output_dir, 'factor_contribution_2000_2023.xlsx')
        df_all.to_excel(excel_file, index=False, engine='openpyxl')
        print(f"\n✓ 已生成因子贡献汇总表: {excel_file}")
        
        # 3. 生成汇总Excel - 触发器分析
        trigger_data = []
        for year in range(start_year, end_year + 1):
            result = self.analyze_year(year)
            trigger_data.append({
                '年份': year,
                '激活触发器': ', '.join(result['activated_triggers']) if result['activated_triggers'] else '无',
                '触发器贡献': result['trigger_contribution'],
                '触发器贡献百分比': result['trigger_contribution'] * 100,
                '总贡献': result['total_contribution'],
                '预测变化': result['predicted_change'],
                '实际变化': result['actual_change'],
                '差异': result['difference'],
                '验证通过': result['validation_passed']
            })
        
        df_triggers = pd.DataFrame(trigger_data)
        trigger_excel = os.path.join(output_dir, 'trigger_analysis_2000_2023.xlsx')
        df_triggers.to_excel(trigger_excel, index=False, engine='openpyxl')
        print(f"✓ 已生成触发器分析汇总表: {trigger_excel}")
        
        return excel_file, trigger_excel


def main():
    """主函数：演示模型使用"""
    print("=" * 80)
    print("黄金价格预测模型 V7.0 - 因子贡献分析")
    print("=" * 80)
    
    # 创建模型实例
    model = GoldPriceModelV7()
    
    # 示例：分析2023年
    print("\n【示例】2023年详细分析\n")
    result_2023 = model.analyze_year(2023)
    
    # 打印单个因子追溯（央行购金）
    central_bank_factor = [f for f in result_2023['factors'] if f.name == '央行购金'][0]
    model.print_factor_trace(2023, central_bank_factor)
    
    # 打印因子贡献汇总
    model.print_factor_summary(result_2023)
    
    # 打印触发器分析
    model.print_trigger_analysis(result_2023)
    
    # 打印验证结果
    model.print_validation(result_2023)
    
    print("\n" + "=" * 80)
    print("开始生成2000-2023年完整报告...")
    print("=" * 80 + "\n")
    
    # 导出所有年份报告
    model.export_all_years(2000, 2023)
    
    print("\n" + "=" * 80)
    print("✅ 所有分析完成！")
    print("=" * 80)


if __name__ == '__main__':
    main()
