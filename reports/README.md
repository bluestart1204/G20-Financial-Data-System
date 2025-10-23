# 黄金价格可视化报告 / Gold Price Visualization Reports

本目录包含黄金价格分析的可视化报告和数据文件。

This directory contains visualization reports and data files for gold price analysis.

## 📁 文件说明 / Files Description

### 1. gold_price_complete_visualization.png
**黄金价格综合可视化图表 (2000-2023)**

- **尺寸**: 24×14英寸 (7200×4200像素)
- **分辨率**: 300 DPI
- **格式**: PNG
- **内容**:
  - 2000-2023年金价周度走势曲线
  - 每年的预测值 vs 实际值标注
  - Top驱动因子及其贡献度
  - 关键事件触发器标记
  - 关键年份高亮显示（2008/2011/2013/2020）

**Features**:
  - Weekly gold price trend (2000-2023)
  - Annual predictions vs. actual values
  - Top driving factors and contributions
  - Key event trigger markers
  - Highlighted key years (2008/2011/2013/2020)

### 2. annual_summary.csv
**年度数据摘要表**

包含每年的详细数据：
- 年份
- 预测收益率
- 实际收益率
- 预测误差
- Top因子名称
- Top因子贡献度
- 触发器事件

**Contains annual data**:
- Year
- Predicted return
- Actual return
- Prediction error
- Top factor name
- Top factor contribution
- Trigger events

## 🚀 如何生成报告 / How to Generate Reports

### 前提条件 / Prerequisites

```bash
# 安装依赖 / Install dependencies
pip install pandas numpy matplotlib yfinance pillow
```

### 运行脚本 / Run Script

```bash
# 在项目根目录执行 / Run from project root
python create_gold_price_chart.py
```

脚本会自动：
1. 下载2000-2023年的黄金价格周度数据
2. 生成综合可视化图表
3. 保存年度数据摘要CSV文件

The script will automatically:
1. Download weekly gold price data (2000-2023)
2. Generate comprehensive visualization
3. Save annual summary CSV file

## 📊 图表说明 / Chart Legend

### 颜色编码 / Color Coding
- **绿色边框**: 金价上涨年份 / Green border: Years with positive returns
- **红色边框**: 金价下跌年份 / Red border: Years with negative returns
- **加粗边框**: 关键年份 / Bold border: Key years (2008, 2011, 2013, 2020)
- **黄色背景**: 重大金融危机年份 / Yellow background: Major financial crisis years

### 事件标记 / Event Markers
- **蓝色箭头**: 正面事件（如QE政策）/ Blue arrows: Positive events (e.g., QE policies)
- **红色箭头**: 负面事件（如危机）/ Red arrows: Negative events (e.g., crises)
- **橙色箭头**: 中性/混合影响事件 / Orange arrows: Neutral/mixed impact events

## 📈 关键年份分析 / Key Years Analysis

### 2008年 - 金融危机 / Financial Crisis
- 实际收益: +4.3%
- Top因子: VIX风险指数 (+8.9%)
- 触发器: 流动性危机

### 2011年 - 主权债务危机 / Sovereign Debt Crisis
- 实际收益: +10.2%
- Top因子: VIX风险指数 (+7.6%)
- 触发器: 美国主权评级下调

### 2013年 - Taper恐慌 / Taper Tantrum
- 实际收益: -28.1%
- Top因子: 美联储Taper (-9.1%)
- 触发器: Taper恐慌

### 2020年 - 疫情+无限QE / Pandemic + Unlimited QE
- 实际收益: +24.9%
- Top因子: 动量因子 (+6.25%)
- 触发器: 疫情爆发、无限QE

## 💡 数据来源 / Data Sources

- **金价数据**: Yahoo Finance (GC=F 黄金期货)
- **预测模型**: 基于多因子模型的年度预测
- **因子分析**: 包括VIX、美元指数、实际利率、央行购金等

**Gold Price Data**: Yahoo Finance (GC=F Gold Futures)
**Prediction Model**: Multi-factor model annual predictions
**Factor Analysis**: Including VIX, USD Index, Real Interest Rates, Central Bank Purchases, etc.

## 📝 更新日志 / Changelog

### 2024-10-23
- ✅ 创建初始可视化脚本
- ✅ 生成2000-2023年完整图表
- ✅ 添加24年年度数据标注
- ✅ 实现触发器事件标记
- ✅ 创建年度摘要CSV文件

## 📧 联系方式 / Contact

如有问题或建议，请通过GitHub Issues反馈。

For questions or suggestions, please submit via GitHub Issues.
