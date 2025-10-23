# 黄金价格预测模型 - 因子分析

## 📊 概述

本模块实现了基于多因子分析的黄金价格预测模型，能够：
- 分析2000-2023年间影响黄金价格的关键因子
- 识别和追踪重大事件触发器
- 导出详细的分析报告和可视化图表

## 🔍 核心功能

### 1. 黄金价格预测模型 (`gold_price_model.py`)

模型包含8个主要因子：
- **美元指数**: 美元强弱对黄金价格的影响
- **通货膨胀率**: 通胀水平与黄金保值需求
- **实际利率**: 持有黄金的机会成本
- **地缘政治风险**: 避险需求驱动
- **央行购金**: 官方储备需求
- **市场情绪**: 投资者信心
- **原油价格**: 大宗商品联动效应
- **股市表现**: 资产配置转移

模型包含5个触发器（特殊事件）：
- **金融危机** (2008-2009)
- **量化宽松** (2009-2014)
- **疫情冲击** (2020-2021)
- **贸易战** (2018-2019)
- **主权债务危机** (2010-2012)

### 2. 导出和可视化 (`export_analysis.py`)

生成以下输出：

#### Excel报告 (`reports/factor_contribution_summary.xlsx`)
包含3个工作表：
- **因子贡献汇总**: 逐年分析结果，按贡献度排序
- **因子贡献矩阵**: 24年×8因子的详细矩阵
- **触发器激活记录**: 触发器时间线

#### 可视化图表
- **factor_heatmap.png**: 因子贡献热力图
- **factor_trends.png**: 年度因子贡献趋势图
- **trigger_statistics.png**: 触发器激活统计

## 🚀 使用方法

### 快速开始

```python
from gold_price_model import GoldPricePredictionModel

# 创建模型实例
model = GoldPricePredictionModel()

# 分析单个年份
result = model.analyze_year(2020)
print(f"2020年因子贡献: {result['factor_contributions']}")
print(f"触发器: {result['trigger_activations']}")

# 批量分析
results = model.get_all_years_analysis(2000, 2023)
```

### 生成完整报告

```bash
cd src/analysis
python export_analysis.py
```

或在Python中：

```python
from export_analysis import main

# 生成所有报告和图表
main()
```

### 自定义导出

```python
from gold_price_model import GoldPricePredictionModel
from export_analysis import (
    export_factor_contribution_summary,
    generate_factor_heatmap,
    generate_factor_trends,
    generate_trigger_statistics
)

model = GoldPricePredictionModel()

# 只生成Excel汇总
excel_file = export_factor_contribution_summary(model, 'custom_output/')

# 只生成热力图
heatmap_file = generate_factor_heatmap(model, 'custom_output/')
```

## 📈 分析结果示例

### 因子贡献分析（2020年）

```python
result = model.analyze_year(2020)

{
    'year': 2020,
    'factor_contributions': {
        '美元指数': -15.2,      # 美元走弱推高金价
        '实际利率': -18.4,      # 负实际利率利好黄金
        '地缘政治风险': 13.5,   # 疫情增加避险需求
        '央行购金': 10.8,       # 央行增持
        ...
    },
    'trigger_activations': {
        '疫情冲击': True,       # 2020年疫情爆发
        '金融危机': False,
        ...
    },
    'total_contribution': 18.6,     # 因子总贡献
    'trigger_contribution': 35.0,   # 触发器贡献
    'predicted_return': 53.6,       # 预测涨跌
    'actual_return': 24.6,          # 实际涨跌
    'difference': -29.0             # 差异
}
```

## 🧪 测试

运行测试套件：

```bash
# 运行所有测试
pytest tests/test_gold_price_analysis.py -v

# 运行特定测试
pytest tests/test_gold_price_analysis.py::TestGoldPriceModel -v
```

测试覆盖：
- ✅ 模型初始化
- ✅ 年份范围验证
- ✅ 因子贡献计算
- ✅ 触发器激活逻辑
- ✅ Excel导出功能
- ✅ 图表生成功能
- ✅ 完整报告生成

## 📁 输出文件结构

```
reports/
├── factor_contribution_summary.xlsx  # Excel汇总表
├── factor_heatmap.png                # 因子贡献热力图
├── factor_trends.png                 # 年度趋势图
└── trigger_statistics.png            # 触发器统计图
```

## 🔧 技术细节

### 因子权重

基础权重（可在模型中调整）：
```python
{
    '美元指数': -0.35,        # 负相关
    '通货膨胀率': 0.25,       # 正相关
    '实际利率': -0.20,        # 负相关
    '地缘政治风险': 0.15,     # 正相关
    '央行购金': 0.12,         # 正相关
    '市场情绪': 0.08,         # 正相关
    '原油价格': 0.10,         # 正相关
    '股市表现': -0.05,        # 负相关
}
```

### 触发器权重

```python
{
    '金融危机': 0.40,
    '量化宽松': 0.30,
    '疫情冲击': 0.35,
    '贸易战': 0.15,
    '主权债务危机': 0.25,
}
```

## 📊 可视化特性

### 热力图
- 色彩编码：绿色（正贡献）↔ 红色（负贡献）
- 时间跨度：2000-2023年
- 因子维度：8个主要因子

### 趋势图
- 多线图展示各因子贡献随时间变化
- 关键事件标注（金融危机、疫情等）
- 零基准线辅助判断

### 触发器统计
- 条形图显示激活频次
- 时间线热图显示激活时段

## 🎯 应用场景

1. **学术研究**: 分析影响黄金价格的宏观因素
2. **投资决策**: 理解当前市场环境对金价的影响
3. **风险管理**: 识别可能触发金价波动的事件
4. **政策分析**: 评估货币政策对黄金市场的影响

## 📝 注意事项

- 模型使用简化的模拟数据，实际应用需要对接真实数据源
- 因子权重基于经验设定，可根据回测结果优化
- 触发器识别基于历史事件，需定期更新
- 预测结果仅供参考，不构成投资建议

## 🔄 未来改进

- [ ] 集成实时数据源（FRED、Bloomberg等）
- [ ] 机器学习自动优化因子权重
- [ ] 扩展更多因子（VIX、比特币等）
- [ ] 添加短期预测功能
- [ ] Web界面展示
- [ ] 实时监控和警报系统

## 📧 联系方式

如有问题或建议，请联系项目维护者或提交Issue。

---

*最后更新: 2025-10-23*  
*版本: 1.0.0*
