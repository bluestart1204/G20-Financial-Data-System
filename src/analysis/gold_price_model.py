"""
黄金价格预测模型
Gold Price Prediction Model with Factor Analysis
"""

import pandas as pd
import numpy as np
from typing import Dict, List, Tuple


class GoldPricePredictionModel:
    """
    黄金价格预测模型，基于多因子分析
    Gold price prediction model based on multi-factor analysis
    """
    
    def __init__(self):
        """初始化模型"""
        # 定义影响黄金价格的主要因子
        self.factors = {
            '美元指数': 'USD_Index',
            '通货膨胀率': 'Inflation',
            '实际利率': 'Real_Interest_Rate',
            '地缘政治风险': 'Geopolitical_Risk',
            '央行购金': 'Central_Bank_Buying',
            '市场情绪': 'Market_Sentiment',
            '原油价格': 'Oil_Price',
            '股市表现': 'Stock_Market',
        }
        
        # 定义触发器（特殊事件）
        self.triggers = {
            '金融危机': 'Financial_Crisis',
            '量化宽松': 'Quantitative_Easing',
            '疫情冲击': 'Pandemic_Shock',
            '贸易战': 'Trade_War',
            '主权债务危机': 'Sovereign_Debt_Crisis',
        }
        
        # 历史数据和权重（基于经验设定）
        self._initialize_historical_weights()
    
    def _initialize_historical_weights(self):
        """初始化历史权重和数据"""
        # 这里使用简化的模拟数据，实际应用中应从数据库或API获取
        # 各年份的因子基础权重
        self.base_weights = {
            '美元指数': -0.35,
            '通货膨胀率': 0.25,
            '实际利率': -0.20,
            '地缘政治风险': 0.15,
            '央行购金': 0.12,
            '市场情绪': 0.08,
            '原油价格': 0.10,
            '股市表现': -0.05,
        }
        
        # 触发器权重
        self.trigger_weights = {
            '金融危机': 0.40,
            '量化宽松': 0.30,
            '疫情冲击': 0.35,
            '贸易战': 0.15,
            '主权债务危机': 0.25,
        }
        
        # 历史年份黄金价格实际涨跌（简化数据，单位：%）
        self.historical_returns = {
            2000: -5.4, 2001: 1.2, 2002: 24.7, 2003: 19.6, 2004: 5.2,
            2005: 18.2, 2006: 23.2, 2007: 31.4, 2008: 5.8, 2009: 23.9,
            2010: 29.8, 2011: 10.2, 2012: 7.0, 2013: -28.3, 2014: -1.5,
            2015: -10.4, 2016: 8.6, 2017: 13.1, 2018: -1.6, 2019: 18.3,
            2020: 24.6, 2021: -3.6, 2022: -0.3, 2023: 13.4,
        }
    
    def _get_factor_values(self, year: int) -> Dict[str, float]:
        """
        获取指定年份的因子值（归一化）
        
        Args:
            year: 年份
            
        Returns:
            因子名称到值的字典
        """
        # 这里使用模拟数据，实际应用中应从真实数据源获取
        np.random.seed(year)  # 使用年份作为种子保证可重复性
        
        factor_values = {}
        for factor_name in self.factors.keys():
            # 生成 -1 到 1 之间的归一化值
            base_value = np.random.uniform(-1, 1)
            
            # 根据历史事件调整某些因子值
            if year == 2008 and factor_name == '地缘政治风险':
                base_value = 0.9  # 2008金融危机
            elif year == 2020 and factor_name == '地缘政治风险':
                base_value = 0.85  # 2020疫情
            elif year >= 2009 and year <= 2013 and factor_name == '实际利率':
                base_value = -0.8  # 低利率环境
            elif year in [2018, 2019] and factor_name == '地缘政治风险':
                base_value = 0.6  # 贸易战
                
            factor_values[factor_name] = base_value
            
        return factor_values
    
    def _get_trigger_activations(self, year: int) -> Dict[str, bool]:
        """
        获取指定年份的触发器激活状态
        
        Args:
            year: 年份
            
        Returns:
            触发器名称到激活状态的字典
        """
        activations = {trigger: False for trigger in self.triggers.keys()}
        
        # 基于历史事件设置触发器
        if year in [2008, 2009]:
            activations['金融危机'] = True
        if year in range(2009, 2015):
            activations['量化宽松'] = True
        if year in [2020, 2021]:
            activations['疫情冲击'] = True
        if year in [2018, 2019]:
            activations['贸易战'] = True
        if year in [2010, 2011, 2012]:
            activations['主权债务危机'] = True
            
        return activations
    
    def analyze_year(self, year: int) -> Dict:
        """
        分析指定年份的因子贡献
        
        Args:
            year: 年份（2000-2023）
            
        Returns:
            包含分析结果的字典，包括：
            - factor_contributions: 各因子的贡献度
            - trigger_contributions: 触发器贡献
            - total_contribution: 总贡献（不含触发器）
            - trigger_contribution: 触发器总贡献
            - predicted_return: 预测涨跌
            - actual_return: 实际涨跌
            - difference: 差异
        """
        if year < 2000 or year > 2023:
            raise ValueError("Year must be between 2000 and 2023")
        
        # 获取因子值
        factor_values = self._get_factor_values(year)
        
        # 计算各因子贡献
        factor_contributions = {}
        total_contribution = 0.0
        
        for factor_name, weight in self.base_weights.items():
            contribution = factor_values[factor_name] * weight * 100
            factor_contributions[factor_name] = contribution
            total_contribution += contribution
        
        # 获取触发器状态
        trigger_activations = self._get_trigger_activations(year)
        
        # 计算触发器贡献
        trigger_contributions = {}
        trigger_contribution = 0.0
        
        for trigger_name, activated in trigger_activations.items():
            if activated:
                contribution = self.trigger_weights[trigger_name] * 100
                trigger_contributions[trigger_name] = contribution
                trigger_contribution += contribution
            else:
                trigger_contributions[trigger_name] = 0.0
        
        # 预测涨跌 = 因子贡献 + 触发器贡献
        predicted_return = total_contribution + trigger_contribution
        
        # 实际涨跌
        actual_return = self.historical_returns.get(year, 0.0)
        
        # 差异
        difference = actual_return - predicted_return
        
        return {
            'year': year,
            'factor_contributions': factor_contributions,
            'trigger_contributions': trigger_contributions,
            'trigger_activations': trigger_activations,
            'total_contribution': total_contribution,
            'trigger_contribution': trigger_contribution,
            'predicted_return': predicted_return,
            'actual_return': actual_return,
            'difference': difference,
        }
    
    def get_all_years_analysis(self, start_year: int = 2000, end_year: int = 2023) -> List[Dict]:
        """
        获取多年分析结果
        
        Args:
            start_year: 起始年份
            end_year: 结束年份
            
        Returns:
            各年分析结果列表
        """
        results = []
        for year in range(start_year, end_year + 1):
            results.append(self.analyze_year(year))
        return results
