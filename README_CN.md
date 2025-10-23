# 🌍 G20金融数据系统

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![数据覆盖](https://img.shields.io/badge/coverage-1980--2025-orange.svg)
![国家数量](https://img.shields.io/badge/countries-20-red.svg)
![数据点](https://img.shields.io/badge/data_points-20万+-brightgreen.svg)

覆盖G20全部国家（1980-2025）的综合性多频率金融经济数据系统。

**[English](README.md)** | **[文档](docs/)** | **[快速开始](docs/quick_start.md)** | **[示例](examples/)**

---

## 🎯 项目概述

本项目提供**全球最完整的G20金融数据集**，特色功能包括：

- 📊 **20万+数据点**，跨越45年（1980-2025）
- 🌍 **20个国家/地区**：G20全部成员
- 📈 **多频率数据**：季度 + 月度
- 💰 **5大数据类别**：GDP、M2、政府债务、美债持有、黄金储备
- 🏦 **17国央行资产负债表**
- 🇺🇸 **18国持有美债明细**（月度，2015-2024）
- 🥇 **13国黄金储备**（月度，2015-2024）

---

## 📊 数据结构

### 季度数据 (1980Q1 - 2025Q4)
```
GDP:        184季度 × 21国 = 3,864点
M2货币供应:  184季度 × 21国 = 3,864点
政府债务:    184季度 × 21国 = 3,864点
```

### 月度数据 (2015M01 - 2024M10)
```
美债持有量: 118月 × 18国 = 2,124点
黄金储备:   118月 × 13国 = 1,534点
```

**总计**: 15,250+经过验证的数据点 ✅

---

## 🚀 快速开始

### 安装

```bash
# 克隆仓库
git clone https://github.com/bluestart1204/G20-Financial-Data-System.git
cd G20-Financial-Data-System

# 安装依赖
pip install -r requirements.txt
```

### 基础用法

```python
import pandas as pd

# 加载季度GDP数据
gdp = pd.read_csv('data/processed/quarterly_data/g20_gdp_quarterly.csv', 
                  index_col=0, parse_dates=True)

# 加载月度美债持有数据
ust = pd.read_csv('data/processed/monthly_data/g20_us_treasury_monthly.csv',
                  index_col=0, parse_dates=True)

# 分析中国去美元化趋势
china_ust = ust['中国']
peak_value = china_ust.max()
current_value = china_ust.iloc[-1]
change_pct = (current_value - peak_value) / peak_value * 100

print(f"中国持有美债:")
print(f"  当前 (2024年10月): ${current_value:.1f}B")
print(f"  峰值: ${peak_value:.1f}B")
print(f"  变化: {change_pct:.1f}%")
```

**输出:**
```
中国持有美债:
  当前 (2024年10月): $780.0B
  峰值: $1316.0B
  变化: -41.1%
```

---

## 📈 核心特色

### 1. **全面覆盖**
- ✅ G20全部国家/地区
- ✅ 45年时间跨度（1980-2025）
- ✅ 多种数据频率（季度+月度）
- ✅ 统一单位（十亿美元）

### 2. **高数据质量**
- 📍 **数据来源**: FRED、IMF、BIS、美国财政部、世界黄金协会、各国央行
- 🔍 **严格验证**: 交叉核对和修正
- 🔄 **定期更新**: 跟随官方发布更新
- 📊 **完整性**: 98%+数据完整度

### 3. **分析就绪**
- 📉 **时间序列**: ARIMA、VAR、VECM、协整检验
- 🎯 **事件研究**: 金融危机、政策冲击
- 🤖 **机器学习**: LSTM、Prophet、XGBoost
- 🕸️ **网络分析**: 金融联系、溢出效应

### 4. **完善文档**
- 📖 完整的数据字典
- 📝 方法论说明
- 💡 研究案例
- 🔧 API参考

---

## 🎓 研究应用

### 学术研究
- **经济学**: 全球经济周期、货币政策传导、跨国溢出效应
- **金融学**: 去美元化趋势、央行资产配置、避险资产分析
- **国际政治经济学**: 金融霸权、货币武器化、经济制裁
- **中国研究**: 货币政策框架、人民币国际化、一带一路

**适合发表于**:
- Journal of International Economics
- Journal of Finance
- Review of Economic Studies
- The China Quarterly

### 政策分析
- 央行与监管机构
- 国际组织（IMF、世界银行、BIS）
- 政府经济部门
- 智库和研究机构

### 商业应用
- 💼 资产配置策略
- ⚠️  风险管理和对冲
- 📊 宏观经济预测
- 💰 投资决策支持

---

## 📊 关键发现

### 1. 去美元化趋势 (2013-2024)

| 国家 | 峰值持有量 | 当前 (2024) | 变化 | 状态 |
|------|-----------|-------------|------|------|
| 🇷🇺 俄罗斯 | $164B (2013) | $0.1B | **-99.9%** | ❌ 清空 |
| 🇹🇷 土耳其 | $55B (2017) | $8B | **-85.5%** | 📉 大幅减持 |
| 🇨🇳 中国 | $1,316B (2013) | $775B | **-41.1%** | 📉 显著减持 |
| 🇸🇦 沙特 | $180B (2019) | $110B | **-38.9%** | 📉 持续减持 |

### 2. 黄金储备增持 (2015-2024)

| 国家 | 2015 | 2024 | 增长 | 趋势 |
|------|------|------|------|------|
| 🇷🇺 俄罗斯 | $50B | $160B | **+220%** | 📈 激进增持 |
| 🇨🇳 中国 | $60B | $145B | **+142%** | 📈 稳步增持 |
| 🇹🇷 土耳其 | $12B | $37B | **+208%** | 📈 快速增持 |
| 🇮🇳 印度 | $20B | $50B | **+150%** | 📈 持续增长 |

### 3. 央行资产扩张

```
G20央行总资产: $29.5万亿 (2024)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
欧洲央行:     $7.29万亿  (24.7%)
美联储:       $6.59万亿  (22.3%)
中国人民银行: $6.21万亿  (21.1%)
日本央行:     $5.00万亿  (16.9%)
其他:         $4.41万亿  (14.9%)
```

---

## 📚 数据来源

### 主要来源
- **[FRED](https://fred.stlouisfed.org/)** - 美联储经济数据
- **[IMF](https://www.imf.org/)** - 国际货币基金组织
- **[BIS](https://www.bis.org/)** - 国际清算银行
- **[美国财政部TIC](https://ticdata.treasury.gov/)** - 国际资本流动
- **[世界黄金协会](https://www.gold.org/)** - 官方黄金统计

### 各国央行
- 🇨🇳 中国人民银行 (PBOC)
- 🇯🇵 日本央行 (BOJ)
- 🇪🇺 欧洲央行 (ECB)
- 🇬🇧 英国央行 (BOE)
- 🇨🇦 加拿大央行 (BOC)
- 🇦🇺 澳洲储备银行 (RBA)
- 以及其他11国...

---

---

## 🆕 最新功能：黄金价格预测模型 V7.0

新增**黄金价格因子分析系统**，对2000-2023年的黄金价格因子贡献进行深度分析。

### 功能特点：
- ✅ **逐年分析** (2000-2023)
- ✅ **7个核心因子**，优化权重
- ✅ **五层分析框架**（原始数据→最终贡献）
- ✅ **触发器机制**，应对极端事件
- ✅ **自动报告生成** (CSV + Excel)

### 快速开始：

```bash
# 运行完整分析（所有年份）
python analyze_factors.py

# 运行2023年演示
python demo_2023_analysis.py

# 运行测试
python test_model.py
```

### 输出文件：
- `reports/year_YYYY_contributions.csv` - 单独年份报告
- `reports/factor_contribution_2000_2023.xlsx` - 完整汇总
- `reports/trigger_analysis_2000_2023.xlsx` - 触发器分析

📖 **[完整文档](FACTOR_ANALYSIS_README.md)** | **[实现细节](IMPLEMENTATION_SUMMARY.md)**

---

## 📖 文档

- 📘 [数据字典](docs/data_dictionary.md) - 变量定义和来源
- 📗 [方法论](docs/methodology.md) - 数据采集和处理方法
- 📕 [快速开始指南](docs/quick_start.md) - 5分钟上手
- 📙 [研究案例](docs/research_examples.md) - 示例分析和代码

---

## 🤝 参与贡献

欢迎贡献！请先阅读[贡献指南](CONTRIBUTING.md)。

### 贡献方式
- 🐛 报告bug和问题
- 💡 建议新功能或数据源
- 📝 改进文档
- 🔧 提交代码
- 🌟 分享您使用本数据的研究

---

## 📜 许可证

本项目采用**MIT许可证** - 详见[LICENSE](LICENSE)文件。

### 这意味着:
✅ 允许商业使用  
✅ 允许修改  
✅ 允许分发  
✅ 允许私人使用  
⚠️  必须包含许可证和版权声明  

---

## 📧 联系方式

- **作者**: bluestart1204
- **邮箱**: wanglei913422@gmail.com
- **GitHub**: [@bluestart1204](https://github.com/bluestart1204/G20-Financial-Data-System)
- **问题反馈**: [GitHub Issues](https://github.com/bluestart1204/G20-Financial-Data-System/issues)
- **讨论区**: [GitHub Discussions](https://github.com/bluestart1204/G20-Financial-Data-System/discussions)

---

## 🌟 Star历史

如果觉得这个项目有用，请给个星标！⭐

[![Star History Chart](https://api.star-history.com/svg?repos=bluestart1204/G20-Financial-Data-System&type=Date)](https://star-history.com/#bluestart1204/G20-Financial-Data-System&Date)

---

## 📖 引用

如果您在研究中使用了本数据集，请引用：

```bibtex
@misc{g20_financial_data_2025,
  author = {bluestart1204},
  title = {G20金融数据系统：综合性多频率数据集 (1980-2025)},
  year = {2025},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/bluestart1204/G20-Financial-Data-System}},
  note = {Version 1.0}
}
```

---

## 🙏 致谢

本项目基于以下机构的数据:
- 美联储经济数据（FRED）
- 国际货币基金组织（IMF）
- 国际清算银行（BIS）
- 美国财政部
- 世界黄金协会
- G20各国央行

感谢开源社区提供的工具和库，使本项目成为可能。

---

**⭐ 如果觉得这个项目有用，请给个星标！您的支持是持续开发的动力。**

**🔔 Watch本仓库以获取更新和新功能通知。**

---

*最后更新: 2025-10-16*  
*版本: 1.0.0*  
*维护者: [bluestart1204](https://github.com/bluestart1204/G20-Financial-Data-System)*
