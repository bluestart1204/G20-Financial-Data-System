# 示例输出说明

本目录包含黄金价格预测模型 V7.0 的示例输出。

## 文件说明

运行 `model.run_complete_analysis()` 后，将在 `results/` 目录生成以下文件：

### 1. model_v7_complete_report.csv
完整报告，包含所有年份和所有因子的数据。

**字段:**
- 年份: 2000-2023
- 因子: 15个因子的中文名称
- 端: 因子所属类别（需求端/供给端/金融端/技术端/情绪端）
- 原始值: 因子的原始变化值
- 权重: 优化后的因子权重
- 传导系数: 市场状态传导系数
- 贡献: 因子对金价的最终贡献
- 实际涨跌: 当年金价实际涨跌

**数据量:** 24年 × 15因子 = 360行

### 2. factor_contribution_trace_2000_2023.xlsx
Excel格式的完整报告，与CSV内容相同，便于在Excel中分析。

### 3. factor_analysis_{year}.csv
单年因子分析结果，通过 `model.analyze_year(year, export_csv=True)` 生成。

**字段:**
- 因子
- 端
- 原始值
- 权重
- 贡献
- 占比

## 使用说明

### 查看完整报告
```python
import pandas as pd

# 读取完整报告
df = pd.read_csv('results/model_v7_complete_report.csv')

# 查看2023年的数据
df_2023 = df[df['年份'] == 2023]
print(df_2023)

# 查看央行购金的历史数据
df_central = df[df['因子'] == '央行购金']
print(df_central)
```

### 分析特定年份
```python
# 读取单年分析
df = pd.read_csv('results/factor_analysis_2023.csv')

# 查看前5大驱动因子
print(df.head())
```

### 在Excel中分析
打开 `factor_contribution_trace_2000_2023.xlsx`，可以使用Excel的筛选、排序、透视表等功能进行分析。

## 示例查询

### 找出所有年份中央行购金的贡献
```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('results/model_v7_complete_report.csv')
df_central = df[df['因子'] == '央行购金']

# 绘制趋势图
plt.figure(figsize=(12, 6))
plt.plot(df_central['年份'], df_central['贡献'], marker='o')
plt.title('央行购金对金价的历史贡献')
plt.xlabel('年份')
plt.ylabel('贡献')
plt.grid(True)
plt.show()
```

### 分析各类别因子的总贡献
```python
import pandas as pd

df = pd.read_csv('results/model_v7_complete_report.csv')

# 按端分组统计
by_sector = df.groupby(['年份', '端'])['贡献'].sum().reset_index()
pivot = by_sector.pivot(index='年份', columns='端', values='贡献')
print(pivot)
```

## 注意事项

1. `results/` 目录下的文件是自动生成的，可以随时删除并重新生成
2. 文件使用 UTF-8 编码，可以在Excel中正常显示中文
3. CSV文件使用逗号分隔，可以导入到大多数数据分析工具
4. Excel文件需要安装 openpyxl 库才能生成

## 获取数据

运行以下命令生成输出文件：

```python
from src.analysis.enhanced_model_v7 import EnhancedGoldPredictionModelV7

model = EnhancedGoldPredictionModelV7()
model.run_complete_analysis()
```

或运行测试脚本：

```bash
python tests/test_model_v7.py
```

或运行示例脚本：

```bash
python examples/example_usage_v7.py
```
