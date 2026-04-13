import time
import random
import sounddevice as sd
import soundfile as sf

# ==============================================
# 第一步：先运行一次，查看你的设备列表
# 第二步：找到【扬声器阵列】的数字，填到下面
# ==============================================
TARGET_DEVICE = 2  # 改成你扬声器阵列的编号


def list_all_devices():
    """列出所有音频输出设备"""
    print("\n" + "=" * 60)
    print("【你的所有音频设备】")
    print("=" * 60)
    devices = sd.query_devices()
    for i, dev in enumerate(devices):
        print(f"设备编号 [{i}] —— {dev['name']}")
    print("\n请找到【扬声器阵列】对应的数字，填到上方 TARGET_DEVICE")
    print("=" * 60)


def play_wav_to_device(wav_path, device_id):
    """指定设备播放wav，不影响其他设备"""
    data, fs = sf.read(wav_path)
    sd.play(data, fs, device=device_id)
    sd.wait()  # 等待播放完毕


def auto_play(total_times=200):
    wav_file = "JG.wav"

    # 先打印设备列表
    list_all_devices()

    print(f"\n✅ 已启动，总次数：{total_times}")
    print(f"✅ 音频将从 设备{TARGET_DEVICE} 播放")
    print("=" * 60)

    for i in range(1, total_times + 1):
        wait_time = random.uniform(12, 20)
        print(f"\n第 {i}/{total_times} 次 | 等待 {wait_time:.1f} 秒")
        time.sleep(wait_time)

        print("正在播放...")
        play_wav_to_device(wav_file, TARGET_DEVICE)

    print("\n🎉 全部播放完成！")


if __name__ == "__main__":
    TOTAL_COUNT = 200
    auto_play(TOTAL_COUNT)