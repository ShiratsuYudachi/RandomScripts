from mido import MidiFile
import numpy as np
midName = '说好的幸福呢.midi'
mid = MidiFile(midName)

sec_per_pai = 60/143
ticktime = sec_per_pai/120


num_notes = 0
output = []
for i in range(len(mid.tracks)):
    isPressed= {}
    currentTick = 0
    notes_list = []
    for note in mid.tracks[i]:#get all effective notes
        if str(note).startswith('note'):
            num_notes+=1
            note_elements = str(note).split(' ')
            notes_list.append([int(note_elements[0]=='note_on'),int(note_elements[2].strip('note=')),int(note_elements[4].strip('time='))])

    for note in notes_list:#extract key info from notes
        currentTick+=note[2]
        if note[0]:
            isPressed[note[1]]=currentTick
        else:
            try:
                startTick = isPressed[note[1]]
                output.append([startTick,note[1],currentTick-startTick])
                del isPressed[note[1]]
            except KeyError:
                startTick = currentTick-note[2]
                output.append([startTick,note[1],currentTick-startTick])

output = np.array(output,dtype=float)
output[:,0]*=ticktime/len(mid.tracks)#这里可能要手动调速，直接再乘一个数字就好了，如果乘1.5就是放慢1.5倍
output[:,2]*=ticktime/len(mid.tracks)
toWrite = ''
for note in output:
    noteLs = [str(x) for x in note]
    noteLs[1] = str(int(note[1]))
    toWrite+='\t'.join(noteLs)+'\n'
#with open(''+midName.strip('.midi')+'.txt','w') as f:
with open('input.txt','w') as f:
    print(1)
    f.write(toWrite)

    