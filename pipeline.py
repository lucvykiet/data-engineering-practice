import subprocess

def run_step(name, path):
    print(f"\n🔧 Đang chạy {name}...")
    result = subprocess.run(f"python \"{path}\"", shell=True)
    if result.returncode != 0:
        print(f"❌ Lỗi ở bước {name}")
        exit(1)
    print(f"✅ {name} hoàn thành")

if __name__ == "__main__":
    run_step("Bài tập 1", "Exercise-1/main.py")
    run_step("Bài tập 2", "Exercise-2/main.py")
    run_step("Bài tập 3", "Exercise-3/main.py")
    run_step("Bài tập 4", "Exercise-4/main.py")
    run_step("Bài tập 5", "Exercise-5/main.py")
