# 黄金价格可视化脚本使用指南
# Gold Price Visualization Script User Guide

## 📖 简介 / Introduction

这个脚本生成一个综合性的黄金价格可视化图表（2000-2023），包含年度预测值、实际值、关键驱动因子和重大事件触发器。

This script generates a comprehensive gold price visualization chart (2000-2023) with annual predictions, actual values, key driving factors, and major event triggers.

## 🚀 快速开始 / Quick Start

### 1. 安装依赖 / Install Dependencies

```bash
pip install pandas numpy matplotlib yfinance pillow
```

### 2. 运行脚本 / Run Script

```bash
# 在项目根目录执行 / Execute from project root
python create_gold_price_chart.py
```

### 3. 查看输出 / View Output

生成的文件将保存在 `reports/` 目录：
- `gold_price_complete_visualization.png` - 主可视化图表
- `annual_summary.csv` - 年度数据摘要

Generated files will be saved in `reports/` directory:
- `gold_price_complete_visualization.png` - Main visualization chart
- `annual_summary.csv` - Annual data summary

## 📊 输出示例 / Output Examples

### 可视化图表包含 / Visualization Includes:

1. **金价主曲线** - 2000-2023年周度金价走势
   - Weekly gold price trend (2000-2023)

2. **年度标注** - 每年的预测vs实际值，带准确度标记
   - Annual annotations with predictions vs. actuals and accuracy markers

3. **因子分析** - Top驱动因子及其贡献度
   - Top driving factors and their contributions

4. **事件标记** - 关键触发器事件（如金融危机、QE政策等）
   - Key trigger events (e.g., financial crises, QE policies)

5. **颜色编码** - 绿色=上涨，红色=下跌
   - Color coding: Green = up, Red = down

6. **关键年份高亮** - 2008/2011/2013/2020年加粗边框
   - Key years highlighted: 2008/2011/2013/2020 with bold borders

## 📋 年度数据示例 / Annual Data Example

```csv
年份,预测收益率,实际收益率,预测误差,Top因子,Top因子贡献,触发器
2008,4.30%,4.30%,0.00%,VIX风险指数,8.90%,liquidity_crisis
2020,24.90%,24.90%,0.00%,动量因子,6.25%,"pandemic, unlimited_qe"
```

## 🎨 图表规格 / Chart Specifications

| 属性 / Property | 值 / Value |
|----------------|-----------|
| 尺寸 / Size | 24×14 英寸 / inches |
| 分辨率 / Resolution | 300 DPI |
| 格式 / Format | PNG |
| 像素尺寸 / Pixel Size | 7200×4200 |

## 🔧 自定义 / Customization

### 修改年份范围 / Change Year Range

编辑脚本中的 `ANNUAL_DATA` 字典，添加或删除年份数据。

Edit the `ANNUAL_DATA` dictionary in the script to add or remove years.

### 调整图表大小 / Adjust Chart Size

修改 `create_gold_price_visualization()` 函数中的 `figsize` 参数：

Modify the `figsize` parameter in `create_gold_price_visualization()`:

```python
fig, ax = plt.subplots(figsize=(24, 14), dpi=100)  # Change these values
```

### 更改输出路径 / Change Output Path

修改 `output_path` 变量：

Modify the `output_path` variable:

```python
output_path = 'reports/gold_price_complete_visualization.png'  # Change this
```

## ✅ 测试 / Testing

运行测试套件验证输出：

Run the test suite to verify outputs:

```bash
python -m pytest tests/test_gold_price_visualization.py -v
```

## 📝 注意事项 / Notes

1. **数据源** / Data Source:
   - 优先从Yahoo Finance下载实时数据
   - First attempts to download live data from Yahoo Finance
   - 如无法连接，使用基于年度收益率的模拟数据
   - Falls back to simulated data based on annual returns if unavailable

2. **中文支持** / Chinese Support:
   - 图表支持中文标注
   - Chart supports Chinese annotations
   - 如显示乱码，请安装中文字体
   - Install Chinese fonts if characters appear garbled

3. **性能** / Performance:
   - 首次运行可能需要下载数据（约30秒）
   - First run may take ~30 seconds to download data
   - 后续运行使用模拟数据（约5秒）
   - Subsequent runs use simulated data (~5 seconds)

## 🐛 故障排除 / Troubleshooting

### 问题：中文显示为方框 / Issue: Chinese characters show as boxes

**解决方案** / Solution:
```python
# 在脚本开头添加 / Add at the beginning of script
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei', 'Arial Unicode MS']
```

### 问题：无法下载Yahoo数据 / Issue: Cannot download Yahoo data

**解决方案** / Solution:
脚本会自动使用模拟数据。模拟数据基于实际年度收益率，适合演示和分析。

Script automatically falls back to simulated data. Simulated data is based on actual annual returns and suitable for demo and analysis.

### 问题：内存不足 / Issue: Out of memory

**解决方案** / Solution:
减小图表尺寸或降低DPI：

Reduce chart size or lower DPI:
```python
fig, ax = plt.subplots(figsize=(16, 10), dpi=100)  # Smaller size
plt.savefig(output_path, dpi=150)  # Lower DPI
```

## 📧 支持 / Support

如有问题，请提交GitHub Issue。

For questions, please submit a GitHub Issue.

## 📜 许可证 / License

MIT License - 详见项目根目录LICENSE文件

MIT License - See LICENSE file in project root
