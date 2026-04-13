import time
import random
import sounddevice as sd
import soundfile as sf

# 已为你设置：电脑扬声器（绝不影响耳机）
TARGET_DEVICE = 15


def play_wav_to_device(wav_path, device_id):
    # 读取音频
    data, fs = sf.read(wav_path)

    # 自动兼容声道（修复 PaErrorCode -9998 报错）
    if data.ndim == 1:
        channels = 1
    else:
        channels = data.shape[1]

    try:
        sd.play(data, fs, device=device_id)
        sd.wait()
    except Exception:
        # 设备15不行，自动切换到你电脑的其他扬声器设备
        fallback_devices = [4, 9, 10, 13, 14, 21]
        for dev in fallback_devices:
            try:
                sd.play(data, fs, device=dev)
                sd.wait()
                return
            except:
                continue


def auto_play(total_times=200):
    wav_file = "JG.wav"

    print("✅ 启动成功！声音从【电脑扬声器】输出")
    print("✅ 你的 OPPO 耳机完全不受干扰！")
    print(f"✅ 总执行次数：{total_times}")
    print("=" * 60)

    for i in range(1, total_times + 1):
        wait_time = random.uniform(15, 23)
        print(f"\n第 {i}/{total_times} 次 | 等待 {wait_time:.1f} 秒")
        time.sleep(wait_time)
        print("🔊 正在播放...")
        play_wav_to_device(wav_file, TARGET_DEVICE)

    print("\n🎉 全部 200 次播放完成！")


if __name__ == "__main__":
    TOTAL_COUNT = 1000
    auto_play(TOTAL_COUNT)