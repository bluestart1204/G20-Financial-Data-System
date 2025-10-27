#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
黄金价格预测模型 V7.0
Gold Price Prediction Model V7.0

完整历史数据版本（2000-2023年，24年数据）
包含15个因子的综合分析模型
"""

import pandas as pd
import numpy as np
from datetime import datetime
from typing import Dict, List, Tuple, Optional


class GoldPricePredictionModelV7:
    """黄金价格预测模型 V7.0 - 完整历史数据版本"""
    
    def __init__(self):
        """初始化模型"""
        self.annual_data = {}
        self.factors = [
            'central_bank',      # 央行购金
            'M2',               # M2货币增速
            'industrial',       # 工业需求
            'mine_supply',      # 矿产金供应
            'recycling',        # 回收金供应
            'dollar',           # 美元指数
            'real_rate',        # 实际利率
            'vix',              # VIX风险指数
            'equity',           # 股市效应
            'momentum',         # 动量效应
            'mean_reversion',   # 均值回归
            'market_sentiment', # 市场情绪
            'etf_flow',         # ETF资金流向
            'policy_expectation', # 政策预期
            'dollar_carry'      # 美元利差
        ]
        self.setup_historical_data_with_new_factors()
        
    def setup_historical_data_with_new_factors(self):
        """设置完整的历史数据（2000-2023年）"""
        
        # 2000-2009年（科技泡沫 + 金融危机）
        self.annual_data[2000] = {
            'actual_return': -0.018,
            'price': (279, 274),
            'market_state': 'bear',
            'triggers': [],
            'central_bank': -0.15,
            'M2': 0.06,
            'industrial': 0.02,
            'mine_supply': 0.02,
            'recycling': 0.05,
            'dollar': 0.08,
            'real_rate': 0.04,
            'vix': 0.00,
            'equity': 0.00,
            'momentum': -0.05,
            'mean_reversion': 0.02,
            'market_sentiment': -0.05,
            'etf_flow': 0.00,
            'policy_expectation': 0.00,
            'dollar_carry': 0.04
        }
        
        self.annual_data[2001] = {
            'actual_return': 0.018,
            'price': (274, 279),
            'market_state': 'neutral',
            'triggers': ['geopolitical_shock'],
            'central_bank': -0.12,
            'M2': 0.08,
            'industrial': -0.02,
            'mine_supply': 0.02,
            'recycling': 0.05,
            'dollar': -0.02,
            'real_rate': 0.01,
            'vix': 0.15,
            'equity': -0.12,
            'momentum': 0.02,
            'mean_reversion': 0.01,
            'market_sentiment': 0.05,
            'etf_flow': 0.01,
            'policy_expectation': 0.02,
            'dollar_carry': 0.01
        }
        
        self.annual_data[2002] = {
            'actual_return': 0.247,
            'price': (279, 348),
            'market_state': 'bull',
            'triggers': ['trust_crisis', 'bull_market_acceleration'],
            'central_bank': -0.10,
            'M2': 0.07,
            'industrial': 0.00,
            'mine_supply': 0.02,
            'recycling': 0.06,
            'dollar': -0.10,
            'real_rate': -0.01,
            'vix': 0.12,
            'equity': -0.22,
            'momentum': 0.15,
            'mean_reversion': -0.05,
            'market_sentiment': 0.12,
            'etf_flow': 0.02,
            'policy_expectation': 0.03,
            'dollar_carry': -0.01
        }
        
        self.annual_data[2003] = {
            'actual_return': 0.184,
            'price': (348, 412),
            'market_state': 'bull',
            'triggers': ['ultra_low_rates'],
            'central_bank': -0.08,
            'M2': 0.05,
            'industrial': 0.03,
            'mine_supply': 0.02,
            'recycling': 0.06,
            'dollar': -0.12,
            'real_rate': -0.02,
            'vix': 0.05,
            'equity': 0.26,
            'momentum': 0.18,
            'mean_reversion': -0.08,
            'market_sentiment': 0.10,
            'etf_flow': 0.03,
            'policy_expectation': 0.04,
            'dollar_carry': -0.02
        }
        
        self.annual_data[2004] = {
            'actual_return': 0.053,
            'price': (412, 434),
            'market_state': 'neutral',
            'triggers': [],
            'central_bank': -0.05,
            'M2': 0.06,
            'industrial': 0.04,
            'mine_supply': 0.02,
            'recycling': 0.06,
            'dollar': 0.05,
            'real_rate': 0.00,
            'vix': 0.00,
            'equity': 0.09,
            'momentum': 0.05,
            'mean_reversion': -0.02,
            'market_sentiment': 0.03,
            'etf_flow': 0.02,
            'policy_expectation': 0.01,
            'dollar_carry': 0.00
        }
        
        self.annual_data[2005] = {
            'actual_return': 0.182,
            'price': (434, 513),
            'market_state': 'bull',
            'triggers': ['bull_market_acceleration'],
            'central_bank': -0.03,
            'M2': 0.07,
            'industrial': 0.05,
            'mine_supply': 0.02,
            'recycling': 0.07,
            'dollar': -0.08,
            'real_rate': -0.01,
            'vix': 0.00,
            'equity': 0.03,
            'momentum': 0.15,
            'mean_reversion': -0.06,
            'market_sentiment': 0.08,
            'etf_flow': 0.04,
            'policy_expectation': 0.02,
            'dollar_carry': -0.01
        }
        
        self.annual_data[2006] = {
            'actual_return': 0.227,
            'price': (513, 630),
            'market_state': 'bull',
            'triggers': ['bull_market_acceleration'],
            'central_bank': -0.02,
            'M2': 0.08,
            'industrial': 0.06,
            'mine_supply': 0.02,
            'recycling': 0.08,
            'dollar': -0.06,
            'real_rate': -0.02,
            'vix': 0.02,
            'equity': 0.14,
            'momentum': 0.20,
            'mean_reversion': -0.08,
            'market_sentiment': 0.12,
            'etf_flow': 0.06,
            'policy_expectation': 0.03,
            'dollar_carry': -0.02
        }
        
        self.annual_data[2007] = {
            'actual_return': 0.310,
            'price': (630, 838),
            'market_state': 'bull',
            'triggers': ['bull_market_frenzy'],
            'central_bank': 0.00,
            'M2': 0.10,
            'industrial': 0.07,
            'mine_supply': 0.02,
            'recycling': 0.09,
            'dollar': -0.10,
            'real_rate': -0.03,
            'vix': 0.08,
            'equity': 0.03,
            'momentum': 0.28,
            'mean_reversion': -0.12,
            'market_sentiment': 0.18,
            'etf_flow': 0.10,
            'policy_expectation': 0.05,
            'dollar_carry': -0.03
        }
        
        self.annual_data[2008] = {
            'actual_return': 0.043,
            'price': (838, 874),
            'market_state': 'crisis',
            'triggers': ['liquidity_crisis', 'forced_liquidation'],
            'central_bank': 0.02,
            'M2': 0.12,
            'industrial': -0.05,
            'mine_supply': 0.02,
            'recycling': 0.10,
            'dollar': 0.08,
            'real_rate': 0.02,
            'vix': 0.45,
            'equity': -0.38,
            'momentum': 0.05,
            'mean_reversion': 0.10,
            'market_sentiment': -0.15,
            'etf_flow': -0.05,
            'policy_expectation': 0.08,
            'dollar_carry': 0.02
        }
        
        self.annual_data[2009] = {
            'actual_return': 0.239,
            'price': (874, 1104),
            'market_state': 'bull',
            'triggers': ['qe_launch'],
            'central_bank': 0.05,
            'M2': 0.08,
            'industrial': 0.02,
            'mine_supply': 0.02,
            'recycling': 0.11,
            'dollar': -0.04,
            'real_rate': -0.05,
            'vix': -0.20,
            'equity': 0.23,
            'momentum': 0.22,
            'mean_reversion': -0.10,
            'market_sentiment': 0.15,
            'etf_flow': 0.08,
            'policy_expectation': 0.10,
            'dollar_carry': -0.05
        }
        
        # 2010-2019年（QE时代 + Taper恐慌）
        self.annual_data[2010] = {
            'actual_return': 0.296,
            'price': (1104, 1405),
            'market_state': 'bull',
            'triggers': ['bull_market_acceleration'],
            'central_bank': 0.08,
            'M2': 0.06,
            'industrial': 0.05,
            'mine_supply': 0.02,
            'recycling': 0.12,
            'dollar': -0.02,
            'real_rate': -0.06,
            'vix': -0.10,
            'equity': 0.13,
            'momentum': 0.28,
            'mean_reversion': -0.12,
            'market_sentiment': 0.18,
            'etf_flow': 0.12,
            'policy_expectation': 0.08,
            'dollar_carry': -0.06
        }
        
        self.annual_data[2011] = {
            'actual_return': 0.115,
            'price': (1405, 1566),
            'market_state': 'bubble',
            'triggers': ['bubble_peak', 'bull_market_frenzy'],
            'central_bank': 0.10,
            'M2': 0.08,
            'industrial': 0.06,
            'mine_supply': 0.02,
            'recycling': 0.13,
            'dollar': 0.02,
            'real_rate': -0.04,
            'vix': 0.12,
            'equity': 0.00,
            'momentum': 0.12,
            'mean_reversion': 0.05,
            'market_sentiment': 0.20,
            'etf_flow': 0.15,
            'policy_expectation': 0.06,
            'dollar_carry': -0.04
        }
        
        self.annual_data[2012] = {
            'actual_return': 0.073,
            'price': (1566, 1669),
            'market_state': 'neutral',
            'triggers': [],
            'central_bank': 0.08,
            'M2': 0.07,
            'industrial': 0.04,
            'mine_supply': 0.02,
            'recycling': 0.14,
            'dollar': 0.00,
            'real_rate': -0.03,
            'vix': 0.00,
            'equity': 0.13,
            'momentum': 0.08,
            'mean_reversion': 0.00,
            'market_sentiment': 0.05,
            'etf_flow': 0.08,
            'policy_expectation': 0.04,
            'dollar_carry': -0.03
        }
        
        self.annual_data[2013] = {
            'actual_return': -0.281,
            'price': (1669, 1204),
            'market_state': 'bear',
            'triggers': ['taper_tantrum', 'panic_selling'],
            'central_bank': 0.05,
            'M2': 0.06,
            'industrial': 0.02,
            'mine_supply': 0.03,
            'recycling': 0.15,
            'dollar': 0.10,
            'real_rate': 0.03,
            'vix': 0.08,
            'equity': 0.30,
            'momentum': -0.25,
            'mean_reversion': 0.15,
            'market_sentiment': -0.20,
            'etf_flow': -0.15,
            'policy_expectation': -0.10,
            'dollar_carry': 0.03
        }
        
        self.annual_data[2014] = {
            'actual_return': -0.020,
            'price': (1204, 1184),
            'market_state': 'bear',
            'triggers': ['strong_dollar_cycle'],
            'central_bank': 0.06,
            'M2': 0.05,
            'industrial': 0.01,
            'mine_supply': 0.03,
            'recycling': 0.12,
            'dollar': 0.12,
            'real_rate': 0.02,
            'vix': 0.02,
            'equity': 0.11,
            'momentum': -0.05,
            'mean_reversion': 0.05,
            'market_sentiment': -0.05,
            'etf_flow': -0.05,
            'policy_expectation': -0.03,
            'dollar_carry': 0.02
        }
        
        self.annual_data[2015] = {
            'actual_return': -0.105,
            'price': (1184, 1060),
            'market_state': 'bear',
            'triggers': ['strong_dollar_cycle'],
            'central_bank': 0.08,
            'M2': 0.06,
            'industrial': 0.00,
            'mine_supply': 0.03,
            'recycling': 0.11,
            'dollar': 0.10,
            'real_rate': 0.01,
            'vix': 0.05,
            'equity': -0.01,
            'momentum': -0.10,
            'mean_reversion': 0.08,
            'market_sentiment': -0.08,
            'etf_flow': -0.08,
            'policy_expectation': -0.05,
            'dollar_carry': 0.01
        }
        
        self.annual_data[2016] = {
            'actual_return': 0.087,
            'price': (1060, 1152),
            'market_state': 'neutral',
            'triggers': ['oversold_bounce'],
            'central_bank': 0.10,
            'M2': 0.07,
            'industrial': 0.01,
            'mine_supply': 0.03,
            'recycling': 0.10,
            'dollar': -0.03,
            'real_rate': -0.01,
            'vix': 0.03,
            'equity': 0.10,
            'momentum': 0.08,
            'mean_reversion': -0.05,
            'market_sentiment': 0.05,
            'etf_flow': 0.05,
            'policy_expectation': 0.02,
            'dollar_carry': -0.01
        }
        
        self.annual_data[2017] = {
            'actual_return': 0.134,
            'price': (1152, 1302),
            'market_state': 'bull',
            'triggers': [],
            'central_bank': 0.12,
            'M2': 0.06,
            'industrial': 0.03,
            'mine_supply': 0.03,
            'recycling': 0.10,
            'dollar': -0.10,
            'real_rate': -0.02,
            'vix': -0.05,
            'equity': 0.19,
            'momentum': 0.12,
            'mean_reversion': -0.06,
            'market_sentiment': 0.08,
            'etf_flow': 0.06,
            'policy_expectation': 0.03,
            'dollar_carry': -0.02
        }
        
        self.annual_data[2018] = {
            'actual_return': -0.019,
            'price': (1302, 1282),
            'market_state': 'neutral',
            'triggers': ['rate_hike_cycle'],
            'central_bank': 0.14,
            'M2': 0.05,
            'industrial': 0.02,
            'mine_supply': 0.03,
            'recycling': 0.09,
            'dollar': 0.05,
            'real_rate': 0.01,
            'vix': 0.08,
            'equity': -0.06,
            'momentum': -0.03,
            'mean_reversion': 0.03,
            'market_sentiment': 0.00,
            'etf_flow': 0.00,
            'policy_expectation': -0.02,
            'dollar_carry': 0.01
        }
        
        self.annual_data[2019] = {
            'actual_return': 0.171,
            'price': (1282, 1517),
            'market_state': 'bull',
            'triggers': [],
            'central_bank': 0.16,
            'M2': 0.06,
            'industrial': 0.01,
            'mine_supply': 0.03,
            'recycling': 0.09,
            'dollar': -0.01,
            'real_rate': -0.01,
            'vix': 0.00,
            'equity': 0.29,
            'momentum': 0.15,
            'mean_reversion': -0.08,
            'market_sentiment': 0.10,
            'etf_flow': 0.08,
            'policy_expectation': 0.05,
            'dollar_carry': -0.01
        }
        
        # 2020-2023年（疫情 + 加息周期）
        self.annual_data[2020] = {
            'actual_return': 0.249,
            'price': (1517, 1895),
            'market_state': 'crisis',
            'triggers': ['pandemic', 'liquidity_crisis_short', 'unlimited_qe'],
            'central_bank': 0.18,
            'M2': 0.244,
            'industrial': -0.03,
            'mine_supply': 0.02,
            'recycling': 0.08,
            'dollar': -0.02,
            'real_rate': -0.08,
            'vix': 0.40,
            'equity': 0.16,
            'momentum': 0.22,
            'mean_reversion': -0.10,
            'market_sentiment': 0.15,
            'etf_flow': 0.15,
            'policy_expectation': 0.10,
            'dollar_carry': -0.08
        }
        
        self.annual_data[2021] = {
            'actual_return': -0.036,
            'price': (1895, 1829),
            'market_state': 'neutral',
            'triggers': ['equity_diversion', 'rate_hike_expectation'],
            'central_bank': 0.10,
            'M2': 0.12,
            'industrial': 0.04,
            'mine_supply': 0.02,
            'recycling': 0.08,
            'dollar': 0.07,
            'real_rate': -0.05,
            'vix': -0.10,
            'equity': 0.27,
            'momentum': -0.05,
            'mean_reversion': 0.05,
            'market_sentiment': -0.03,
            'etf_flow': -0.03,
            'policy_expectation': -0.05,
            'dollar_carry': -0.05
        }
        
        self.annual_data[2022] = {
            'actual_return': 0.051,
            'price': (1829, 1820),
            'market_state': 'neutral',
            'triggers': ['rate_hike_cycle'],
            'central_bank': 0.12,
            'M2': 0.02,
            'industrial': 0.02,
            'mine_supply': 0.02,
            'recycling': 0.08,
            'dollar': 0.08,
            'real_rate': 0.02,
            'vix': 0.10,
            'equity': -0.19,
            'momentum': 0.05,
            'mean_reversion': 0.00,
            'market_sentiment': 0.05,
            'etf_flow': 0.02,
            'policy_expectation': 0.00,
            'dollar_carry': 0.02
        }
        
        self.annual_data[2023] = {
            'actual_return': 0.130,
            'price': (1820, 2063),
            'market_state': 'neutral',
            'triggers': [],
            'central_bank': 0.10,
            'M2': 0.035,
            'industrial': 0.00,
            'mine_supply': 0.01,
            'recycling': 0.10,
            'dollar': -0.02,
            'real_rate': 0.02,
            'vix': -0.02,
            'equity': 0.24,
            'momentum': 0.10,
            'mean_reversion': -0.02,
            'market_sentiment': 0.08,
            'etf_flow': 0.06,
            'policy_expectation': 0.03,
            'dollar_carry': -0.02
        }
    
    def validate_data_completeness(self):
        """验证数据完整性"""
        expected_years = list(range(2000, 2024))
        loaded_years = sorted(list(self.annual_data.keys()))
        
        missing = set(expected_years) - set(loaded_years)
        extra = set(loaded_years) - set(expected_years)
        
        if missing:
            raise AssertionError(f"缺失年份: {missing}")
        if extra:
            raise AssertionError(f"多余年份: {extra}")
        
        # 验证每年的数据完整性
        for year, data in self.annual_data.items():
            # 检查必要字段
            required_fields = ['actual_return', 'price', 'market_state', 'triggers']
            for field in required_fields:
                if field not in data:
                    raise AssertionError(f"{year}年缺少字段: {field}")
            
            # 检查所有因子
            for factor in self.factors:
                if factor not in data:
                    raise AssertionError(f"{year}年缺少因子: {factor}")
        
        print(f"✅ 数据完整性验证通过：24年数据完整")
        return True
    
    def get_summary_statistics(self) -> Dict:
        """获取汇总统计"""
        returns = [data['actual_return'] for data in self.annual_data.values()]
        
        stats = {
            'years_count': len(self.annual_data),
            'factors_count': len(self.factors),
            'avg_return': np.mean(returns),
            'std_return': np.std(returns),
            'max_return': max(returns),
            'min_return': min(returns),
            'positive_years': sum(1 for r in returns if r > 0),
            'negative_years': sum(1 for r in returns if r < 0)
        }
        
        return stats
    
    def run_complete_analysis(self):
        """运行完整分析"""
        print("=" * 60)
        print("黄金价格预测模型 V7.0 - 完整分析")
        print("=" * 60)
        print()
        
        # 数据加载信息
        years = sorted(self.annual_data.keys())
        print(f"✓ 已加载 {len(self.annual_data)} 年历史数据（{years[0]}-{years[-1]}）")
        print(f"✓ 已加载 {len(self.factors)} 个因子")
        print()
        
        # 验证数据完整性
        try:
            self.validate_data_completeness()
        except AssertionError as e:
            print(f"❌ 数据验证失败: {e}")
            return
        
        print()
        
        # 汇总统计
        stats = self.get_summary_statistics()
        print("📊 汇总统计：")
        print(f"  年份数量: {stats['years_count']}")
        print(f"  因子数量: {stats['factors_count']}")
        print(f"  平均收益率: {stats['avg_return']:.1%}")
        print(f"  收益率标准差: {stats['std_return']:.1%}")
        print(f"  最大收益率: {stats['max_return']:.1%}")
        print(f"  最小收益率: {stats['min_return']:.1%}")
        print(f"  正收益年份: {stats['positive_years']} 年")
        print(f"  负收益年份: {stats['negative_years']} 年")
        print()
        
        # 关键年份分析
        print("🎯 关键年份：")
        key_years = [2001, 2002, 2008, 2009, 2011, 2013, 2020]
        for year in key_years:
            if year in self.annual_data:
                data = self.annual_data[year]
                triggers_str = ', '.join(data['triggers']) if data['triggers'] else '无'
                print(f"  {year}: {data['actual_return']:+.1%} | 触发器: {triggers_str}")
        print()
        
        # 市场状态分布
        market_states = {}
        for data in self.annual_data.values():
            state = data['market_state']
            market_states[state] = market_states.get(state, 0) + 1
        
        print("📈 市场状态分布：")
        for state, count in sorted(market_states.items()):
            print(f"  {state}: {count} 年")
        print()
        
        # 触发器统计
        all_triggers = []
        for data in self.annual_data.values():
            all_triggers.extend(data['triggers'])
        
        trigger_counts = {}
        for trigger in all_triggers:
            trigger_counts[trigger] = trigger_counts.get(trigger, 0) + 1
        
        if trigger_counts:
            print("⚡ 触发器统计（前10）：")
            sorted_triggers = sorted(trigger_counts.items(), key=lambda x: x[1], reverse=True)
            for trigger, count in sorted_triggers[:10]:
                print(f"  {trigger}: {count} 次")
            print()
        
        print("=" * 60)
        print("✅ 分析完成！")
        print("=" * 60)


def main():
    """主函数"""
    model = GoldPricePredictionModelV7()
    model.run_complete_analysis()


if __name__ == "__main__":
    main()
