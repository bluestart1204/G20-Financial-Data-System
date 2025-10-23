"""
导出黄金价格预测模型分析结果并生成可视化图表
Export gold price prediction model analysis results and generate visualizations
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import matplotlib
import warnings

from gold_price_model import GoldPricePredictionModel

# 设置中文字体支持
matplotlib.rcParams['font.sans-serif'] = ['WenQuanYi Zen Hei', 'Noto Sans CJK SC', 'SimHei', 'DejaVu Sans']
matplotlib.rcParams['axes.unicode_minus'] = False

# 忽略字体警告
warnings.filterwarnings('ignore', category=UserWarning, module='seaborn')


def export_factor_contribution_summary(model: GoldPricePredictionModel, 
                                       output_dir: str = 'reports') -> str:
    """
    导出因子贡献汇总表到Excel
    
    Args:
        model: 黄金价格预测模型实例
        output_dir: 输出目录
        
    Returns:
        输出文件路径
    """
    # 创建输出目录
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    # 获取所有年份的分析结果
    results = model.get_all_years_analysis(2000, 2023)
    
    # 准备数据框
    summary_data = []
    
    for result in results:
        year = result['year']
        
        # 创建行数据
        row_data = {'年份': year}
        
        # 添加因子贡献（按贡献度排序）
        factor_contribs = result['factor_contributions']
        sorted_factors = sorted(factor_contribs.items(), 
                               key=lambda x: abs(x[1]), 
                               reverse=True)
        
        for i, (factor_name, contribution) in enumerate(sorted_factors, 1):
            row_data[f'因子{i}'] = factor_name
            row_data[f'因子{i}贡献'] = round(contribution, 2)
        
        # 添加汇总信息
        row_data['因子贡献总和'] = round(result['total_contribution'], 2)
        row_data['触发器贡献'] = round(result['trigger_contribution'], 2)
        
        # 添加激活的触发器名称
        activated_triggers = [name for name, activated 
                            in result['trigger_activations'].items() 
                            if activated]
        row_data['激活触发器'] = ', '.join(activated_triggers) if activated_triggers else '无'
        
        row_data['预测涨跌'] = round(result['predicted_return'], 2)
        row_data['实际涨跌'] = round(result['actual_return'], 2)
        row_data['差异'] = round(result['difference'], 2)
        
        summary_data.append(row_data)
    
    # 创建DataFrame
    df_summary = pd.DataFrame(summary_data)
    
    # 导出到Excel
    output_file = os.path.join(output_dir, 'factor_contribution_summary.xlsx')
    
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        # 写入汇总表
        df_summary.to_excel(writer, sheet_name='因子贡献汇总', index=False)
        
        # 创建详细的因子贡献矩阵
        factors_matrix = []
        years = []
        
        for result in results:
            years.append(result['year'])
            row = [result['factor_contributions'][factor] 
                   for factor in model.base_weights.keys()]
            factors_matrix.append(row)
        
        df_factors = pd.DataFrame(
            factors_matrix,
            index=years,
            columns=list(model.base_weights.keys())
        )
        df_factors.to_excel(writer, sheet_name='因子贡献矩阵')
        
        # 创建触发器激活记录
        triggers_matrix = []
        
        for result in results:
            row = [1 if result['trigger_activations'][trigger] else 0
                   for trigger in model.triggers.keys()]
            triggers_matrix.append(row)
        
        df_triggers = pd.DataFrame(
            triggers_matrix,
            index=years,
            columns=list(model.triggers.keys())
        )
        df_triggers.to_excel(writer, sheet_name='触发器激活记录')
    
    print(f"✅ 因子贡献汇总表已导出: {output_file}")
    return output_file


def generate_factor_heatmap(model: GoldPricePredictionModel, 
                           output_dir: str = 'reports') -> str:
    """
    生成因子贡献热力图
    
    Args:
        model: 黄金价格预测模型实例
        output_dir: 输出目录
        
    Returns:
        输出文件路径
    """
    # 创建输出目录
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    # 获取所有年份的分析结果
    results = model.get_all_years_analysis(2000, 2023)
    
    # 创建因子贡献矩阵
    factors_matrix = []
    years = []
    
    for result in results:
        years.append(result['year'])
        row = [result['factor_contributions'][factor] 
               for factor in model.base_weights.keys()]
        factors_matrix.append(row)
    
    df_factors = pd.DataFrame(
        factors_matrix,
        index=years,
        columns=list(model.base_weights.keys())
    )
    
    # 绘制热力图
    plt.figure(figsize=(14, 10))
    sns.heatmap(df_factors.T, 
                annot=False, 
                cmap='RdYlGn', 
                center=0,
                cbar_kws={'label': '贡献度 (%)'},
                linewidths=0.5,
                linecolor='gray')
    
    plt.title('黄金价格因子贡献热力图 (2000-2023)', fontsize=16, pad=20)
    plt.xlabel('年份', fontsize=12)
    plt.ylabel('因子', fontsize=12)
    plt.xticks(rotation=45)
    plt.yticks(rotation=0)
    plt.tight_layout()
    
    output_file = os.path.join(output_dir, 'factor_heatmap.png')
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"✅ 因子贡献热力图已生成: {output_file}")
    return output_file


def generate_factor_trends(model: GoldPricePredictionModel, 
                          output_dir: str = 'reports') -> str:
    """
    生成年度因子贡献趋势图
    
    Args:
        model: 黄金价格预测模型实例
        output_dir: 输出目录
        
    Returns:
        输出文件路径
    """
    # 创建输出目录
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    # 获取所有年份的分析结果
    results = model.get_all_years_analysis(2000, 2023)
    
    # 创建因子贡献矩阵
    factors_matrix = []
    years = []
    
    for result in results:
        years.append(result['year'])
        row = [result['factor_contributions'][factor] 
               for factor in model.base_weights.keys()]
        factors_matrix.append(row)
    
    df_factors = pd.DataFrame(
        factors_matrix,
        index=years,
        columns=list(model.base_weights.keys())
    )
    
    # 绘制趋势图
    plt.figure(figsize=(16, 10))
    
    for column in df_factors.columns:
        plt.plot(df_factors.index, df_factors[column], 
                marker='o', markersize=4, linewidth=2, 
                label=column, alpha=0.8)
    
    plt.title('黄金价格因子贡献趋势图 (2000-2023)', fontsize=16, pad=20)
    plt.xlabel('年份', fontsize=12)
    plt.ylabel('贡献度 (%)', fontsize=12)
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1), fontsize=10)
    plt.grid(True, alpha=0.3, linestyle='--')
    plt.axhline(y=0, color='black', linestyle='-', linewidth=0.5)
    
    # 添加关键事件标注
    events = {
        2008: '金融危机',
        2010: '主权债务危机',
        2018: '贸易战',
        2020: '疫情冲击',
    }
    
    for year, event in events.items():
        plt.axvline(x=year, color='red', linestyle=':', alpha=0.5, linewidth=1)
        plt.text(year, plt.ylim()[1] * 0.95, event, 
                rotation=90, verticalalignment='top',
                fontsize=9, alpha=0.7)
    
    plt.tight_layout()
    
    output_file = os.path.join(output_dir, 'factor_trends.png')
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"✅ 因子贡献趋势图已生成: {output_file}")
    return output_file


def generate_trigger_statistics(model: GoldPricePredictionModel, 
                                output_dir: str = 'reports') -> str:
    """
    生成触发器激活统计图表
    
    Args:
        model: 黄金价格预测模型实例
        output_dir: 输出目录
        
    Returns:
        输出文件路径
    """
    # 创建输出目录
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    # 获取所有年份的分析结果
    results = model.get_all_years_analysis(2000, 2023)
    
    # 统计各触发器的激活次数
    trigger_counts = {trigger: 0 for trigger in model.triggers.keys()}
    
    for result in results:
        for trigger, activated in result['trigger_activations'].items():
            if activated:
                trigger_counts[trigger] += 1
    
    # 准备数据
    triggers = list(trigger_counts.keys())
    counts = list(trigger_counts.values())
    
    # 绘制条形图
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
    
    # 左图：触发器激活次数
    colors = plt.cm.Set3(range(len(triggers)))
    bars = ax1.bar(triggers, counts, color=colors, edgecolor='black', linewidth=1.5)
    
    ax1.set_title('触发器激活次数统计 (2000-2023)', fontsize=14, pad=15)
    ax1.set_xlabel('触发器', fontsize=12)
    ax1.set_ylabel('激活次数', fontsize=12)
    ax1.set_ylim(0, max(counts) + 2)
    ax1.grid(True, alpha=0.3, axis='y', linestyle='--')
    
    # 在条形上显示数值
    for bar, count in zip(bars, counts):
        height = bar.get_height()
        ax1.text(bar.get_x() + bar.get_width()/2., height,
                f'{int(count)}',
                ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    plt.setp(ax1.xaxis.get_majorticklabels(), rotation=45, ha='right')
    
    # 右图：触发器时间线
    trigger_timeline = []
    years = []
    
    for result in results:
        years.append(result['year'])
        row = [1 if result['trigger_activations'][trigger] else 0
               for trigger in model.triggers.keys()]
        trigger_timeline.append(row)
    
    df_timeline = pd.DataFrame(
        trigger_timeline,
        index=years,
        columns=list(model.triggers.keys())
    )
    
    sns.heatmap(df_timeline.T, 
                cmap=['white', 'red'], 
                cbar=False,
                linewidths=1,
                linecolor='gray',
                ax=ax2)
    
    ax2.set_title('触发器激活时间线', fontsize=14, pad=15)
    ax2.set_xlabel('年份', fontsize=12)
    ax2.set_ylabel('触发器', fontsize=12)
    ax2.set_xticklabels(ax2.get_xticklabels(), rotation=45, ha='right')
    ax2.set_yticklabels(ax2.get_yticklabels(), rotation=0)
    
    plt.tight_layout()
    
    output_file = os.path.join(output_dir, 'trigger_statistics.png')
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.close()
    
    print(f"✅ 触发器激活统计图表已生成: {output_file}")
    return output_file


def main():
    """主函数：生成所有报告和图表"""
    print("=" * 60)
    print("黄金价格预测模型 - 因子贡献分析报告生成")
    print("Gold Price Prediction Model - Factor Contribution Analysis")
    print("=" * 60)
    print()
    
    # 创建模型实例
    print("📊 初始化黄金价格预测模型...")
    model = GoldPricePredictionModel()
    print("✅ 模型初始化完成")
    print()
    
    # 设置输出目录 - 使用项目根目录的 reports/
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(os.path.dirname(script_dir))
    output_dir = os.path.join(project_root, 'reports')
    
    # 1. 导出Excel汇总表
    print("📝 正在生成因子贡献汇总表...")
    excel_file = export_factor_contribution_summary(model, output_dir)
    print()
    
    # 2. 生成热力图
    print("🎨 正在生成因子贡献热力图...")
    heatmap_file = generate_factor_heatmap(model, output_dir)
    print()
    
    # 3. 生成趋势图
    print("📈 正在生成因子贡献趋势图...")
    trends_file = generate_factor_trends(model, output_dir)
    print()
    
    # 4. 生成触发器统计图
    print("🔔 正在生成触发器激活统计图...")
    trigger_file = generate_trigger_statistics(model, output_dir)
    print()
    
    # 显示摘要
    print("=" * 60)
    print("✅ 所有报告和图表生成完成！")
    print("=" * 60)
    print()
    print("📁 生成的文件：")
    print(f"  1. {excel_file}")
    print(f"  2. {heatmap_file}")
    print(f"  3. {trends_file}")
    print(f"  4. {trigger_file}")
    print()
    print("=" * 60)


if __name__ == '__main__':
    main()
