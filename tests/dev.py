# Fixing the scaffolding directory definition
import sys
former_path = sys.path[0]
new_path = former_path + '/../'
sys.path.insert(0, new_path)
print(sys.path[0])

from src.GUI import GUI

gui = GUI()

gui.run()
