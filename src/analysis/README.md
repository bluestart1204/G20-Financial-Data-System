# 黄金价格预测模型 V7.0

## 概述

这是一个基于历史数据的黄金价格预测模型，包含完整的2000-2023年（24年）历史数据和15个关键因子。

## 主要特性

- ✅ **完整的历史数据**：涵盖2000-2023年全部24年
- ✅ **15个关键因子**：包括央行购金、M2货币增速、美元指数、实际利率等
- ✅ **市场状态识别**：牛市、熊市、危机、中性、泡沫
- ✅ **触发器系统**：识别关键市场事件和异常情况
- ✅ **数据验证**：自动验证数据完整性和准确性

## 快速开始

### 运行模型

```bash
python src/analysis/enhanced_model_v7.py
```

### 运行测试

```bash
python tests/test_enhanced_model_v7.py
```

### 在代码中使用

```python
from src.analysis.enhanced_model_v7 import GoldPricePredictionModelV7

# 创建模型实例
model = GoldPricePredictionModelV7()

# 运行完整分析
model.run_complete_analysis()

# 获取汇总统计
stats = model.get_summary_statistics()
print(f"平均收益率: {stats['avg_return']:.2%}")

# 访问特定年份的数据
data_2020 = model.annual_data[2020]
print(f"2020年收益率: {data_2020['actual_return']:.2%}")
print(f"2020年触发器: {data_2020['triggers']}")
```

## 数据结构

### 年度数据格式

每年的数据包含以下字段：

```python
{
    'actual_return': 0.130,      # 实际收益率
    'price': (1820, 2063),       # (起始价格, 结束价格)
    'market_state': 'neutral',   # 市场状态
    'triggers': [],              # 触发器列表
    
    # 15个因子
    'central_bank': 0.10,        # 央行购金
    'M2': 0.035,                 # M2货币增速
    'industrial': 0.00,          # 工业需求
    'mine_supply': 0.01,         # 矿产金供应
    'recycling': 0.10,           # 回收金供应
    'dollar': -0.02,             # 美元指数
    'real_rate': 0.02,           # 实际利率
    'vix': -0.02,                # VIX风险指数
    'equity': 0.24,              # 股市效应
    'momentum': 0.10,            # 动量效应
    'mean_reversion': -0.02,     # 均值回归
    'market_sentiment': 0.08,    # 市场情绪
    'etf_flow': 0.06,            # ETF资金流向
    'policy_expectation': 0.03,  # 政策预期
    'dollar_carry': -0.02        # 美元利差
}
```

### 市场状态

- `bull`: 牛市
- `bear`: 熊市
- `neutral`: 中性
- `crisis`: 危机
- `bubble`: 泡沫

### 触发器类型

- `geopolitical_shock`: 地缘政治冲击（如911）
- `trust_crisis`: 信任危机
- `ultra_low_rates`: 超低利率
- `liquidity_crisis`: 流动性危机
- `forced_liquidation`: 强制清算
- `qe_launch`: QE启动
- `bull_market_acceleration`: 牛市加速
- `bull_market_frenzy`: 牛市狂热
- `bubble_peak`: 泡沫顶点
- `taper_tantrum`: Taper恐慌
- `panic_selling`: 恐慌性抛售
- `strong_dollar_cycle`: 强美元周期
- `oversold_bounce`: 超卖反弹
- `rate_hike_cycle`: 加息周期
- `pandemic`: 疫情
- `unlimited_qe`: 无限QE
- `equity_diversion`: 股市分流
- `rate_hike_expectation`: 加息预期

## 关键历史事件

### 2000-2009年（科技泡沫 + 金融危机）

- **2001年**：911恐袭，金价上涨1.8%
- **2002年**：安然/世通丑闻，金价暴涨24.7%
- **2007年**：牛市狂热，金价上涨31.0%
- **2008年**：雷曼破产，流动性危机，金价上涨4.3%
- **2009年**：QE1启动，金价上涨23.9%

### 2010-2019年（QE时代 + Taper恐慌）

- **2010年**：QE2预期，金价上涨29.6%
- **2011年**：历史高点$1917，年末收于$1566（+11.5%）
- **2013年**：Taper恐慌，金价暴跌28.1%
- **2016年**：超卖反弹，金价上涨8.7%

### 2020-2023年（疫情 + 加息周期）

- **2020年**：COVID-19疫情，无限QE，金价上涨24.9%
- **2021年**：股市分流，金价下跌3.6%
- **2022年**：加息周期，金价微涨5.1%
- **2023年**：央行购金，金价上涨13.0%

## 统计摘要

- **时间范围**：2000-2023年（24年）
- **平均年收益率**：9.7%
- **收益率标准差**：13.6%
- **最大年收益率**：31.0%（2007年）
- **最小年收益率**：-28.1%（2013年）
- **正收益年份**：18年（75%）
- **负收益年份**：6年（25%）

## 市场状态分布

- 牛市（bull）：9年
- 中性（neutral）：8年
- 熊市（bear）：4年
- 危机（crisis）：2年
- 泡沫（bubble）：1年

## 数据来源

- 金价：Kitco Historical Gold Prices
- 央行购金：World Gold Council
- VIX：CBOE
- 股市：S&P 500 Index
- M2：Federal Reserve Economic Data (FRED)

## 许可证

MIT License
