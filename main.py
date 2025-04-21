#!/usr/bin/env python3
"""
Main module
Author: Jordy Garzón
"""

import pandas as pd
import numpy as np
from datetime import datetime

class DataProcessor:
    def __init__(self):
        self.data = None
        print("Initialized DataProcessor")
    
    def load_data(self, filepath):
        self.data = pd.read_csv(filepath)
        print(f"Loaded {len(self.data)} records")
        return self.data
    
    def process(self):
        print("Processing data...")
        # Add processing logic here
        return self.data
    
    def save(self, output_path):
        self.data.to_csv(output_path, index=False)
        print(f"Saved to {output_path}")

if __name__ == "__main__":
    processor = DataProcessor()
    print("Ready to process data")
