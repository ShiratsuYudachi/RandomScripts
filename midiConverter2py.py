def convert_freq(pitch):
    # 提供pitch到频率的转换。你可能需要调整这个函数。
    return 440.0 * 2.0**((pitch-69)/12.0)

def read_file(filename):
    with open(filename, "r") as file:
        data = file.readlines()
    return [line.split() for line in data]

def generate_c_code(notes):
    c_code = []
    i = 0
    
    while i < len(notes):
        start_time, pitch, duration = notes[i]
        
        # 对于同时开始的多个音符，计算pitch的平均值
        pitches = [float(pitch)]
        duration = float(duration)
        j = i + 1
        while j < len(notes) and float(notes[j][0]) == float(start_time):
            pitches.append(float(notes[j][1]))
            j += 1

        avg_pitch = sum(pitches) / len(pitches)
        freq = convert_freq(avg_pitch)
        duration_ms = int(duration * 1000) * 0.5# 这里可以自定义multiplier
        pause_ms = 0# 可根据需要调整

        c_code.append(f"playFreq({freq:.2f}, {duration_ms}, {pause_ms});")
        
        i = j  # 跳过相同开始时间的音符

    return c_code

def save_to_c_file(c_code, filename):
    with open(filename, "w") as file:
        for line in c_code:
            file.write("    " + line + "\n")
            
# 示例
input_filename = "input.txt"  # 假设你的音符数据在这个文件中
output_filename = "output.c"   # 生成的C代码将保存在这个文件中

notes = read_file(input_filename)
c_code = generate_c_code(notes)
save_to_c_file(c_code, output_filename)
