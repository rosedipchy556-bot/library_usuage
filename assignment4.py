from tqdm import tqdm

import time

for i in tqdm(range(20), desc="Completing the task"):
    time.sleep(0.1)

print(f"All 20 tasks completed successfully!. Great job! 🎉")