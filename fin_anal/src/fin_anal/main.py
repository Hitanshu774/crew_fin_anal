#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from fin_anal.crew import FinAnal

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the financial analyser.
    """
    inputs = {
        'company': "BlackRock"
    }

    result = FinAnal().crew().kickoff(inputs=inputs)
    print(result.raw)
    
if __name__ == "__main__":
    run()
