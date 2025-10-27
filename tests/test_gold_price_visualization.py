#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test suite for gold price visualization script
"""

import os
import sys
import pytest
import pandas as pd
from PIL import Image

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestGoldPriceVisualization:
    """Tests for the gold price visualization outputs"""
    
    @pytest.fixture
    def reports_dir(self):
        """Get the reports directory path"""
        return os.path.join(os.path.dirname(os.path.dirname(__file__)), 'reports')
    
    def test_reports_directory_exists(self, reports_dir):
        """Test that reports directory exists"""
        assert os.path.exists(reports_dir), "Reports directory should exist"
        assert os.path.isdir(reports_dir), "Reports should be a directory"
    
    def test_visualization_png_exists(self, reports_dir):
        """Test that visualization PNG file exists"""
        png_path = os.path.join(reports_dir, 'gold_price_complete_visualization.png')
        assert os.path.exists(png_path), "Visualization PNG should exist"
    
    def test_annual_summary_csv_exists(self, reports_dir):
        """Test that annual summary CSV exists"""
        csv_path = os.path.join(reports_dir, 'annual_summary.csv')
        assert os.path.exists(csv_path), "Annual summary CSV should exist"
    
    def test_visualization_image_properties(self, reports_dir):
        """Test that visualization image has correct properties"""
        png_path = os.path.join(reports_dir, 'gold_price_complete_visualization.png')
        
        if not os.path.exists(png_path):
            pytest.skip("PNG file not found")
        
        img = Image.open(png_path)
        
        # Test image size (should be 24x14 inches at 300 DPI = 7200x4200 pixels)
        assert img.size[0] == 7200, f"Width should be 7200 pixels, got {img.size[0]}"
        assert img.size[1] == 4200, f"Height should be 4200 pixels, got {img.size[1]}"
        
        # Test format
        assert img.format == 'PNG', f"Format should be PNG, got {img.format}"
    
    def test_annual_summary_csv_content(self, reports_dir):
        """Test that annual summary CSV has correct content"""
        csv_path = os.path.join(reports_dir, 'annual_summary.csv')
        
        if not os.path.exists(csv_path):
            pytest.skip("CSV file not found")
        
        df = pd.read_csv(csv_path)
        
        # Test that we have data for 24 years (2000-2023)
        assert len(df) == 24, f"Should have 24 years of data, got {len(df)}"
        
        # Test column names
        expected_columns = ['年份', '预测收益率', '实际收益率', '预测误差', 
                          'Top因子', 'Top因子贡献', '触发器']
        for col in expected_columns:
            assert col in df.columns, f"Column '{col}' should exist in CSV"
        
        # Test year range
        assert df['年份'].min() == 2000, "Minimum year should be 2000"
        assert df['年份'].max() == 2023, "Maximum year should be 2023"
    
    def test_annual_data_has_key_years(self, reports_dir):
        """Test that key years (2008, 2011, 2013, 2020) are present"""
        csv_path = os.path.join(reports_dir, 'annual_summary.csv')
        
        if not os.path.exists(csv_path):
            pytest.skip("CSV file not found")
        
        df = pd.read_csv(csv_path)
        key_years = [2008, 2011, 2013, 2020]
        
        for year in key_years:
            assert year in df['年份'].values, f"Key year {year} should be in data"


if __name__ == '__main__':
    pytest.main([__file__, '-v'])
